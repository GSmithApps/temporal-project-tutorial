# @@@SNIPSTART python-geocode-tutorial-run-worker
import asyncio

from temporalio.client import Client

from make_worker import make_worker


async def main():

    client = await Client.connect("localhost:7233", namespace="default")

    worker = make_worker(client)

    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND
