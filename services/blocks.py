from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import RowMapping

from repo.blocks import BlockRepository
from services.hash_gen import ShortUuidGenerator
from services.storage import Storage

@dataclass(frozen=True, slots=True)
class BlockData:
    """
        ---
    """

    text: str
    ttl: datetime
    views: int


class BlockService:
    """Бизнес-логика репозитория Block."""

    def __init__(self, repository: BlockRepository, storage: Storage,
                 short_uuid_gen: ShortUuidGenerator):
        self.repo = repository
        self.storage = storage
        self.short_uuid_gen = short_uuid_gen

    async def get_block(self, short_uuid: str) -> BlockData | None:

        uuid = await self.short_uuid_gen.get_uuid(short_uuid)
        block = await self.repo.get(uuid)
        if not block:
            return None
        block_data = await self.create_block_obj(block)
        await self.repo.add_one_view(uuid)

        return block_data

    async def create_block(self, text: str, ttl: datetime):
        """..."""

        uuid = await self.repo.create()
        short_uuid = await self.short_uuid_gen.get_short_id(uuid)

        obj_name = f'{short_uuid}.txt'
        result = await self.storage.upload(obj_name, text)

        if result:

            data = {
                'short_uuid': short_uuid,
                'object_name': obj_name,
                'ttl': ttl
            }
            await self.repo.update(uuid, data)
            return short_uuid

        else:

            await self.repo.remove(uuid)
            return None

    async def create_block_obj(self, block: RowMapping) -> BlockData:
        """Преобразует данные блока в объект BlockData."""

        object_name = block.get('object_name')
        text = await self.storage.get(object_name)

        block_data = BlockData(
            text=text,
            ttl=block.get('ttl', ''),
            views=block.get('views', 0)
        )

        return block_data





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


