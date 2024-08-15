# @@@SNIPSTART python-project-template-run-workflow-hello-world
import asyncio

from run_worker import GeoCode
from temporalio.client import Client


async def main():
    # Create a client connected to the server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    location_from_user = await client.execute_workflow(
        GeoCode.run, id="hello-workflow", task_queue="hello-task-queue"
    )

    print(f"Lat long: {location_from_user}")


if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND
