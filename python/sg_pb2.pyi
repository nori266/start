# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class SluRequest(google___protobuf___message___Message):
    audio = ... # type: bytes

    @property
    def config(self) -> SluConfig: ...

    @property
    def event(self) -> SluEvent: ...

    def __init__(self,
        config : typing___Optional[SluConfig] = None,
        event : typing___Optional[SluEvent] = None,
        audio : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SluRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"audio",u"config",u"event",u"streaming_request"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"audio",u"config",u"event",u"streaming_request"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"audio",b"audio",u"config",b"config",u"event",b"event",u"streaming_request",b"streaming_request"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"audio",b"config",b"event",b"streaming_request"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"streaming_request",b"streaming_request"]) -> typing_extensions___Literal["config","event","audio"]: ...

class SluConfig(google___protobuf___message___Message):
    class Encoding(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> SluConfig.Encoding: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[SluConfig.Encoding]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, SluConfig.Encoding]]: ...
    LINEAR16 = typing___cast(Encoding, 0)

    encoding = ... # type: SluConfig.Encoding
    channels = ... # type: int
    sample_rate_hertz = ... # type: int
    language_code = ... # type: typing___Text

    def __init__(self,
        encoding : typing___Optional[SluConfig.Encoding] = None,
        channels : typing___Optional[int] = None,
        sample_rate_hertz : typing___Optional[int] = None,
        language_code : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SluConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"channels",u"encoding",u"language_code",u"sample_rate_hertz"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"channels",b"encoding",b"language_code",b"sample_rate_hertz"]) -> None: ...

class SluEvent(google___protobuf___message___Message):
    class Event(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> SluEvent.Event: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[SluEvent.Event]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, SluEvent.Event]]: ...
    START = typing___cast(Event, 0)
    STOP = typing___cast(Event, 1)

    event = ... # type: SluEvent.Event

    def __init__(self,
        event : typing___Optional[SluEvent.Event] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SluEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"event"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"event"]) -> None: ...

class SluResponse(google___protobuf___message___Message):

    @property
    def started(self) -> SluStarted: ...

    @property
    def utterance(self) -> Utterance: ...

    @property
    def finished(self) -> SluFinished: ...

    def __init__(self,
        started : typing___Optional[SluStarted] = None,
        utterance : typing___Optional[Utterance] = None,
        finished : typing___Optional[SluFinished] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SluResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"finished",u"started",u"streaming_response",u"utterance"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"finished",u"started",u"streaming_response",u"utterance"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"finished",b"finished",u"started",b"started",u"streaming_response",b"streaming_response",u"utterance",b"utterance"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"finished",b"started",b"streaming_response",b"utterance"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"streaming_response",b"streaming_response"]) -> typing_extensions___Literal["started","utterance","finished"]: ...

class SluStarted(google___protobuf___message___Message):
    utterance_id = ... # type: typing___Text

    def __init__(self,
        utterance_id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SluStarted: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"utterance_id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"utterance_id"]) -> None: ...

class SluFinished(google___protobuf___message___Message):
    utterance_id = ... # type: typing___Text

    @property
    def error(self) -> SluError: ...

    def __init__(self,
        utterance_id : typing___Optional[typing___Text] = None,
        error : typing___Optional[SluError] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SluFinished: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",u"utterance_id"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"error",b"error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"error",b"utterance_id"]) -> None: ...

class SluError(google___protobuf___message___Message):
    code = ... # type: typing___Text
    message = ... # type: typing___Text

    def __init__(self,
        code : typing___Optional[typing___Text] = None,
        message : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SluError: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"message"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"message"]) -> None: ...

class Utterance(google___protobuf___message___Message):
    utterance_id = ... # type: typing___Text
    type = ... # type: typing___Text
    language_code = ... # type: typing___Text

    @property
    def alternatives(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Alternative]: ...

    def __init__(self,
        utterance_id : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        language_code : typing___Optional[typing___Text] = None,
        alternatives : typing___Optional[typing___Iterable[Alternative]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Utterance: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"alternatives",u"language_code",u"type",u"utterance_id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"alternatives",b"language_code",b"type",b"utterance_id"]) -> None: ...

class Alternative(google___protobuf___message___Message):
    confidence = ... # type: float

    @property
    def tokens(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Token]: ...

    def __init__(self,
        confidence : typing___Optional[float] = None,
        tokens : typing___Optional[typing___Iterable[Token]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Alternative: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"confidence",u"tokens"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"confidence",b"tokens"]) -> None: ...

class Token(google___protobuf___message___Message):
    class TokenPosition(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> Token.TokenPosition: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[Token.TokenPosition]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, Token.TokenPosition]]: ...
    outsideOf = typing___cast(TokenPosition, 0)
    startOf = typing___cast(TokenPosition, 1)
    insideOf = typing___cast(TokenPosition, 2)

    text = ... # type: typing___Text
    text_with_trailing_space = ... # type: typing___Text
    lemma = ... # type: typing___Text
    pos = ... # type: typing___Text
    tag = ... # type: typing___Text
    case = ... # type: typing___Text
    number = ... # type: typing___Text
    entity_type = ... # type: typing___Text
    position_in_entity = ... # type: Token.TokenPosition
    is_segment_start = ... # type: bool
    trailing_silence = ... # type: int

    def __init__(self,
        text : typing___Optional[typing___Text] = None,
        text_with_trailing_space : typing___Optional[typing___Text] = None,
        lemma : typing___Optional[typing___Text] = None,
        pos : typing___Optional[typing___Text] = None,
        tag : typing___Optional[typing___Text] = None,
        case : typing___Optional[typing___Text] = None,
        number : typing___Optional[typing___Text] = None,
        entity_type : typing___Optional[typing___Text] = None,
        position_in_entity : typing___Optional[Token.TokenPosition] = None,
        is_segment_start : typing___Optional[bool] = None,
        trailing_silence : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Token: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"case",u"entity_type",u"is_segment_start",u"lemma",u"number",u"pos",u"position_in_entity",u"tag",u"text",u"text_with_trailing_space",u"trailing_silence"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"case",b"entity_type",b"is_segment_start",b"lemma",b"number",b"pos",b"position_in_entity",b"tag",b"text",b"text_with_trailing_space",b"trailing_silence"]) -> None: ...

class LoginRequest(google___protobuf___message___Message):
    device_id = ... # type: typing___Text
    app_id = ... # type: typing___Text

    def __init__(self,
        device_id : typing___Optional[typing___Text] = None,
        app_id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LoginRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"app_id",u"device_id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"app_id",b"device_id"]) -> None: ...

class LoginResponse(google___protobuf___message___Message):
    token = ... # type: typing___Text

    def __init__(self,
        token : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LoginResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"token"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"token"]) -> None: ...
