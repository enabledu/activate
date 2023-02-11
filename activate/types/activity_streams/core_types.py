from datetime import datetime, timedelta

from typing import Union

from pydantic import BaseModel, AnyUrl
from pydantic import Field


class Link(BaseModel):
    # Type is NOT explicitly defined in the standard vocabulary as functional.
    # It is assumed to be functional (a single value) here
    type: AnyUrl = "Link"

    id: AnyUrl

    href: AnyUrl

    # A link relation associated with a Link.
    # The value must conform to both the [HTML5] and [RFC5988] "link relation" definitions.
    # In the [HTML5], any string NOT containing the
    # "space" U+0020, "tab" (U+0009), "LF" (U+000A), "FF" (U+000C), "CR" (U+000D) or "," (U+002C) characters
    # can be used as a valid link relation.
    # rel: list[str] | str

    # should be a MIME media type (how to validate this? Is there a specific set of MIME types?)
    mediaType: str

    # name must NOT include HTML markup (how to enforce this?).
    # It can be a map of the name in different languages (maybe a map would be supported later)
    # content is NOT explicitly defined in the standard vocabulary as functional.
    # It is assumed to be functional (a single value) here
    name: str

    # a [BCP47] Language-Tag.
    # FIXME: how to validate this the language tag in this spec.
    hreflang: str

    # On a Link, specifies a hint as to the rendering height and width
    # in device - independent pixels of the linked resource.
    height: int = Field(ge=0)
    width: int = Field(ge=0)

    preview: Union[list["Object"], list["Link"], "Object", "Link"]


class Object(BaseModel):
    # Type is NOT explicitly defined in the standard vocabulary as functional.
    # It is assumed to be functional (a single value) here
    type: AnyUrl = "Object"

    id: AnyUrl | None

    # attachment: Union[list["Object"], Link, "Object", Link]
    # attributedTo: Union[list["Object"], Link, "Object", Link]
    # audience: Union[list["Object" | Link], "Object", Link]

    # By default, content is an HTML string.
    # Otherwise, use the mediatype property to declare the type of string. How to enforce this?
    # It can be a map of the content in different languages (Maybe implemented later)
    # content is NOT explicitly defined in the standard vocabulary as functional.
    # It is assumed to be functional (a single value) here
    content: str

    # content is NOT explicitly defined in the standard vocabulary as functional.
    # It is assumed to be functional (a single value) here
    # context: Union["Object", Link]

    # name must NOT include HTML markup (how to enforce this?).
    # It can be a map of the name in different languages (maybe a map would be supported later)
    # content is NOT explicitly defined in the standard vocabulary as functional.
    # It is assumed to be functional (a single value) here
    name: str

    endTime: datetime

    # content is NOT explicitly defined in the standard vocabulary as functional.
    # It is assumed to be functional (a single value) here
    # generator: Union["Object", Link]

    # Icons should be of 1:1 aspect ratio and should be suitable for presentation at a small size
    # icon: Union[list["Image", Link], "Image", Link]
    # Images don't have the limitations assumed in icons
    # image: list["Image" | Link] | "Image" | Link

    # inReplyTo: list["Object" | Link] | "Object" | Link
    # location: list["Object" | Link] | "Object" | Link
    # preview: list["Object" | Link] | "Object" | Link
    published: datetime

    # replies is a collection, but it is a functional property (a single collection)
    replies: "Collection"

    startTime: datetime

    # Like the content property
    # summary: list[str] | str

    # Attachments imply association by inclusion. Tags imply association by reference.
    # tag: list["Object" | Link] | "Object" | Link

    updated: datetime
    # url: list["AnyUrl" | Link] | "AnyUrl" | Link
    # to: list["Object" | Link] | "Object" | Link
    # bto: list["Object" | Link] | "Object" | Link
    # cc: list["Object" | Link] | "Object" | Link
    # bcc: list["Object" | Link] | "Object" | Link

    # should be a MIME media type (how to validate this? Is there a specific set of MIME types?)
    mediaType: str

    # The value must be expressed as an xsd: duration as defined by[xmlschema11-2], section 3.3.6
    # (e.g.a period of 5 seconds is represented as "PT5S").
    # FIXME: how to parse and validate this value
    duration: timedelta


class BaseActivity(Object):
    ...
    # Abstract class for the activity and IntransitiveActivity Types

    # Subproperty of "attributedTO"
    # TODO: what are the complications of this?
    # actor: list["Object" | Link] | "Object" | Link

    # target: list["Object" | Link] | "Object" | Link
    # result: list["Object" | Link] | "Object" | Link
    # origin: list["Object" | Link] | "Object" | Link
    # instrument: list["Object" | Link] | "Object" | Link


class IntransitiveActivity(BaseActivity):
    type: AnyUrl = "IntransitiveActivity"


class Activity(BaseActivity):
    type: AnyUrl = "Activity"

    # object: list["Object" | Link] | "Object" | Link


class Collection(Object):
    type: AnyUrl = "Collection"

    # This number might not actually reflect the actual number of items
    # serialized within the Collection object instance
    totalItems: int = Field(ge=0)

    # current: "CollectionPage" | Link
    # first: "CollectionPage" | Link
    # last: "CollectionPage" | Link
    # items: list[Object | Link] | Object | Link


class OrderedCollection(Collection):
    type: AnyUrl = "OrderedCollection"


class CollectionPage(Collection):
    type: AnyUrl = "CollectionPage"

    # partOf: Collection | Link
    # next: "CollectionPage" | Link
    # prev: "CollectionPage" | Link


class OrderedCollectionPage(OrderedCollection, CollectionPage):
    type: AnyUrl = "OrderedCollectionPage"

    startIndex: int = Field(ge=0)
