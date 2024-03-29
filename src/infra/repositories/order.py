from src.core.order.entities import Order
from src.core.order.repositories import AbstractOrderRepository


class DBOrderRepository(AbstractOrderRepository):
    def __init__(self):
        self._db = []

    async def save_order(self, order: Order) -> Order:
        self._db.append(order.model_dump())
        return order
