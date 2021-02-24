import asyncio
import grpc
from . import _base_call, _base_channel
from ._call import (
    StreamStreamCall as StreamStreamCall,
    StreamUnaryCall as StreamUnaryCall,
    UnaryStreamCall as UnaryStreamCall,
    UnaryUnaryCall as UnaryUnaryCall
)
from ._interceptor import (
    ClientInterceptor as ClientInterceptor,
    InterceptedStreamStreamCall as InterceptedStreamStreamCall,
    InterceptedStreamUnaryCall as InterceptedStreamUnaryCall,
    InterceptedUnaryStreamCall as InterceptedUnaryStreamCall,
    InterceptedUnaryUnaryCall as InterceptedUnaryUnaryCall,
    StreamStreamClientInterceptor as StreamStreamClientInterceptor,
    StreamUnaryClientInterceptor as StreamUnaryClientInterceptor,
    UnaryStreamClientInterceptor as UnaryStreamClientInterceptor,
    UnaryUnaryClientInterceptor as UnaryUnaryClientInterceptor
)
from ._metadata import Metadata as Metadata
from ._typing import (
    ChannelArgumentType as ChannelArgumentType,
    DeserializingFunction as DeserializingFunction,
    RequestIterableType as RequestIterableType,
    SerializingFunction as SerializingFunction
)
from grpc._cython import cygrpc as cygrpc
from typing import Any, Optional, Sequence

class _BaseMultiCallable:
    def __init__(
        self,
        channel: cygrpc.AioChannel,
        method: bytes,
        request_serializer: SerializingFunction,
        response_deserializer: DeserializingFunction,
        interceptors: Optional[Sequence[ClientInterceptor]],
        loop: asyncio.AbstractEventLoop
    ) -> None: ...


class UnaryUnaryMultiCallable(_BaseMultiCallable,
                              _base_channel.UnaryUnaryMultiCallable):
    def __call__(
        self,
        request: Any, *,
        timeout: Optional[float]=...,
        metadata: Optional[Metadata]=...,
        credentials: Optional[grpc.CallCredentials]=...,
        wait_for_ready: Optional[bool]=...,
        compression: Optional[grpc.Compression]=...
    ) -> _base_call.UnaryUnaryCall: ...


class UnaryStreamMultiCallable(_BaseMultiCallable,
                               _base_channel.UnaryStreamMultiCallable):
    def __call__(
        self,
        request: Any,
        *,
        timeout: Optional[float]=...,
        metadata: Optional[Metadata]=...,
        credentials: Optional[grpc.CallCredentials]=...,
        wait_for_ready: Optional[bool]=...,
        compression: Optional[grpc.Compression]=...
    ) -> _base_call.UnaryStreamCall: ...


class StreamUnaryMultiCallable(_BaseMultiCallable,
                               _base_channel.StreamUnaryMultiCallable):
    def __call__(
        self,
        request_iterator: Optional[RequestIterableType]=...,
        timeout: Optional[float]=...,
        metadata: Optional[Metadata]=...,
        credentials: Optional[grpc.CallCredentials]=...,
        wait_for_ready: Optional[bool]=...,
        compression: Optional[grpc.Compression]=...
    ) -> _base_call.StreamUnaryCall: ...


class StreamStreamMultiCallable(_BaseMultiCallable,
                                _base_channel.StreamStreamMultiCallable):
    def __call__(
        self,
        request_iterator: Optional[RequestIterableType]=...,
        timeout: Optional[float]=...,
        metadata: Optional[Metadata]=...,
        credentials: Optional[grpc.CallCredentials]=...,
        wait_for_ready: Optional[bool]=...,
        compression: Optional[grpc.Compression]=...
    ) -> _base_call.StreamStreamCall: ...


class Channel(_base_channel.Channel):
    def __init__(
        self,
        target: str,
        options: ChannelArgumentType,
        credentials: Optional[grpc.ChannelCredentials],
        compression: Optional[grpc.Compression],
        interceptors: Optional[Sequence[ClientInterceptor]]
    ) -> None: ...

    async def __aenter__(self): ...

    async def __aexit__(
        self,
        exc_type: Any,
        exc_val: Any,
        exc_tb: Any
    ) -> None: ...

    async def close(self, grace: Optional[float]=...) -> Any: ...

    def get_state(self, try_to_connect: bool=...) -> grpc.ChannelConnectivity: ...

    async def wait_for_state_change(
        self,
        last_observed_state: grpc.ChannelConnectivity
    ) -> None: ...

    async def channel_ready(self) -> None: ...

    def unary_unary(
        self,
        method: str,
        request_serializer: Optional[SerializingFunction]=...,
        response_deserializer: Optional[DeserializingFunction]=...
    ) -> UnaryUnaryMultiCallable: ...

    def unary_stream(
        self,
        method: str,
        request_serializer: Optional[SerializingFunction]=...,
        response_deserializer: Optional[DeserializingFunction]=...
    ) -> UnaryStreamMultiCallable: ...

    def stream_unary(
        self,
        method: str,
        request_serializer: Optional[SerializingFunction]=...,
        response_deserializer: Optional[DeserializingFunction]=...
    ) -> StreamUnaryMultiCallable: ...

    def stream_stream(
        self,
        method: str,
        request_serializer: Optional[SerializingFunction]=...,
        response_deserializer: Optional[DeserializingFunction]=...
    ) -> StreamStreamMultiCallable: ...


def insecure_channel(
    target: str,
    options: Optional[ChannelArgumentType]=...,
    compression: Optional[grpc.Compression]=...,
    interceptors: Optional[Sequence[ClientInterceptor]]=...
) -> Any: ...


def secure_channel(
    target: str,
    credentials: grpc.ChannelCredentials,
    options: Optional[ChannelArgumentType]=...,
    compression: Optional[grpc.Compression]=...,
    interceptors: Optional[Sequence[ClientInterceptor]]=...
) -> Any: ...
