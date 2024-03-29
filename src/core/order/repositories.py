from abc import (
    ABC,
    abstractmethod,
)

from src.core.order.entities import Order


class AbstractOrderRepository(ABC):
    @abstractmethod
    async def save_order(self, order: Order) -> Order:
        raise NotImplementedError
