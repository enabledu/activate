from datetime import datetime

from pydantic import AnyUrl, Field

from activate.types.activity_streams.core_types import Object, Link


class Relationship(Object):
    type: AnyUrl = "Relationship"

    subject: Object | Link

    # NOT explicitly functional in the spec.
    # Here it is considered functional though.
    object: Object | Link

    relationship: Object
    

class Article(Object):
    type: AnyUrl = "Article"
    
    
class Document(Object):
    type: AnyUrl = "Document"
    
    
class Audio(Document):
    type: AnyUrl = "Audio"
    
    
class Video(Document):
    type: AnyUrl = "Video"
    
    
class Note(Object):
    type: AnyUrl = "Note"


class Page(Document):
    """
    Represents a web page
    """
    type: AnyUrl = "Page"
    
    
class Event(Object):
    type: AnyUrl = "Event"


class Place(Object):
    type: AnyUrl = "Place"

    accuracy: float = Field(ge=0.0, le=100.0)
    altitude: float
    latitude: float
    longitude: float
    radius: float = Field(ge=0.0)

    # The unit of measurements.
    # By default it is meters.
    # How to validate it is a unit?
    units: str = "m"
    

class Mention(Link):
    """
    A specialized Link that represents an @mention.
    """
    type: AnyUrl = "Mention"


class Profile(Object):
    type: AnyUrl = "Profile"

    describes: Object


class Tombstone(Object):
    """
    A Tombstone represents a content object that has been deleted.
    It can be used in Collections to signify that
    there used to be an object at this position, but it has been deleted.
    """
    type: AnyUrl = "Tombstone"

    formerType: Object
    deleted: datetime
