from datetime import date

from pydantic import (
    EmailStr,
    Field,
    model_validator,
)

from src.apps.api.models import BaseAppModel


class OrderModel(BaseAppModel):
    hotel_id: str
    room_id: str
    email: EmailStr
    date_from: date = Field(alias="from")
    date_to: date = Field(alias="to")

    @model_validator(mode="after")
    def check_dates(self) -> "OrderModel":
        if self.date_from > self.date_to:
            raise ValueError("Invalid dates")
        return self
