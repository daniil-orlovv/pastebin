from datetime import datetime, timedelta

from repo.blocks import BlockRepository
from services.hash_gen import ShortUuidGenerator
from services.storage import Storage


class BlockService:
    """Бизнес-логика репозитория Block."""

    def __init__(self, repository: BlockRepository, storage: Storage,
                 short_uuid_gen: ShortUuidGenerator):
        self.repo = repository
        self.storage = storage
        self.short_uuid_gen = short_uuid_gen

    async def get_block(self, short_uuid: str):

        uuid = await self.short_uuid_gen.get_uuid(short_uuid)
        block = await self.repo.get(uuid)
        return block

    async def create_block(self, text, ttl):
        """..."""

        uuid = await self.repo.create()
        short_uuid = await self.short_uuid_gen.get_short_id(uuid)

        obj_name = f'{short_uuid}.txt'
        await self.storage.upload(obj_name, text)

        datetime_to_rm = datetime.now() + timedelta(days=3)
        data = {
            'short_uuid': short_uuid,
            'object_name': obj_name,
            'ttl': datetime_to_rm
        }
        await self.repo.update(uuid, data)

        return short_uuid



    def change_block(self):
        ...

    def delete_block(self):
        ...
