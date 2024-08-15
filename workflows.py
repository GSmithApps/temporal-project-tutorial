# @@@SNIPSTART python-project-template-workflows
from datetime import timedelta
from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import get_location_from_user, get_api_key_from_user

@workflow.defn
class SayHello:
    @workflow.run
    async def run(self) -> str:
        api_key_from_user =  await workflow.execute_activity(
            get_api_key_from_user, start_to_close_timeout=timedelta(seconds=5)
        )
        location_from_user =  await workflow.execute_activity(
            get_location_from_user, start_to_close_timeout=timedelta(seconds=5)
        )
        return location_from_user


# @@@SNIPEND
