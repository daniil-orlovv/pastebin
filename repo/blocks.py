from uuid import UUID

from sqlalchemy import RowMapping, func, select, update

from db.models import Block
from repo.base import BaseRepository


class BlockRepository(BaseRepository[Block]):
    """Репозиторий для работы с моделью Block."""

    model = Block

    async def get(self, uuid: UUID) -> RowMapping | None:
        """Получает запись в формате словаря из таблицы blocks."""

        pass

        async with self.db_session_maker() as session:

            query = (
                select(
                    Block.uuid,
                    Block.short_uuid,
                    Block.object_name,
                    Block.created_at,
                    Block.updated_at,
                    Block.ttl
                    ).where(
                        Block.uuid == uuid))

            result = await session.execute(query)
            return result.mappings().first()

    async def create(self) -> ...:
        """..."""

        async with self.db_session_maker() as session:

            block = Block(
                short_uuid=None,
                object_name=None,
            )

            session.add(block)
            await session.commit()
            return block.uuid

    async def update(self, uuid: UUID, data: dict) -> ...:
        """..."""

        async with self.db_session_maker() as session:

            stmt = update(Block).where(Block.uuid == uuid).values(data)

            await session.execute(stmt)
            await session.commit()

    async def remove(self, uuid: UUID) -> bool:

        async with self.db_session_maker() as session:

            obj = await session.get(Block, uuid)
            if obj is None:
                return False

            await session.delete(obj)
            await session.commit()
            return True

    async def get_blocks_with_expired_ttl(self):

        async with self.db_session_maker() as session:

            query = (select(Block.object_name).where(
                Block.ttl >= func.current_date()))
            result = await session.execute(query)
            return result.scalars().all()

    async def get_uuid_blocks_with_expired_ttl(self):

        async with self.db_session_maker() as session:

            query = (select(Block.uuid).where(
                Block.ttl >= func.current_date()))
            result = await session.execute(query)
            return result.scalars().all()
