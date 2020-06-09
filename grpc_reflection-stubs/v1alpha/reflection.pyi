from google.protobuf import descriptor_pool
from grpc import Server, ServicerContext
from grpc_reflection.v1alpha import reflection_pb2 as _reflection_pb2
from grpc_reflection.v1alpha._base import BaseReflectionServicer
from typing import Iterable, List, Optional

SERVICE_NAME: str

class ReflectionServicer(BaseReflectionServicer):
    def ServerReflectionInfo(self, request_iterator: Iterable[_reflection_pb2.ServerReflectionRequest], context: ServicerContext) -> None:
        ...

def enable_server_reflection(service_names: List[str], server: grpc.Server, pool: Optional[descriptor_pool.DescriptorPool] = ...) -> None:
    ...
