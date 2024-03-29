from typing import (
    Optional,
    Union,
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)

from src.utils.models import BaseServiceModel


class ErrorResponseModel(BaseModel):
    code: str
    details: Optional[Union[dict, str, list]] = Field(None)


class BaseAppModel(BaseServiceModel):
    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
