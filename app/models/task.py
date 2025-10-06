from typing import Optional
from beanie import Document
from pydantic import BaseModel


#defines how the task will be structured in the database
class Task(Document):
    title: str
    description: str 
    completed: bool = False
    user_id: Optional[str] = None  # Optional field for user ID
    urgent: bool = False  # New field to indicate if the task is urgent

# Pydantic model for task updates
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    user_id: Optional[str] = None
    urgent: Optional[bool] = None