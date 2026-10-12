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
        result = await self.storage.upload(obj_name, text)

        if result:

            datetime_to_rm = datetime.now() + timedelta(days=3)
            data = {
                'short_uuid': short_uuid,
                'object_name': obj_name,
                'ttl': datetime_to_rm
            }
            await self.repo.update(uuid, data)
            return short_uuid

        else:

            await self.repo.remove(uuid)
            return None





    def change_block(self):
        ...

    def delete_block(self):
        ...

    async def remove_expired_blocks(self):

        list_blocks = await self.repo.get_blocks_with_expired_ttl()
        print(list_blocks)
        for block in list_blocks:
            await self.storage.remove(block)

        list_uuid_blocks = await self.repo.get_uuid_blocks_with_expired_ttl()
        print(list_uuid_blocks)
        for uuid_block in list_uuid_blocks:
            await self.repo.remove(uuid_block)


