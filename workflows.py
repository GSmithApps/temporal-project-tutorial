# @@@SNIPSTART python-project-template-workflows
from datetime import timedelta
from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import get_location_from_user

@workflow.defn
class SayHello:
    @workflow.run
    async def run(self) -> str:
        address_from_user =  await workflow.execute_activity(
            get_location_from_user, start_to_close_timeout=timedelta(seconds=5)
        )


# @@@SNIPEND
