from camunda_orchestration_sdk import ConnectedJobContext
from pydantic import BaseModel, Field

from services.fulfillment_service import (
    process_deposit,
    get_courier_status,
    validate_and_prepare_shipment,
)

class DepositInput(BaseModel):
    requestId: str 
    price: float

class CourierStatusInput(BaseModel):
    request_id: str = Field(validation_alias="requestId")

class PrepareKitInput(BaseModel):
    request_id: str = Field(validation_alias="requestId")

async def track_courier_status(job: ConnectedJobContext) -> None:
    
    input_data = CourierStatusInput(**job.variables.to_dict())

    job.log.info(f"Tracking courier status for request: {input_data.request_id}")
    await get_courier_status(job)
    job.log.info(f"Courier status tracked successfully for request: {input_data.request_id}") 


async def collect_deposit(job: ConnectedJobContext) -> None:
    input_data = DepositInput(**job.variables.to_dict())

    job.log.info(f"Collecting deposit for request: {input_data.requestId}")
    payment_confirmation = await process_deposit(job, input_data.price)
    job.log.info(f"Deposit collected successfully for request: {input_data.requestId} @ {payment_confirmation}")
    return {"paymentConfirmation": payment_confirmation}

async def prepare_kit(job: ConnectedJobContext) -> None:
    input_data = PrepareKitInput(**job.variables.to_dict())

    job.log.info(f"Preparing kit for request {input_data.request_id}")
    kit_ready = await validate_and_prepare_shipment(job)
    job.log.info(f"Kit prepared for request {input_data.request_id}")
    return {"kitReady": kit_ready}
