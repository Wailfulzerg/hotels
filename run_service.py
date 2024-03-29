import asyncio
import logging

from src.containers.app import AppContainer

logger = logging.getLogger(__name__)


async def run_api_server(container: AppContainer):
    from uvicorn import (
        Config,
        Server,
    )

    from src.apps.api.app import create_app

    config = Config(
        app=await create_app(container),
        host=container.config.api.host(),
        port=container.config.api.port(),
    )
    server = Server(config=config)
    try:
        logger.info("Starting Web Server")
        await server.serve()
    finally:
        logger.info("Web Server has been stopped")


async def run_all():
    container = AppContainer()
    container.wire(modules=["src.apps.api.v1.dependencies"])
    logger.info("Starting WebSocket Communication Service")

    tasks = [asyncio.create_task(run_api_server(container))]
    try:
        await asyncio.wait(tasks)
    finally:
        logger.info("WebSocket Communication Service has been stopped")


if __name__ == "__main__":
    asyncio.run(run_all())
