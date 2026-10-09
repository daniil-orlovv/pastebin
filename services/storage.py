import io

from minio import Minio
from minio.commonconfig import Tags


class Storage:

    def __init__(self, access_data: dict, files_dir: str) -> None:

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

        self.files_dir = files_dir


    async def upload(self, object_name: str, text: str):

        file_data = io.BytesIO(text.encode('utf-8'))

        tags = Tags.new_object_tags()
        tags["ttl"] = "3day"

        self.client.put_object(
            self.files_dir,
            object_name,
            file_data,
            length=len(text.encode('utf-8')),
            content_type='text/plain; charset=utf-8',
            tags=tags
        )

    async def get(self, object_name: str):

        self.client.get_object(
            self.files_dir,
            object_name
        )

