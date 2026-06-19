# Python Develop Workers Lab

A hands-on lab project demonstrating how to build Camunda 8 job workers using the [Camunda Python SDK](https://github.com/camunda/orchestration-cluster-api-python).

## Prerequisites

- Python 3.10+
- A Camunda 8 cluster (SaaS or local [Camunda 8 Run](https://docs.camunda.io/docs/self-managed/setup/deploy/local/c8run/))
- One of the following IDEs:
  - [Visual Studio Code](https://code.visualstudio.com/) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [PyCharm](https://www.jetbrains.com/pycharm/)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/camunda-academy/c8-develop-workers-python-lab.git
cd c8-develop-workers-python-lab
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env` and fill in your Camunda cluster credentials:

```bash
cp .env.example .env
```

Then edit `.env` with your values:

| Variable | Description |
|---|---|
| `CAMUNDA_REST_ADDRESS` | Your cluster's REST API address |
| `CAMUNDA_AUTH_STRATEGY` | Set to `OAUTH` for SaaS, `NONE` for local Camunda 8 Run |
| `CAMUNDA_CLIENT_ID` | OAuth client ID from your Camunda cluster |
| `CAMUNDA_CLIENT_SECRET` | OAuth client secret from your Camunda cluster |
| `CAMUNDA_OAUTH_URL` | OAuth token URL (SaaS default: `https://login.cloud.camunda.io/oauth/token`) |
| `CAMUNDA_TOKEN_AUDIENCE` | OAuth audience (SaaS default: `zeebe.camunda.io`) |

> **Note:** The app loads these from the `.env` file automatically via python-dotenv.

### 4. Run the project

```bash
python main.py
```

You should see:

```
Workers started. Press Ctrl+C to exit.
```

Press **Ctrl+C** to stop the workers.

## Project Structure

```
main.py                          # Entry point — sets up workers and starts the client
handlers/
  order_handlers.py              # Job handler implementations
services/
  process_starter.py             # Starts process instances
  tracking_order_service.py      # Business logic for order tracking
utilities/
  fake_randomizer.py             # Helper utilities
Resources/
  Bpmn/
    order.bpmn                   # BPMN process definition
```

## Troubleshooting

If the application fails to start with an authentication error, verify your environment variables are correctly set. The error output will indicate which variables are `MISSING`.

## License

This project is licensed under the [Apache License 2.0](LICENSE).
