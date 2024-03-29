from datetime import datetime

from src.core.room_availability.repositories import AbstractRoomAvailabilityRepository


class RoomAvailabilityService:
    def __init__(self, room_availability_repository: AbstractRoomAvailabilityRepository):
        self.room_availability_repo = room_availability_repository

    async def check_availability(self, hotel_id: str, room_id: str, dates: list[datetime]) -> bool:
        availability = await self.room_availability_repo.get_availability(hotel_id, room_id, dates)
        if not availability:
            return False
        return True
