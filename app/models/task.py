from typing import Optional
from beanie import Document

class task(Document):
    title: str
    description: Optional[str] = None
    completed: bool = False