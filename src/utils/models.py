from pydantic import BaseModel

from src.utils.transformation import (
    to_camel_case,
    to_snake_case,
)


class BaseServiceModel(BaseModel):
    def model_dump(
        self,
        *args,
        by_camel: bool = False,
        by_snake: bool = False,
        **kwargs,
    ) -> dict:
        obj = super().model_dump(*args, **kwargs)
        if by_camel and by_snake:
            raise ValueError("by_snake and by_camel can`t be selected by same time")
        if by_camel:
            return to_camel_case(obj)
        if by_snake:
            return to_snake_case(obj)
        return obj
