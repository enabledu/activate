from pydantic import AnyUrl

from activate.types.activity_streams.core_types import Object, OrderedCollection


class Actor(Object):
    type: AnyUrl = "Actor"

    inbox: OrderedCollection
    outbox: OrderedCollection


class Application(Actor):
    type: AnyUrl = "Application"


class Group(Actor):
    type: AnyUrl = "Group"


class Organization(Actor):
    type: AnyUrl = "Organization"


class Person(Actor):
    type: AnyUrl = "Person"


class Service(Actor):
    type: AnyUrl = "Service"
