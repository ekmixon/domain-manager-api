"""Template document."""
# Standard Python Libraries
from datetime import datetime

# Third-Party Libraries
from utils.db.base import Document
from utils.db.datatypes import StringType, Datetime


class Template(Document):
    """Template document model."""

    name: StringType
    url: StringType
    created: Datetime

    def __init__(self, _id=None):
        """Initialize collection and indices."""
        self._id = _id
        self.collection = "templates"
        self.indexes = ["name"]

    def create(self, name):
        """Create a new template."""
        self.name = name
        self.requester_name = "Dev User"
        self.created = datetime.now()
        return super().create()
