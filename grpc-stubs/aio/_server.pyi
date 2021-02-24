import grpc
from . import _base_server
from ._interceptor import ServerInterceptor as ServerInterceptor
from ._typing import ChannelArgumentType as ChannelArgumentType
from concurrent.futures import Executor
from grpc._cython import cygrpc as cygrpc
from typing import Any, Optional, Sequence


class Server(_base_server.Server):
    def __init__(
        self,
        thread_pool: Optional[Executor],
        generic_handlers: Optional[Sequence[grpc.GenericRpcHandler]],
        interceptors: Optional[Sequence[Any]],
        options: ChannelArgumentType,
        maximum_concurrent_rpcs: Optional[int],
        compression: Optional[grpc.Compression]
    ) -> None: ...

    def add_generic_rpc_handlers(
        self,
        generic_rpc_handlers: Sequence[grpc.GenericRpcHandler]
    ) -> None: ...

    def add_insecure_port(self, address: str) -> int: ...

    def add_secure_port(
        self,
        address: str,
        server_credentials: grpc.ServerCredentials
    ) -> int: ...

    async def start(self) -> None: ...

    async def stop(self, grace: Optional[float]) -> None: ...

    async def wait_for_termination(self, timeout: Optional[float]=...) -> bool: ...

    def __del__(self) -> None: ...


def server(
    migration_thread_pool: Optional[Executor]=...,
    handlers: Optional[Sequence[grpc.GenericRpcHandler]]=...,
    interceptors: Optional[Sequence[Any]]=...,
    options: Optional[ChannelArgumentType]=...,
    maximum_concurrent_rpcs: Optional[int]=...,
    compression: Optional[grpc.Compression]=...
) -> Any: ...
