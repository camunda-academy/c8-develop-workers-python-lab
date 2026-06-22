from camunda_orchestration_sdk import ConnectedJobContext
from pydantic import BaseModel
import asyncio
import random

from services.tracking_order_service import (
    execute_payment_transaction,
    get_order_tracking,
    validate_and_prepare_shipment,
)


class OrderVariables(BaseModel):
    orderId: str | None = None
    paymentConfirmation: str | None = None
    packaged: bool | None = None


async def track_order_status(job: ConnectedJobContext) -> None:
    variables = job.variables.to_dict()
    order = OrderVariables.model_validate(variables)

    print(f"Order: {order.orderId} Tracking status")

    await get_order_tracking(job)

    print(f"Order: {order.orderId} Status tracked successfully")
    print(f"List of variables from Zeebe: {variables}")


async def process_payment(job: ConnectedJobContext) -> dict:
    variables = job.variables.to_dict()
    order = OrderVariables.model_validate(variables)

    print(f"Order: {order.orderId} Processing payment")

    await asyncio.sleep(random.uniform(1, 3))
    payment_confirmation = await execute_payment_transaction(job)

    print(f"Order: {order.orderId} Successful Transaction: {payment_confirmation}")
    print(f"Process variables retrieved from process_payment: {variables}")

    order.paymentConfirmation = payment_confirmation

    updated_variables = order.model_dump() #convert to json
    print(f"Order: {order.orderId} Payment processed successfully")
    print(f"Process variables returned by process_payment: {updated_variables}")

    return {"paymentConfirmation": order.paymentConfirmation}


async def pack_items(job: ConnectedJobContext) -> dict:
    variables = job.variables.to_dict()
    order = OrderVariables.model_validate(variables)

    print(f"Order: {order.orderId} Packing items")

    await asyncio.sleep(random.uniform(1, 3))
    packaged = await validate_and_prepare_shipment(job)

    print(f"Process variables retrieved from pack_items: {variables}")

    order.packaged = packaged

    updated_variables = order.model_dump() #convert to json
    print(f"Order: {order.orderId} Items packed successfully")
    print(f"Process variables returned by pack_items: {updated_variables}")
    
    return {"packaged": order.packaged}
