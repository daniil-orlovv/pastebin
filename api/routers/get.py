import logging

from fastapi import APIRouter, Request

from services.blocks import BlockService


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

            block = await self.service.get_block(short_uuid)
            return {'block': block}


    async def _handle_result(self, data: dict) -> list:
        """Обрабатывает запрос на эндпоинт."""

        ...

    def get_router(self) -> APIRouter:
        """Получает и возвращает роутер."""

        return self.router
