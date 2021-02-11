import asyncio
import grpc
from . import _base_call
from ._call import (
    AioRpcError as AioRpcError,
    StreamStreamCall as StreamStreamCall,
    StreamUnaryCall as StreamUnaryCall,
    UnaryStreamCall as UnaryStreamCall,
    UnaryUnaryCall as UnaryUnaryCall
)
from ._metadata import Metadata as Metadata
from ._typing import (
    DeserializingFunction as DeserializingFunction,
    DoneCallbackType as DoneCallbackType,
    RequestIterableType as RequestIterableType,
    RequestType as RequestType,
    ResponseIterableType as ResponseIterableType,
    ResponseType as ResponseType,
    SerializingFunction as SerializingFunction
)
from abc import ABCMeta, abstractmethod
from grpc._cython import cygrpc as cygrpc
from typing import (
    Any,
    AsyncIterable,
    Awaitable,
    Callable,
    Optional,
    Sequence,
    Union
)


class ServerInterceptor(metaclass=ABCMeta):
    @abstractmethod
    async def intercept_service(
        self,
        continuation: Callable[[grpc.HandlerCallDetails], Awaitable[grpc.RpcMethodHandler]],
        handler_call_details: grpc.HandlerCallDetails
    ) -> grpc.RpcMethodHandler: ...


class ClientCallDetails(grpc.ClientCallDetails):
    method: str
    timeout: Optional[float]
    metadata: Optional[Metadata]
    credentials: Optional[grpc.CallCredentials]
    wait_for_ready: Optional[bool]


class ClientInterceptor(metaclass=ABCMeta): ...


class UnaryUnaryClientInterceptor(ClientInterceptor, metaclass=ABCMeta):
    @abstractmethod
    async def intercept_unary_unary(
        self,
        continuation: Callable[[ClientCallDetails, RequestType], UnaryUnaryCall],
        client_call_details: ClientCallDetails,
        request: RequestType
    ) -> Union[UnaryUnaryCall, ResponseType]: ...


class UnaryStreamClientInterceptor(ClientInterceptor, metaclass=ABCMeta):
    @abstractmethod
    async def intercept_unary_stream(
        self,
        continuation: Callable[[ClientCallDetails, RequestType], UnaryStreamCall],
        client_call_details: ClientCallDetails,
        request: RequestType
    ) -> Union[ResponseIterableType, UnaryStreamCall]: ...


class StreamUnaryClientInterceptor(ClientInterceptor, metaclass=ABCMeta):
    @abstractmethod
    async def intercept_stream_unary(
        self,
        continuation: Callable[[ClientCallDetails, RequestType], UnaryStreamCall],
        client_call_details: ClientCallDetails,
        request_iterator: RequestIterableType
    ) -> StreamUnaryCall: ...


class StreamStreamClientInterceptor(ClientInterceptor, metaclass=ABCMeta):
    @abstractmethod
    async def intercept_stream_stream(
        self,
        continuation: Callable[[ClientCallDetails, RequestType], UnaryStreamCall],
        client_call_details: ClientCallDetails,
        request_iterator: RequestIterableType
    ) -> Union[ResponseIterableType, StreamStreamCall]: ...


class InterceptedCall:
    def __init__(self, interceptors_task: asyncio.Task) -> None: ...

    def __del__(self) -> None: ...

    def cancel(self) -> bool: ...

    def cancelled(self) -> bool: ...

    def done(self) -> bool: ...

    def add_done_callback(self, callback: DoneCallbackType) -> None: ...

    def time_remaining(self) -> Optional[float]: ...

    async def initial_metadata(self) -> Optional[Metadata]: ...

    async def trailing_metadata(self) -> Optional[Metadata]: ...

    async def code(self) -> grpc.StatusCode: ...

    async def details(self) -> str: ...

    async def debug_error_string(self) -> Optional[str]: ...

    async def wait_for_connection(self) -> None: ...


class _InterceptedUnaryResponseMixin:
    def __await__(self): ...


class _InterceptedStreamResponseMixin:
    def __aiter__(self) -> AsyncIterable[ResponseType]: ...

    async def read(self) -> ResponseType: ...


class _InterceptedStreamRequestMixin:
    async def write(self, request: RequestType) -> None: ...

    async def done_writing(self) -> None: ...


class InterceptedUnaryUnaryCall(_InterceptedUnaryResponseMixin,
                                InterceptedCall,
                                _base_call.UnaryUnaryCall):
    def __init__(
        self,
        interceptors: Sequence[UnaryUnaryClientInterceptor],
        request: RequestType,
        timeout: Optional[float],
        metadata: Metadata,
        credentials: Optional[grpc.CallCredentials],
        wait_for_ready: Optional[bool],
        channel: cygrpc.AioChannel,
        method: bytes,
        request_serializer: SerializingFunction,
        response_deserializer: DeserializingFunction,
        loop: asyncio.AbstractEventLoop
    ) -> None: ...

    def time_remaining(self) -> Optional[float]: ...


