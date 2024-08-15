# @@@SNIPSTART python-project-template-activities
from temporalio import activity

@activity.defn
async def get_api_key_from_user() -> str:
    return input("Please give your API key: ")

@activity.defn
async def get_location_from_user() -> str:
    return input("Please give a location: ")

# @@@SNIPEND

# @@@SNIPSTART python-project-template-activities
import requests

@activity.defn
async def get() -> str:
    return input("Please give a location: ")

# @@@SNIPEND