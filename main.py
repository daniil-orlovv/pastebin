import asyncio
import logging
from logging.config import dictConfig

import uvicorn
from fastapi import FastAPI
from api.app import init_api
from logs.settings.logging_settings import logging_config

from config import Config, load_config
from db.manager import DBManager
from repo.blocks import BlockRepository
from services.blocks import BlockService
from services.hash_gen import ShortUuidGenerator
from services.scheduler.manager import SchedulerManager
from services.storage import Storage

dictConfig(logging_config)
logger = logging.getLogger(__name__)


async def start_server(app: FastAPI, config: Config) -> None:
    """Запускает ASGI-сервер."""

    config_api = uvicorn.Config(
        app=app,
        host=config.asgi.host,
        port=config.asgi.port,
        reload=config.asgi.reload,
    )

    server = uvicorn.Server(config_api)

    logger.info('Запуск ASGI-сервера...')
    await server.serve()


async def main():

    try:

        config = load_config()
        db_manager = DBManager(config)
        session_maker = await db_manager.initialize()

        access_data_storage = {
            'host': config.storage.host,
            'port': config.storage.port,
            'login': config.storage.login,
            'pswd': config.storage.pswd
        }
        bucket_name = config.storage.bucket_name
        storage = Storage(access_data_storage, bucket_name)
        hash_gen = ShortUuidGenerator()

        repo = BlockRepository(session_maker)
        service = BlockService(repo, storage, hash_gen)

        scheduler = SchedulerManager(session_maker, config, service)
        await scheduler.add_job_rm_object()
        await scheduler.start()

        app = await init_api(service)
        await start_server(app, config)

    except Exception:
        logger.exception('Ошибка при запуске приложения:')

if __name__ == "__main__":

    asyncio.run(main())
