from abc import (
    ABC,
    abstractmethod,
)
from datetime import datetime


class AbstractRoomAvailabilityRepository(ABC):
    @abstractmethod
    async def get_availability(self, hotel_id: str, room_id: str, dates: list[datetime]) -> bool:
        raise NotImplementedError
