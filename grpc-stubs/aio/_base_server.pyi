import abc
import grpc
from ._metadata import Metadata
from ._typing import RequestType, ResponseType
from typing import Iterable, Mapping, Optional, Sequence


class Server(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_generic_rpc_handlers(
        self,
        generic_rpc_handlers: Sequence[grpc.GenericRpcHandler]
    ) -> None: ...

    @abc.abstractmethod
    def add_insecure_port(self, address: str) -> int: ...

    @abc.abstractmethod
    def add_secure_port(
        self,
        address: str,
        server_credentials: grpc.ServerCredentials
    ) -> int: ...

    @abc.abstractmethod
    async def start(self) -> None: ...

    @abc.abstractmethod
    async def stop(self, grace: Optional[float]) -> None: ...

    @abc.abstractmethod
    async def wait_for_termination(
        self,
        timeout: Optional[float]=...
    ) -> bool: ...


class ServicerContext(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def read(self) -> RequestType: ...

    @abc.abstractmethod
    async def write(self, message: ResponseType) -> None: ...

    @abc.abstractmethod
    async def send_initial_metadata(self, initial_metadata: Metadata) -> None: ...

    @abc.abstractmethod
    async def abort(
        self,
        code: grpc.StatusCode,
        details: str=...,
        trailing_metadata: Metadata=...
    ) -> None: ...

    @abc.abstractmethod
    async def set_trailing_metadata(self, trailing_metadata: Metadata) -> None: ...

    @abc.abstractmethod
    def invocation_metadata(self) -> Optional[Metadata]: ...

    @abc.abstractmethod
    def set_code(self, code: grpc.StatusCode) -> None: ...

    @abc.abstractmethod
    def set_details(self, details: str) -> None: ...

    @abc.abstractmethod
    def set_compression(self, compression: grpc.Compression) -> None: ...

    @abc.abstractmethod
    def disable_next_message_compression(self) -> None: ...

    @abc.abstractmethod
    def peer(self) -> str: ...

    @abc.abstractmethod
    def peer_identities(self) -> Optional[Iterable[bytes]]: ...

    @abc.abstractmethod
    def peer_identity_key(self) -> Optional[str]: ...

    @abc.abstractmethod
    def auth_context(self) -> Mapping[str, Iterable[bytes]]: ...
