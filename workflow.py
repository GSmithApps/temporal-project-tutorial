# @@@SNIPSTART python-geocode-tutorial-workflow
from datetime import timedelta
from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import (
        get_address_from_user,
        get_api_key_from_user,
        get_lat_long,
        QueryParams,
    )

_TIMEOUT_5_MINS = 5 * 60


@workflow.defn
class GeoCode:

    @workflow.run
    async def run(self) -> list:

        api_key_from_user = await workflow.execute_activity(
            get_api_key_from_user,
            start_to_close_timeout=timedelta(seconds=_TIMEOUT_5_MINS),
        )

        address_from_user = await workflow.execute_activity(
            get_address_from_user,
            start_to_close_timeout=timedelta(seconds=_TIMEOUT_5_MINS),
        )

        query_params = QueryParams(api_key=api_key_from_user, address=address_from_user)

        lat_long = await workflow.execute_activity(
            get_lat_long,
            query_params,
            start_to_close_timeout=timedelta(seconds=_TIMEOUT_5_MINS),
        )

        return lat_long


# @@@SNIPEND
