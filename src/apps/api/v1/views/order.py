from fastapi import (
    APIRouter,
    Depends,
)

from src.apps.api.v1.dependencies import get_order_service
from src.apps.api.v1.models.order import OrderModel
from src.core.order.entities import Order
from src.core.order.services import OrderService

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post(path="/", response_model=OrderModel)
async def create_order(
    model: OrderModel, order_service: OrderService = Depends(get_order_service)
):
    order = await order_service.create_order(Order.model_validate(model.model_dump()))
    return OrderModel.model_validate(order.model_dump())
