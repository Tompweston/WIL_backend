from typing import Optional
from beanie import Document


#defines how the task will be structured in the database
class Task(Document):
    title: str
    description: Optional[str] = None
    completed: bool = False