class InterceptedUnaryStreamCall(_InterceptedStreamResponseMixin,
                                 InterceptedCall,
                                 _base_call.UnaryStreamCall):
    def __init__(
        self,
        interceptors: Sequence[UnaryStreamClientInterceptor],
        request: RequestType,
        timeout: Optional[float],
        metadata: Metadata,
        credentials: Optional[grpc.CallCredentials],
        wait_for_ready: Optional[bool],
        channel: cygrpc.AioChannel,
        method: bytes,
        request_serializer: SerializingFunction,
        response_deserializer: DeserializingFunction,
        loop: asyncio.AbstractEventLoop
    ) -> None: ...

    def time_remaining(self) -> Optional[float]: ...


class InterceptedStreamUnaryCall(_InterceptedUnaryResponseMixin,
                                 _InterceptedStreamRequestMixin,
                                 InterceptedCall,
                                 _base_call.StreamUnaryCall):
    def __init__(
        self,
        interceptors: Sequence[StreamUnaryClientInterceptor],
        request_iterator: Optional[RequestIterableType],
        timeout: Optional[float],
        metadata: Metadata,
        credentials: Optional[grpc.CallCredentials],
        wait_for_ready: Optional[bool],
        channel: cygrpc.AioChannel,
        method: bytes,
        request_serializer: SerializingFunction,
        response_deserializer: DeserializingFunction,
        loop: asyncio.AbstractEventLoop
    ) -> None: ...

    def time_remaining(self) -> Optional[float]: ...


class InterceptedStreamStreamCall(_InterceptedStreamResponseMixin,
                                  _InterceptedStreamRequestMixin,
                                  InterceptedCall,
                                  _base_call.StreamStreamCall):
    def __init__(
        self,
        interceptors: Sequence[StreamStreamClientInterceptor],
        request_iterator: Optional[RequestIterableType],
        timeout: Optional[float],
        metadata: Metadata,
        credentials: Optional[grpc.CallCredentials],
        wait_for_ready: Optional[bool],
        channel: cygrpc.AioChannel,
        method: bytes,
        request_serializer: SerializingFunction,
        response_deserializer: DeserializingFunction, 
        loop: asyncio.AbstractEventLoop
    ) -> None: ...

    def time_remaining(self) -> Optional[float]: ...


class UnaryUnaryCallResponse(_base_call.UnaryUnaryCall):
    def __init__(self, response: ResponseType) -> None: ...

    def cancel(self) -> bool: ...

    def cancelled(self) -> bool: ...

    def done(self) -> bool: ...

    def add_done_callback(self, unused_callback: Any) -> None: ...

    def time_remaining(self) -> Optional[float]: ...

    async def initial_metadata(self) -> Optional[Metadata]: ...

    async def trailing_metadata(self) -> Optional[Metadata]: ...

    async def code(self) -> grpc.StatusCode: ...

    async def details(self) -> str: ...

    async def debug_error_string(self) -> Optional[str]: ...

    def __await__(self): ...

    async def wait_for_connection(self) -> None: ...


class _StreamCallResponseIterator:
    def __init__(
        self,
        call: Union[_base_call.UnaryStreamCall, _base_call.StreamStreamCall],
        response_iterator: AsyncIterable[ResponseType]
    ) -> None: ...

    def cancel(self) -> bool: ...

    def cancelled(self) -> bool: ...

    def done(self) -> bool: ...

    def add_done_callback(self, callback: Any) -> None: ...

    def time_remaining(self) -> Optional[float]: ...

    async def initial_metadata(self) -> Optional[Metadata]: ...

    async def trailing_metadata(self) -> Optional[Metadata]: ...

    async def code(self) -> grpc.StatusCode: ...

    async def details(self) -> str: ...

    async def debug_error_string(self) -> Optional[str]: ...

    def __aiter__(self): ...

    async def wait_for_connection(self) -> None: ...


class UnaryStreamCallResponseIterator(_StreamCallResponseIterator,
                                      _base_call.UnaryStreamCall):
    async def read(self) -> ResponseType: ...


class StreamStreamCallResponseIterator(_StreamCallResponseIterator,
                                       _base_call.StreamStreamCall):
    async def read(self) -> ResponseType: ...

    async def write(self, request: RequestType) -> None: ...

    async def done_writing(self) -> None: ...
