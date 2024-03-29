from datetime import datetime

from src.core.shared.entities import EntityModel


class RoomAvailability(EntityModel):
    hotel_id: str
    room_id: str
    date: datetime
    quota: int
