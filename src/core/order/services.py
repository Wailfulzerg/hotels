from src.core.order.entities import Order
from src.core.order.repositories import AbstractOrderRepository
from src.core.room_availability.services import RoomAvailabilityService
from src.core.shared.exceptions import DatesNotAvailableError


class OrderService:
    def __init__(
        self,
        order_repository: AbstractOrderRepository,
        room_availability_service: RoomAvailabilityService,
    ):
        self.order_repo = order_repository
        self.room_availability_service = room_availability_service

    async def create_order(self, order: Order):
        availability = await self.room_availability_service.check_availability(
            order.hotel_id, order.room_id, order.days_between
        )
        if not availability:
            raise DatesNotAvailableError
        return await self.order_repo.save_order(order)
