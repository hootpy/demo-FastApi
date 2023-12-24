from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.api.common.routes import router as common_router
from app.api.routes import router as api_router
from app.common.utils.version import get_project_version
from app.setup.database import sessionmanager
from app.setup.setting import SETTING


def create_app() -> FastAPI:
    database_url = (
        f"postgresql+asyncpg://{SETTING.POSTGRES_USERNAME}:{SETTING.POSTGRES_PASSWORD}"
        f"@{SETTING.POSTGRES_SERVER}:{SETTING.POSTGRES_PORT}/{SETTING.POSTGRES_DATABASE}"
    )
    sessionmanager.init(database_url)

    @asynccontextmanager
    async def lifespan(
        app: FastAPI,
    ) -> AsyncGenerator[None, None]:
        yield
        if sessionmanager._engine is not None:
            await sessionmanager.close()

    app = FastAPI(
        title="Demo FastAPI",
        version=get_project_version(),
        description="Demo FastAPI",
        lifespan=lifespan,
    )

    app.include_router(common_router)
    app.include_router(api_router, prefix="/api")

    return app
