from datetime import (
    datetime,
    timedelta, date,
)

from pydantic import EmailStr

from src.core.shared.entities import EntityModel


class Order(EntityModel):
    hotel_id: str
    room_id: str
    email: EmailStr
    date_from: date
    date_to: date

    @property
    def days_between(self):
        delta = self.date_to - self.date_from
        return [self.date_from + timedelta(days=i) for i in range(delta.days + 1)]
