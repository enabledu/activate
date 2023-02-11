from typing import Callable

from activate.types.activity_streams.core_types import Activity


def get_activate_manager():
    return ActivateManager()


class ActivateManager:
    schema: dict[Activity, Callable]

    def resolve(self, activity: Activity):
        """
        Called by the web adapter to resolve activities
        """
        # TODO: check the schema for a registered activity that matches the requested one
        # TODO: if so, call it

    def resolver(self):
        """
        A decorator used by the package user to register custom resolvers for activities
        """
        def wrapper(resolver_function):
            # TODO: check that the first argument to the function is an activity
            # TODO: if so, register the resolver function in schema
            return resolver_function

        return wrapper
