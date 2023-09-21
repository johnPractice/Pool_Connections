from minio import Minio
from interfaces.connection import Connection
from interfaces.pool_connection import PoolConnection


class MinioConnection(Connection):
    pass


class MinioPoolConnection(PoolConnection):
    pass


minio_connection = MinioConnection(
    config={
        "endpoint": "OBJECT_STORAGE_URL",
        "access_key": "OBJECT_STORAGE_ACCESS_KEY",
        "secret_key": "OBJECT_STORAGE_SECRET_KEY",
        "secure": True,
    },
    connection_obj=Minio,
)


minio_pool_connection = MinioPoolConnection(connection=minio_connection, pool_count=10)


for _ in range(20):
    connection = minio_pool_connection.get_connection()
    print(id(connection))
