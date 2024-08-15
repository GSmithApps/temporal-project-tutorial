# @@@SNIPSTART python-project-template-activities
from temporalio import activity

@activity.defn
async def get_location_from_user() -> str:
    return input("Please give a location: ")

# @@@SNIPEND
