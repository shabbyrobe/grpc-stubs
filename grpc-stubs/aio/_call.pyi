import asyncio
import enum
import grpc
from . import _base_call
from ._metadata import Metadata
from ._typing import (
    DeserializingFunction,
    DoneCallbackType,
    RequestIterableType,
    RequestType,
    ResponseType,
    SerializingFunction
)
from grpc._cython import cygrpc
from typing import AsyncIterable, Optional

class AioRpcError(grpc.RpcError):
    def __init__(
        self,
        code: grpc.StatusCode,
        initial_metadata: Metadata,
        trailing_metadata: Metadata,
        details: Optional[str]=...,
        debug_error_string: Optional[str]=...
    ) -> None: ...

    def code(self) -> grpc.StatusCode: ...

    def details(self) -> Optional[str]: ...

    def initial_metadata(self) -> Metadata: ...

    def trailing_metadata(self) -> Metadata: ...

    def debug_error_string(self) -> str: ...


class Call:
    def __init__(
        self,
        cython_call: cygrpc._AioCall,
        metadata: Metadata,
        request_serializer: SerializingFunction,
        response_deserializer: DeserializingFunction,
        loop: asyncio.AbstractEventLoop
    ) -> None: ...

    def __del__(self) -> None: ...

    def cancelled(self) -> bool: ...

    def cancel(self) -> bool: ...

    def done(self) -> bool: ...

    def add_done_callback(self, callback: DoneCallbackType) -> None: ...

    def time_remaining(self) -> Optional[float]: ...

    async def initial_metadata(self) -> Metadata: ...

    async def trailing_metadata(self) -> Metadata: ...

    async def code(self) -> grpc.StatusCode: ...

    async def details(self) -> str: ...

    async def debug_error_string(self) -> str: ...


class _APIStyle(enum.IntEnum):
    UNKNOWN: int = ...
    ASYNC_GENERATOR: int = ...
    READER_WRITER: int = ...


class _UnaryResponseMixin(Call):
    def cancel(self) -> bool: ...

    def __await__(self) -> ResponseType: ...


class _StreamResponseMixin(Call):
    def cancel(self) -> bool: ...

    def __aiter__(self) -> AsyncIterable[ResponseType]: ...

    async def read(self) -> ResponseType: ...


class _StreamRequestMixin(Call):
    def cancel(self) -> bool: ...

    async def write(self, request: RequestType) -> None: ...

    async def done_writing(self) -> None: ...

    async def wait_for_connection(self) -> None: ...


class UnaryUnaryCall(_UnaryResponseMixin, Call, _base_call.UnaryUnaryCall):
    def __init__(
        self,
        request: RequestType,
        deadline: Optional[float],
        metadata: Metadata,
        credentials: Optional[grpc.CallCredentials],
        wait_for_ready: Optional[bool],
        channel: cygrpc.AioChannel,
        method: bytes,
        request_serializer: SerializingFunction,
        response_deserializer: DeserializingFunction,
        loop: asyncio.AbstractEventLoop
    ) -> None: ...

    async def wait_for_connection(self) -> None: ...


class UnaryStreamCall(_StreamResponseMixin, Call, _base_call.UnaryStreamCall):
    def __init__(
        self,
        request: RequestType,
        deadline: Optional[float],
        metadata: Metadata,
        credentials: Optional[grpc.CallCredentials],
        wait_for_ready: Optional[bool],
        channel: cygrpc.AioChannel,
        method: bytes,
        request_serializer: SerializingFunction,
        response_deserializer: DeserializingFunction,
        loop: asyncio.AbstractEventLoop
    ) -> None: ...

    async def wait_for_connection(self) -> None: ...


class StreamUnaryCall(_StreamRequestMixin, _UnaryResponseMixin, Call, _base_call.StreamUnaryCall):
    def __init__(
        self,
        request_iterator: Optional[RequestIterableType],
        deadline: Optional[float],
        metadata: Metadata,
        credentials: Optional[grpc.CallCredentials],
        wait_for_ready: Optional[bool],
        channel: cygrpc.AioChannel,
        method: bytes,
        request_serializer: SerializingFunction,
        response_deserializer: DeserializingFunction,
        loop: asyncio.AbstractEventLoop
    ) -> None: ...


class StreamStreamCall(_StreamRequestMixin, _StreamResponseMixin, Call, _base_call.StreamStreamCall):
    def __init__(
        self,
        request_iterator: Optional[RequestIterableType],
        deadline: Optional[float],
        metadata: Metadata,
        credentials: Optional[grpc.CallCredentials],
        wait_for_ready: Optional[bool],
        channel: cygrpc.AioChannel,
        method: bytes,
        request_serializer: SerializingFunction,
        response_deserializer: DeserializingFunction,
        loop: asyncio.AbstractEventLoop
    ) -> None: ...
