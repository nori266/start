# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import sg_pb2 as sg__pb2


class SluStub(object):
  """Speechgrinder spoken language understanding service

  This service requires that the user has an accesstoken from
  `Identity` service. The token must be included in the metadata as
  `Authorization` key with value `Bearer TOKEN_HERE`.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Stream = channel.stream_stream(
        '/speechgrinder.sgapi.v1.Slu/Stream',
        request_serializer=sg__pb2.SluRequest.SerializeToString,
        response_deserializer=sg__pb2.SluResponse.FromString,
        )


class SluServicer(object):
  """Speechgrinder spoken language understanding service

  This service requires that the user has an accesstoken from
  `Identity` service. The token must be included in the metadata as
  `Authorization` key with value `Bearer TOKEN_HERE`.
  """

  def Stream(self, request_iterator, context):
    """Starts an SLU bidirectional stream, the input and output
    messages explains the details of the call.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SluServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Stream': grpc.stream_stream_rpc_method_handler(
          servicer.Stream,
          request_deserializer=sg__pb2.SluRequest.FromString,
          response_serializer=sg__pb2.SluResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'speechgrinder.sgapi.v1.Slu', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class IdentityStub(object):
  """Authentication and identity service
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Login = channel.unary_unary(
        '/speechgrinder.sgapi.v1.Identity/Login',
        request_serializer=sg__pb2.LoginRequest.SerializeToString,
        response_deserializer=sg__pb2.LoginResponse.FromString,
        )


class IdentityServicer(object):
  """Authentication and identity service
  """

  def Login(self, request, context):
    """Performs a login for the user, when successful it returns an
    access token to access `Slu` service.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IdentityServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Login': grpc.unary_unary_rpc_method_handler(
          servicer.Login,
          request_deserializer=sg__pb2.LoginRequest.FromString,
          response_serializer=sg__pb2.LoginResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'speechgrinder.sgapi.v1.Identity', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
