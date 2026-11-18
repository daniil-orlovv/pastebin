import logging
import re

from fastapi import APIRouter, HTTPException, status

from services.blocks import BlockService

SHORT_UUID_RE = re.compile(r'^[2-9A-HJ-NP-Za-km-z]{22}$')

class GetRouter:
    """Класс для управлением роутера для эндпоинта '/api/get'."""

    def __init__(
        self,
        service: BlockService
    ):
        self.router = APIRouter(prefix="/blocks", tags=["results"])
        self._setup_routes()
        self.logger = logging.getLogger(__name__)
        self.service = service

    def _setup_routes(self):
        """Устанавливает роутер для эндпоинта '/get'."""

        @self.router.post("/get/{short_uuid}")
        async def get_block(short_uuid: str):
            """Обрабатывает запросы, приходящие на эндпоинт /get."""

            if not SHORT_UUID_RE.fullmatch(short_uuid):
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail='Введите корректный uuid',
                )

            block = await self.service.get_block(short_uuid)
            if not block:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Блок не найден',
                )
            return {
                'text': block.text,
                'ttl': block.ttl.strftime('%d.%m.%Y %H:%M'),
                'views': block.views
            }


    async def _handle_result(self, data: dict) -> list:
        """Обрабатывает запрос на эндпоинт."""

        ...

    def get_router(self) -> APIRouter:
        """Получает и возвращает роутер."""

        return self.router
