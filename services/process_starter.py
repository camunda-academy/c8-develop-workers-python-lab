from camunda_orchestration_sdk import CamundaAsyncClient, ProcessCreationById, ProcessDefinitionId
from camunda_orchestration_sdk.models import ProcessInstanceCreationInstructionByIdVariables

from utilities.fake_randomizer import get_random


async def start_process_instances(
    client: CamundaAsyncClient,
    num_instances: int,
    process_id: str,
) -> None:
    print(f"Starting: {num_instances} process instances for process: {process_id}")

    for _ in range(num_instances):
        fake_request = get_random()
        print(f"Generating Order({fake_request['orderId']})")

        result = await client.create_process_instance(
            data=ProcessCreationById(
                process_definition_id=ProcessDefinitionId(process_id),
                variables=ProcessInstanceCreationInstructionByIdVariables.from_dict(fake_request),
            )
        )

        print(f"Process instance: {result.process_instance_key} started")

    print(f"Ending: {num_instances} instances created for process: {process_id}")
