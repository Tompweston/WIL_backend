from typing import Optional
from beanie import Document
from pydantic import BaseModel


#defines how the task will be structured in the database
class Task(Document):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Pydantic model for task updates
class TaskUpdate(BaseModel):
    description: Optional[str] = None
    completed: Optional[bool] = None