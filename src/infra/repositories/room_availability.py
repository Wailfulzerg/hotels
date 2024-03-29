from datetime import datetime, date

from src.core.room_availability.repositories import AbstractRoomAvailabilityRepository


class DBRoomAvailabilityRepository(AbstractRoomAvailabilityRepository):
    def __init__(self):
        self._db = [
            {"hotel_id": "reddison", "room_id": "lux", "date": date(2024, 1, 1), "quota": 1},
            {"hotel_id": "reddison", "room_id": "lux", "date": date(2024, 1, 2), "quota": 1},
            {"hotel_id": "reddison", "room_id": "lux", "date": date(2024, 1, 3), "quota": 1},
            {"hotel_id": "reddison", "room_id": "lux", "date": date(2024, 1, 4), "quota": 1},
            {"hotel_id": "reddison", "room_id": "lux", "date": date(2024, 1, 5), "quota": 0},
        ]

    async def get_availability(self, hotel_id: str, room_id: str, dates: list[datetime]) -> bool:
        dates_availability = []
        for day in dates:
            availability = next(
                (
                    a
                    for a in self._db
                    if a["hotel_id"] == hotel_id
                    and a["room_id"] == room_id
                    and a["date"] == day
                    and a["quota"] > 0
                ),
                None,
            )
            if availability:
                availability["quota"] -= 1
                dates_availability.append(availability)
            else:
                return False
        if len(dates) != len(dates_availability): 
            for date_availability in dates_availability:
                date_availability["quota"] += 1
            return False
        return True
