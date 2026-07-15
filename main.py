import asyncio
import os
import sys

import httpx
from dotenv import load_dotenv

from camunda_orchestration_sdk import CamundaAsyncClient, WorkerConfig
from camunda_orchestration_sdk.errors import ForbiddenError, UnauthorizedError

from handlers.fulfillment_handlers import prepare_kit, collect_deposit, track_courier_status
from services.process_starter import start_process_instances

load_dotenv()

PROCESS_ID = "fulfillmentProcess"
NUM_INSTANCES = 0
WORKER_TIMEOUT_MS = 30_000


def _get_var_state(name: str) -> str:
    value = os.environ.get(name, "")
    return "MISSING" if not value.strip() else "SET"


def _print_auth_error(reason: str) -> None:
    print("Camunda authentication failed.", file=sys.stderr)
    print(f"Reason: {reason}", file=sys.stderr)
    print(file=sys.stderr)
    print("Check these environment variables for OAuth (Camunda SaaS):", file=sys.stderr)
    print(f"- CAMUNDA_REST_ADDRESS: {_get_var_state('CAMUNDA_REST_ADDRESS')}", file=sys.stderr)
    print(f"- CAMUNDA_AUTH_STRATEGY: {_get_var_state('CAMUNDA_AUTH_STRATEGY')} (expected OAUTH)", file=sys.stderr)
    print(f"- CAMUNDA_CLIENT_ID: {_get_var_state('CAMUNDA_CLIENT_ID')}", file=sys.stderr)
    print(f"- CAMUNDA_CLIENT_SECRET: {_get_var_state('CAMUNDA_CLIENT_SECRET')}", file=sys.stderr)
    print(f"- CAMUNDA_OAUTH_URL: {_get_var_state('CAMUNDA_OAUTH_URL')} (usually https://login.cloud.camunda.io/oauth/token)", file=sys.stderr)
    print(f"- CAMUNDA_TOKEN_AUDIENCE: {_get_var_state('CAMUNDA_TOKEN_AUDIENCE')} (usually zeebe.camunda.io)", file=sys.stderr)
    print(file=sys.stderr)
    print("If you are running local Camunda 8 Run, set CAMUNDA_AUTH_STRATEGY=NONE.", file=sys.stderr)


async def _main() -> None:
    async with CamundaAsyncClient() as client:
        await start_process_instances(client, NUM_INSTANCES, PROCESS_ID)

        client.create_job_worker(
            WorkerConfig(job_type="myWorkerType", job_timeout_milliseconds=WORKER_TIMEOUT_MS),
            track_courier_status,
        )

        print("Workers started. Press Ctrl+C to exit.")
        await client.run_workers()


def main() -> None:
    try:
        asyncio.run(_main())
    except KeyboardInterrupt:
        pass
    except (UnauthorizedError, ForbiddenError) as exc:
        _print_auth_error(str(exc))
        sys.exit(1)
    except httpx.HTTPStatusError as exc:
        if exc.response.status_code in (401, 403):
            _print_auth_error(str(exc))
            sys.exit(1)
        raise


if __name__ == "__main__":
    main()
