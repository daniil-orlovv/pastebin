import logging
from dataclasses import dataclass

from environs import Env

logger = logging.getLogger(__name__)


@dataclass
class ASGIConfig:
    """Параметры работы с ASGI-сервером."""

    host: str
    port: int
    reload: bool

@dataclass
class StorageConfig:
    """Параметры работы с Storage S3."""

    host: str
    port: int
    login: str
    pswd: str
    bucket_name: str

@dataclass
class RedisConfig:
    """Параметры работы с Storage S3."""

    host: str
    db: int
    port: str



@dataclass
class Config:
    """Общие параметры всего проекта."""

    db_url: str
    asgi: ASGIConfig
    storage: StorageConfig
    redis_config: RedisConfig


def load_config(path: str | None = None) -> Config:
    """Загружает конфигурацию из .env файла."""

    try:

        env = Env()
        env.read_env(path)

        config = Config(
            db_url=env('DB_URL'),
            asgi=ASGIConfig(
                host=str(env('HOST_ASGI_SERVER')),
                port=int(env('PORT_ASGI_SERVER')),
                reload=bool(env('RELOAD_ASGI_SERVER')),
            ),
            storage=StorageConfig(
                host=str(env('STORAGE_HOST')),
                port=int(env('STORAGE_PORT')),
                login=str(env('STORAGE_LOGIN')),
                pswd=str(env('STORAGE_PSWD')),
                bucket_name=str(env('BUCKET_NAME'))
            ),
            redis_config=RedisConfig(
                host=env('REDIS_HOST'),
                db=env('REDIS_DB'),
                port=env('REDIS_PORT'),
            )
        )

        logger.info('Конфиг загружен')
        return config

    except Exception:
        logger.exception('Ошибка при загрузке переменных окружения из .env:')
        raise
