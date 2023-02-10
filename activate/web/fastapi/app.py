from fastapi import FastAPI

from activate.activate_manager import ActivateManager
from activate.types.activity_streams.core_types import Activity

app = FastAPI()


@app.get("/")
async def activitypub_get_endpoint(activity: Activity, activate_manager:ActivateManager):
    return await activate_manager.resolve(activity)


@app.post("/")
async def activitypub_post_endpoint(activity: Activity, activate_manager:ActivateManager):
    return await activate_manager.resolve(activity)
