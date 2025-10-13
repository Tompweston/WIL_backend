from beanie import Document, PydanticObjectId
import datetime
from typing import Optional, Annotated
from pydantic import Field
# structures session in DB
class session(Document): 
    expiresAt: datetime.datetime
    user_id: PydanticObjectId = Field(alias="userId")

