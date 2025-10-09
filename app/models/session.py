from beanie import Document, PydanticObjectId
import datetime
from pydantic import Field


# structures session in DB
class session(Document):
    expiresAt: datetime.datetime
    user_id: PydanticObjectId = Field(alias="userId")
