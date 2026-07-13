import asyncio
import time

from camunda_orchestration_sdk import ConnectedJobContext

TRACKING_TIME_SECONDS = 10


async def get_courier_status(job: ConnectedJobContext) -> None:
    await asyncio.sleep(TRACKING_TIME_SECONDS)


async def validate_and_prepare_shipment(job: ConnectedJobContext) -> bool:
    return True


async def process_deposit(job: ConnectedJobContext) -> str:
    return str(int(time.time() * 1000))
