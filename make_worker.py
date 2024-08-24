# @@@SNIPSTART python-geocode-tutorial-make-worker
from temporalio.client import Client
from temporalio.worker import Worker

from activities import get_address_from_user, get_api_key_from_user, get_lat_long
from workflow import GeoCode


def make_worker(client: Client):

    worker = Worker(
        client,
        task_queue="geocode-task-queue",
        workflows=[GeoCode],
        activities=[get_address_from_user, get_api_key_from_user, get_lat_long],
    )

    return worker


# @@@SNIPEND
