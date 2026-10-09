import logging
from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

T = TypeVar('T')


class BaseRepository(Generic[T]):
    model: type[T]

    def __init__(self, session_maker: async_sessionmaker[AsyncSession]):
        self.db_session_maker = session_maker
        self.logger = logging.getLogger(__name__)
