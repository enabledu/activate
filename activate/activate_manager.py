import functools
from typing import Callable

from fastapi import HTTPException

from activate.types.activity_streams.core_types import Activity

activate_manager: "ActivateManager"


def get_activate_manager():
    global activate_manager
    if not activate_manager:
        activate_manager = ActivateManager()
    return activate_manager


class ActivateManager:
    schema: dict[str, Callable] = {}

    async def resolve(self, activity: str):
        """
        Called by the web adapter to resolve activities
        """
        if self.schema[Activity]:
            return await self.schema[Activity](activity)
        else:
            raise HTTPException(status_code=404, detail="Activity can NOT be handled")

    def resolver(self, resolver_function):
        """
        A decorator used by the package user to register custom resolvers for activities
        """
        @functools.wraps(resolver_function)
        async def wrapper(activity: Activity):
            self.schema[Activity] = resolver_function
            return resolver_function(activity)

        return wrapper


activate_manager = ActivateManager()
