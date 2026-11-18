from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers.create import CreateRouter
from api.routers.get import GetRouter
from services.blocks import BlockService


async def init_api(service: BlockService) -> FastAPI:
    """Инициализирует приложение API."""

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],   # адрес фронта
        allow_methods=["*"],
        allow_headers=["*"],
    )

    create_router_manager = CreateRouter(service)
    create_router = create_router_manager.get_router()

    get_router_manager = GetRouter(service)
    get_router = get_router_manager.get_router()

    app.include_router(create_router, prefix='/api')
    app.include_router(get_router, prefix='/api')

    return app
