from typing import TypeVar

from pydantic import ConfigDict

from src.utils.models import BaseServiceModel


class EntityModel(BaseServiceModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True, use_enum_values=True)


ENTITY_TYPE = TypeVar("ENTITY_TYPE", bound=EntityModel)
