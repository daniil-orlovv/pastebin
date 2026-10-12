import io
import traceback

from minio import Minio
from minio.commonconfig import Tags


class Storage:

    def __init__(self, access_data: dict, bucket_name: str) -> None:

        host = access_data.get('host')
        port = access_data.get('port')
        host_port = f'{host}:{port}'
        login = access_data.get('login')
        pswd = access_data.get('pswd')

        self.client = Minio(
            endpoint=host_port,
            access_key=login,
            secret_key=pswd,
            secure=False
        )

        self.bucket_name = bucket_name


    async def upload(self, object_name: str, text: str) -> str:

        file_data = io.BytesIO(text.encode('utf-8'))

        tags = Tags.new_object_tags()
        tags["ttl"] = "3day"

        result = self.client.put_object(
            self.bucket_name,
            object_name,
            file_data,
            length=len(text.encode('utf-8')),
            content_type='text/plain; charset=utf-8',
            tags=tags
        )
        return result.object_name

    async def get(self, object_name: str):

        self.client.get_object(
            self.bucket_name,
            object_name
        )

    async def remove(self, object_name):
        try:
            self.client.remove_object(self.bucket_name, object_name)
        except Exception:
            traceback.print_exc()
