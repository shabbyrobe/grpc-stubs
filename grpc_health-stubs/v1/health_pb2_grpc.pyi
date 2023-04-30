from grpc import (
    Channel,
    Server,
    ServicerContext,
    UnaryStreamMultiCallable,
    UnaryUnaryMultiCallable,
)

from .health_pb2 import (
    HealthCheckRequest,
    HealthCheckResponse,
)

from typing import (
    Iterator,
)


class HealthStub:
    def __init__(self, channel: Channel) -> None: ...
    Check: UnaryUnaryMultiCallable[
        HealthCheckRequest,
        HealthCheckResponse]

    Watch: UnaryStreamMultiCallable[
        HealthCheckRequest,
        HealthCheckResponse]


class HealthServicer:
    def Check(self,
        request: HealthCheckRequest,
        context: ServicerContext,
    ) -> HealthCheckResponse: ...

    def Watch(self,
        request: HealthCheckRequest,
        context: ServicerContext,
    ) -> Iterator[HealthCheckResponse]: ...


def add_HealthServicer_to_server(servicer: HealthServicer, server: Server) -> None: ...
