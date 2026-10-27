# Python Develop Workers Lab

A hands-on starter project for building asynchronous job workers with the [Camunda Orchestration Cluster API Python SDK](https://github.com/camunda/orchestration-cluster-api-python). The included fulfillment process is modeled for Camunda 8.10.

This is a learning exercise, not a fully configured worker application. The worker registration in `main.py` contains a placeholder for you to complete. The process-instance count is zero by default, so starting the app does not create a process instance.

## Prerequisites

- Python 3.10 or later
- A reachable Camunda 8.10 cluster, either SaaS or [Camunda 8 Run](https://docs.camunda.io/docs/self-managed/setup/deploy/local/c8run/)
- Cluster REST API address and authentication details
- Camunda Modeler or another deployment method to deploy the BPMN process

The Python SDK's major version 10 corresponds to Camunda 8.10. `requirements.txt` currently leaves the SDK version unconstrained; select SDK 10.x when setting up against Camunda 8.10.

## Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/camunda-academy/c8-develop-workers-python-lab.git
cd c8-develop-workers-python-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell, create and activate the environment with:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and configure the connection for your cluster. Keep credentials out of source control.

| Variable | SaaS | Local Camunda 8 Run |
|---|---|---|
| `CAMUNDA_REST_ADDRESS` | REST API address from your cluster credentials | Usually `http://localhost:8080/v2` |
| `CAMUNDA_AUTH_STRATEGY` | `OAUTH` | `NONE` |
| `CAMUNDA_CLIENT_ID` | OAuth client ID | Not required |
| `CAMUNDA_CLIENT_SECRET` | OAuth client secret | Not required |
| `CAMUNDA_OAUTH_URL` | Defaults to `https://login.cloud.camunda.io/oauth/token` | Not required |
| `CAMUNDA_TOKEN_AUDIENCE` | Defaults to `zeebe.camunda.io` | Not required |

The application loads `.env` at startup. For SaaS, fill in the OAuth credentials. For local Camunda 8 Run, set `CAMUNDA_AUTH_STRATEGY=NONE` and use the local REST address.

## Deploy and Run

1. Deploy [`resources/bpmn/fulfillment.bpmn`](resources/bpmn/fulfillment.bpmn) to your cluster. Its process ID is `fulfillmentProcess`.
2. Complete the worker-registration exercise in `main.py` so the application can handle the process's service tasks.
3. If you want the application to create a process instance on startup, change `NUM_INSTANCES` from its default of `0` to a positive number.
4. Start the application:

```bash
python main.py
```

When the workers are running, the application prints `Workers started. Press Ctrl+C to exit.` Press Ctrl+C to stop it.

## Project Structure

```text
main.py                          # Client setup, worker registration, and application entry point
handlers/fulfillment_handlers.py # Job handler examples
services/fulfillment_service.py  # Fulfillment business logic
services/process_starter.py     # Creates process instances
utilities/fake_randomizer.py    # Generates sample process variables
resources/bpmn/fulfillment.bpmn # Fulfillment process definition
```

## Troubleshooting

- **Authentication error:** Check `CAMUNDA_REST_ADDRESS` and `CAMUNDA_AUTH_STRATEGY`. For SaaS, verify the client ID, secret, OAuth URL, and audience. The application reports whether required environment variables are missing.
- **Process definition not found:** Deploy `resources/bpmn/fulfillment.bpmn` and verify that the process ID is `fulfillmentProcess`.
- **No process instances appear:** The startup count is zero by default. Set `NUM_INSTANCES` to a positive number to create instances.
- **A process waits at a service task:** Confirm that the worker exercise is complete and that the registered worker type matches the BPMN service task.

## License

This project is licensed under the [Apache License 2.0](LICENSE).
