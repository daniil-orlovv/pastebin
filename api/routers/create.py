import logging

from fastapi import APIRouter, Request

from services.blocks import BlockService


class CreateRouter:
    """Класс для управлением роутера для эндпоинта '/api/create'."""

    def __init__(
        self,
        service: BlockService
    ):
        self.router = APIRouter(prefix="/blocks", tags=["results"])
        self._setup_routes()
        self.logger = logging.getLogger(__name__)
        self.service = service

    def _setup_routes(self):
        """Устанавливает роутер для эндпоинта '/create'."""

        @self.router.post("/create")
        async def create_block(request: Request):
            """Обрабатывает запросы, приходящие на эндпоинт /create."""
            data = await request.json()
            print(data)

            hash_id = await self.service.create_block(
                data['text'],
                data['ttl'])
            return {'hash_id': hash_id}


    async def _handle_result(self, data: dict) -> list:
        """Обрабатывает запрос на эндпоинт."""

        ...

    def get_router(self) -> APIRouter:
        """Получает и возвращает роутер."""

        return self.router
