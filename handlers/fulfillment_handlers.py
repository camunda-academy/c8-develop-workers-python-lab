from camunda_orchestration_sdk import ConnectedJobContext
from pydantic import BaseModel
import asyncio
import random

from services.fulfillment_service import (
    process_deposit,
    get_courier_status,
    validate_and_prepare_shipment,
)


async def track_courier_status(job: ConnectedJobContext) -> None:
    job.log.info(f"Handling job: {job.job_key} Tracking status")
    await get_courier_status(job)
    job.log.info(f"Handling job: {job.job_key} Courier status tracked successfully")


async def collect_deposit(job: ConnectedJobContext) -> None:
    job.log.info(f"Handling job: {job.job_key} Collecting deposit")
    await process_deposit(job)
    job.log.info(f"Handling job: {job.job_key} Deposit collected successfully")


async def prepare_kit(job: ConnectedJobContext) -> None:
    job.log.info(f"Handling job: {job.job_key} Preparing kit")
    await validate_and_prepare_shipment(job)
    job.log.info(f"Handling job: {job.job_key} Kit prepared successfully")
