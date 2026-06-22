from camunda_orchestration_sdk import ConnectedJobContext
from pydantic import BaseModel
import asyncio
import random

from services.tracking_order_service import (
    execute_payment_transaction,
    get_order_tracking,
    validate_and_prepare_shipment,
)


async def track_order_status(job: ConnectedJobContext) -> None:
    print(f"Handling job: {job.job_key} Tracking status")
    await get_order_tracking(job)
    print(f"Handling job: {job.job_key} Order status tracked successfully")


async def process_payment(job: ConnectedJobContext) -> None:
    print(f"Handling job: {job.job_key} Processing payment")
    payment_confirmation = await execute_payment_transaction(job)
    print(f"Handling job: {job.job_key} Payment processed successfully")


async def pack_items(job: ConnectedJobContext) -> None:
    print(f"Handling job: {job.job_key} Packing items")
    await validate_and_prepare_shipment(job)
    print(f"Handling job: {job.job_key} Items packed successfully")
