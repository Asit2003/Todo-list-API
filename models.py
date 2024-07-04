from pydantic import BaseModel
from typing import Optional

class TodoItem(BaseModel):
    id: Optional[int]
    title: str
    description: Optional[str] = None
    completed: bool = False
