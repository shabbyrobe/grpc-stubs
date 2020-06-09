from . import _async as aio
from grpc_reflection.v1alpha._base import BaseReflectionServicer
from typing import Any, Optional

SERVICE_NAME: Any

class ReflectionServicer(BaseReflectionServicer):
    def ServerReflectionInfo(self, request_iterator: Any, context: Any) -> None: ...

def enable_server_reflection(service_names: Any, server: Any, pool: Optional[Any] = ...) -> None: ...
