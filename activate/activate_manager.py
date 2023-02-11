from typing import Callable


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
        # TODO: check the schema for a registered activity that matches the requested one
        # TODO: if so, call it
        if self.schema.get(activity):
            callable = self.schema[activity]
            callable()

    def resolver(self, resolver_function):
        """
        A decorator used by the package user to register custom resolvers for activities
        """

        def wrapper(activity: str):
            # TODO: check that the first argument to the function is an activity
            # TODO: if so, register the resolver function in schema

            self.schema[activity] = resolver_function

            return resolver_function

        return wrapper


activate_manager = ActivateManager()