import os
import wave
import time
import sys

import grpc

from sg_pb2 import SluRequest, SluConfig, SluEvent, LoginRequest
from sg_pb2_grpc import IdentityStub as IdentityService
from sg_pb2_grpc import SluStub as SLUService


chunk_size = 8000

sample_rate_hertz=16000


if 'APP_ID' not in os.environ:
    raise RuntimeError('APP_ID environment variable needs to be set')

if len(sys.argv) > 1:
    FILE_NAME = sys.argv[1]
else: 
    FILE_NAME = '../audio.wav'

def audio_iterator():
    yield SluRequest(config=SluConfig(channels=1, sample_rate_hertz=sample_rate_hertz))
    yield SluRequest(event=SluEvent(event='START'))
    with wave.open(FILE_NAME, mode='r') as audio_file:
        audio_bytes = audio_file.readframes(chunk_size)

        while audio_bytes:

            yield SluRequest(audio=audio_bytes)
            audio_bytes = audio_file.readframes(chunk_size)
            time.sleep(float(chunk_size) / sample_rate_hertz)

    yield SluRequest(event=SluEvent(event='STOP'))




with grpc.secure_channel('api.speechgrinder.com', grpc.ssl_channel_credentials()) as channel:
    token = IdentityService(channel)\
        .Login(LoginRequest(device_id='python-simple-test', app_id=os.environ['APP_ID']))\
        .token

with grpc.secure_channel('api.speechgrinder.com', grpc.ssl_channel_credentials()) as channel:
    slu = SLUService(channel)
    responses = slu.Stream(
        audio_iterator(),
        None,
        [('authorization', 'Bearer {}'.format(token))])
    for response in responses:
        print(response)
