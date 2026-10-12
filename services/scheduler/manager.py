import logging

from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler_di import ContextSchedulerDecorator
from sqlalchemy.ext.asyncio import async_sessionmaker

from config import Config
from services.blocks import BlockService
from services.scheduler.jobs import remove_expired_blocks_job


class SchedulerManager:
    def __init__(
        self,
        session_maker_db: async_sessionmaker,
        config: Config,
        block_service: BlockService
    ):
        self.logger = logging.getLogger(__name__)
        self.session_maker_db = session_maker_db
        self.block_service = block_service
        self.logger = logging.getLogger(__name__)

        try:
            redis_host = config.redis_config.host
            redis_port = config.redis_config.port
            redis_db = config.redis_config.db

            jobstore = RedisJobStore(
                host=redis_host,
                port=redis_port,
                db=redis_db
            )

            jobstores = {
                "default": jobstore
            }

            self.scheduler = ContextSchedulerDecorator(
                AsyncIOScheduler(
                    jobstores=jobstores,
                    job_defaults={
                        "misfire_grace_time": 600,
                        "coalesce": True,
                        "max_instances": 1,
                    },
                )
            )

            self.scheduler.ctx.add_instance(
                session_maker_db, async_sessionmaker)
            self.scheduler.ctx.add_instance(
                self.scheduler, ContextSchedulerDecorator)
            self.scheduler.ctx.add_instance(config, Config)
            self.scheduler.ctx.add_instance(jobstore, RedisJobStore)
            self.scheduler.ctx.add_instance(block_service, BlockService)

        except Exception:
            self.logger.exception('Ошибка при инициализации менеджера для '
                                  'планировщика:')
            raise

    async def start(self) -> None:
        """Запуск планировщика."""

        try:
            self.scheduler.start()
        except Exception:
            self.logger.exception('Ошибка при запуске планировщика:')

    async def add_job_rm_object(self):

        try:

            job_id = 'rm_objects_minio'
            self.scheduler.add_job(
                remove_expired_blocks_job,
                trigger='interval',
                minutes=2,
                id=job_id,
                replace_existing=True,
            )

        except Exception:
            self.logger.exception(
                'Ошибка при добавлении задачи на отправку сообщений с '
                'напоминаниями о приемах, запланированных через 7 дней:')
