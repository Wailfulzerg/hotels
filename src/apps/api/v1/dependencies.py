import logging

from dependency_injector.wiring import (
    Provide,
    inject,
)
from fastapi import Depends

from src.containers.app import AppContainer
from src.core.order.services import OrderService

logger = logging.getLogger(__name__)


@inject
def get_app_container(
    container: AppContainer = Depends(Provide[AppContainer]),
) -> AppContainer:
    return container


def get_order_service(
    container: AppContainer = Depends(get_app_container),
) -> OrderService:
    return container.services.order()


def get_room_availability_service(
    container: AppContainer = Depends(get_app_container),
) -> OrderService:
    return container.services.room_availability()
