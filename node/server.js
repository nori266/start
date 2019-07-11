const R = require("ramda");
const express = require("express");
const http = require("http");
const WebSocket = require("ws");
const queryString = require("query-string");
const protoLoader = require("@grpc/proto-loader");
const grpc = require("grpc");
const crypto = require("crypto");
const wav = require("wav");
const path = require("path");

const logger = console;

const appId = process.env.APP_ID;
if (appId === undefined) {
  throw new Error("APP_ID environment variable needs to be set");
}

let sgApiUrl;
let creds;
if (process.env.SG_API_URL) {
  sgApiUrl = process.env.SG_API_URL;
  creds = grpc.credentials.createInsecure();
} else {
  sgApiUrl = "api.speechgrinder.com";
  creds = grpc.credentials.createSsl();
}

logger.debug(`Using ${sgApiUrl} with appId "${appId}"`);

const SgGrpc = grpc.loadPackageDefinition(
  protoLoader.loadSync("../sg.proto", {
    keepCase: false,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
  })
);

const errors = {
  S01: "Invalid session",
  S02: "Invalid deviceId",
  C01: "Client version too old",
  G01: "General failure"
};

const processError = websocket => error => {
  if (websocket.readyState === 1) {
    if (error.code == 11) {
      logger.error(error.details);
      return;
    }
    logger.error(error);
    logger.error("Sending error message to client...");
    websocket.send(JSON.stringify({ event: "error", data: { error: error.message, code: "G01" } }));
    logger.error("Closing websocket...");
  }
};

const processData = (websocket) => {
  return data => {
    if (websocket.readyState !== 1) {
      // client websocket is not writable, ignore result
      return;
    }
    if (data.started !== undefined) {
      // slu api returns an utterance id
      websocket.send(JSON.stringify({ event: "started", data: data.started }));
    } else if (data.finished !== undefined) {
      websocket.send(JSON.stringify({ event: "stopped", data: data.finished }));
    } else {
      const tokens = data.utterance.alternatives[0].tokens.map(tok => {
        return {text: tok.text, lemma: tok.lemma, pos: tok.pos}
      });
      if (websocket.readyState === 1 && !R.isEmpty(tokens)) {
        try {
          websocket.send(
            JSON.stringify({
              event: "transcription",
              data: { utteranceId: data.utterance.utteranceId, type: data.utterance.type, tokens: tokens }
            })
          );
        } catch (err) {
          logger.log( err )
          processError(websocket)(err);
        }
      }
    }
  };
};

const handler = (ws, token, params) => {
  const sampleRateHertz = params.sampleRate ? parseInt(params.sampleRate) : 48000;
  const languageCode = params.languageCode || "fi-FI";

  const config = {
    channels: 1,
    sampleRateHertz: sampleRateHertz,
    languageCode: languageCode
  };

  logger.debug(`WebSocket opened with parameters ${JSON.stringify(config)}`);

  const client = new SgGrpc.speechgrinder.sgapi.v1.Slu(sgApiUrl, creds);
  const metadata = new grpc.Metadata();
  metadata.add("Authorization", `Bearer ${token}`);
  const recognizer = client.Stream(metadata);
  recognizer.write({ config });
  recognizer.on("error", processError(ws));
  recognizer.on("data", processData(ws));

  ws.on("error", error => {
    logger.error("ws got error");
    logger.error(error);
    recognizer.end();
  });

  ws.on("message", message => {
    if (typeof message === "string") {
      // command event, not audio
      const event = JSON.parse(message);
      if (event.event === "start") {
        return recognizer.write({ event: { event: "START" } });
      } else if (event.event === "stop") {
        return recognizer.write({ event: { event: "STOP" } });
      } else if (event.event === "quit") {
        return recognizer.end();
      } else {
        logger.debug("Invalid message from a client:");
        logger.debug(message);
        return ws.send(
          JSON.stringify({ event: "error", data: { code: "C01", details: "Unknown event from the client" } })
        );
      }
    } else {
      if (recognizer.writable) {
        try {
          recognizer.write({ audio: message });
        } catch (err) {
          logger.error("Error in handling binary message from client");
          logger.error(err);
          ws.send(
            JSON.stringify({
              event: "error",
              data: { error: err, code: "G01" }
            })
          );
        }
      }
    }
  });
  ws.on("close", () => {
    logger.debug("Client WebSocket closed");
    recognizer.end();
    client.close();
  });
};

const kParams = Symbol("session");
const kToken = Symbol("token");
const kError = Symbol("error");

const createToken = deviceId => {
  const client = new SgGrpc.speechgrinder.sgapi.v1.Identity(sgApiUrl, creds);
  return new Promise((resolve, reject) => {
    client.login({ deviceId, appId }, (err, response) => {
      if (err) {
        return reject(err);
      }
      logger.debug(`Created new token ${response.token}`);
      return resolve(response.token);
    });
  });
};

const verifyClient = (info, cb) => {
  const url = info.req.url;
  const queryStr = url.split("?")[1];
  if (queryStr === undefined) {
    return Promise.reject(new Error("Missing query string"));
  }

  const params = queryString.parse(queryStr);
  const findDeviceId = () => {
    if (params.deviceId !== undefined) {
      return params.deviceId;
    } else {
      if (info.req.headers["user-agent"] === undefined) {
        info.req[kError] = JSON.stringify({
          event: "error",
          data: {
            error: errors["S02"],
            code: "S02"
          }
        });
      } else {
        return crypto
          .createHash("md5")
          .update(info.req.headers["user-agent"])
          .digest("hex");
      }
    }
  };

  info.req[kParams] = params;
  return Promise.resolve()
    .then(() => {
      // TODO: find token from cookie or local storage
      const token = info.req.headers.jwt;
      if (token === undefined) {
        return createToken(findDeviceId());
      }
      return Promise.resolve(token);
    })
    .then(token => {
      // TODO: store the token as cookie or local storage
      info.req[kToken] = token;
    })
    .catch(err => {
      const code = err.message || "G01";
      info.req[kError] = JSON.stringify({
        event: "error",
        data: {
          error: errors[code],
          code: code
        }
      });
    })
    .then(() => {
      // verify always succeeds, errors are sent as a WebSocket message
      cb(true);
    });
};

const handleWebSocketConnection = (ws, req) => {
  // the request is already verified by verifyClient
  if (req.hasOwnProperty(kError)) {
    logger.error("Sending error to client", req[kError]);
    ws.send(req[kError]);
    ws.close();
  } else {
    handler(ws, req[kToken], req[kParams]);
  }
};

const bindWebSocket = server => {
  const ws = new WebSocket.Server({ perMessageDeflate: false, server, verifyClient });
  ws.on("connection", handleWebSocketConnection);
};

process.on("unhandledRejection", (reason, p) => {
  logger.error("Unhandled rejection");
  logger.error(reason);
});

process.on("uncaughtException", err => {
  logger.error("Uncaught exception cxdgaught, logging and exiting");
  logger.error(err);
  process.exitCode = 2;
});

const shutdown = () => {
  logger.info("Shutdown requested");
  process.exit();
};

process.on("SIGTERM", shutdown);
process.on("SIGINT", shutdown);

const httpApp = express();
httpApp.get("/", (req, res) => {
  const baseUrl = req.headers["x-envoy-original-path"] || req.baseUrl;
  res.redirect(baseUrl + "/index.html");
});
httpApp.use(express.static("../www", { index: false }));

const httpServer = http.createServer(httpApp);
bindWebSocket(httpServer);

const port = process.env.PORT || 8080;
httpServer.listen(port, () => {
  logger.info(`HTTP Server listening on port: ${port}`);
});
