from fastapi import APIRouter, Body, Depends

from activate.activate_manager import ActivateManager, get_activate_manager
from activate.types.activity_streams.core_types import Activity

activate_router = APIRouter()


# TODO: check the initialization of the activate manager
# TODO: check the middleware to ensure the right content-type and accept header are correct


@activate_router.get("/")
async def activitypub_get_endpoint(
    activity: Activity = Body(),
    activate_manager: ActivateManager = Depends(get_activate_manager),
):
    return await activate_manager.resolve(activity)


@activate_router.post("/")
async def activitypub_post_endpoint(
    activity: Activity,
    activate_manager: ActivateManager = Depends(get_activate_manager),
):
    return await activate_manager.resolve(activity)
