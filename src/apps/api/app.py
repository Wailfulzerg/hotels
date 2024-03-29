import logging

from typing import Optional

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from src.containers.app import AppContainer
from src.core.shared.exceptions import DomainError

from .exception_handlers import (
    domain_exception_handler,
    internal_exception_handler,
    validation_exception_handler,
)
from .models import ErrorResponseModel

logger = logging.getLogger(__name__)


async def create_app(container: Optional[AppContainer] = None) -> FastAPI:
    if not container:
        container = container or AppContainer()
        await container.init_resources()

        container.wire(
            modules=[
                "src.apps.api.dependencies",
            ]
        )
    container.config.service.api.root_path() or ""
    swagger_path_prefix = container.config.service.api.swagger_path_prefix() or ""
    app = FastAPI(
        title=container.config.service.name(),
        version="v1",
        responses={
            HTTP_400_BAD_REQUEST: {"model": ErrorResponseModel},
            HTTP_500_INTERNAL_SERVER_ERROR: {"model": ErrorResponseModel},
        },
        exception_handlers={
            RequestValidationError: validation_exception_handler,
            DomainError: domain_exception_handler,
            ValidationError: validation_exception_handler,
            Exception: internal_exception_handler,
        },
        servers=[{"url": swagger_path_prefix}],
    )

    app.state.dependency_container = container

    from src.apps.api.v1.views import ROUTERS as V1_ROUTERS
    from src.apps.api.views import ROUTERS as SYSTEM_ROUTERS

    for r in V1_ROUTERS:
        app.include_router(r, prefix="/api")

    for r in SYSTEM_ROUTERS:
        app.include_router(r)

    # OpenAPI
    openapi_schema = app.openapi()
    for path in openapi_schema["paths"].values():
        for method in path.values():
            # Убираем ненужные статусы (FastAPI 422 по умолчанию добавляет)
            method["responses"].pop("422", None)
    app.openapi_schema = openapi_schema
    return app
