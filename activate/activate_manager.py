from typing import Callable

from activate.types.activity_streams.core_types import Activity


class ActivateManager:
    schema: dict[Activity, Callable]

    def resolve(self, activity: Activity):
        """
        Called by the web adapter to resolve activities
        """
        pass

    def resolver(self):
        """
        A decorator used by the package user to register custom resolvers for activities
        """
        pass
