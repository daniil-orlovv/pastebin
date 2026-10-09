from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from config import Config


class DBManager:
    """Управление подключением к БД и session_maker'ами"""

    def __init__(self, config: Config) -> None:
        self._config = config
        self._engine = None
        self._session_maker_db = None

    async def initialize(self) -> async_sessionmaker[AsyncSession]:
        """Инициализирует фабрику сессий и возвращает ее."""

        self._engine = create_async_engine(self._config.db_url)
        self._session_maker_db = async_sessionmaker(
            self._engine, class_=AsyncSession, expire_on_commit=False)
        return self._session_maker_db
