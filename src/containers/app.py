import logging

from dependency_injector import containers
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import (
    Configuration,
    Container,
    Dependency,
    Singleton,
)

from src.core.order.repositories import AbstractOrderRepository
from src.core.order.services import OrderService
from src.core.room_availability.repositories import AbstractRoomAvailabilityRepository
from src.core.room_availability.services import RoomAvailabilityService
from src.infra.repositories.order import DBOrderRepository
from src.infra.repositories.room_availability import DBRoomAvailabilityRepository

logger = logging.getLogger(__name__)


class ProjectRepositoryContainer(DeclarativeContainer):
    config = Dependency(Configuration)
    order = Singleton(DBOrderRepository)
    room_availability = Singleton(DBRoomAvailabilityRepository)


class ProjectServiceContainer(DeclarativeContainer):
    config = Dependency(Configuration)
    order_repository = Dependency(AbstractOrderRepository)
    room_availability_repository = Dependency(AbstractRoomAvailabilityRepository)

    room_availability = Singleton(
        RoomAvailabilityService, room_availability_repository=room_availability_repository
    )
    order = Singleton(
        OrderService,
        order_repository=order_repository,
        room_availability_service=room_availability,
    )


class AppContainer(containers.DeclarativeContainer):
    config = Configuration()
    config.from_yaml("config.yml")

    repositories: ProjectRepositoryContainer = Container(
        ProjectRepositoryContainer,
        config=config,
    )  # type: ignore

    services: ProjectServiceContainer = Container(
        ProjectServiceContainer,
        config=config,
        order_repository=repositories.order,
        room_availability_repository=repositories.room_availability,
    )
