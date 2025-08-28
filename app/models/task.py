from typing import Optional
from beanie import Document
from pydantic import BaseModel


#defines how the task will be structured in the database
class Task(Document):
    title: str
    description: Optional[str] = None
    completed: bool = False
    userID: Optional[str] = None  # Optional field for user ID
    urgent: bool = False  # New field to indicate if the task is urgent

# Pydantic model for task updates
class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]
    userID: Optional[str]
    urgent: Optional[bool]