from datetime import datetime

from pydantic import AnyUrl


from activate.types.activity_streams.core_types import (
    Activity,
    IntransitiveActivity,
    Object,
    Link,
)


class Accept(Activity):
    type: AnyUrl = "ِAccept"


class Add(Activity):
    type: AnyUrl = "Add"


class Announce(Activity):
    type: AnyUrl = "Announce"


class Arrive(Activity):
    type: AnyUrl = "Arrive"


class Ignore(Activity):
    type: AnyUrl = "Ignore"


class Block(Ignore):
    type: AnyUrl = "Block"


class Create(Activity):
    type: AnyUrl = "Create"


class Delete(Activity):
    type: AnyUrl = "Delete"


class Dislike(Activity):
    type: AnyUrl = "Dislike"


class Flag(Activity):
    type: AnyUrl = "Flag"


class Follow(Activity):
    type: AnyUrl = "Follow"


class Offer(Activity):
    type: AnyUrl = "Offer"


class Invite(Offer):
    type: AnyUrl = "Invite"


class Join(Activity):
    type: AnyUrl = "Join"


class Leave(Activity):
    type: AnyUrl = "Leave"


class Like(Activity):
    type: AnyUrl = "Like"


class Listen(Activity):
    type: AnyUrl = "Listen"


class Move(Activity):
    type: AnyUrl = "Move"


class Question(IntransitiveActivity):
    type: AnyUrl = "Question"

    # oneOf and anyOf must NOT exist together
    # FIXME: how to validate this?
    # oneOf: list[Object | Link] | Object | Link
    # anyOf: list[Object | Link] | Object | Link

    # closed can also be a generic object as per the vocabulary. HOW?
    # closed: datetime | bool


class Reject(Activity):
    type: AnyUrl = "Reject"


class Read(Activity):
    type: AnyUrl = "Read"


class Remove(Activity):
    type: AnyUrl = "Remove"


class TentativeReject(Reject):
    type: AnyUrl = "TentativeReject"


class TentativeAccept(Accept):
    type: AnyUrl = "TentativeAccept"


class Travel(IntransitiveActivity):
    type: AnyUrl = "Travel"


class Undo(Activity):
    type: AnyUrl = "Undo"


class Update(Activity):
    type: AnyUrl = "Update"


class View(Activity):
    type: AnyUrl = "View"
