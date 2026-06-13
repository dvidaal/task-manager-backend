from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "todo"

class TaskResponse(TaskCreate):
    id: int

    class Config:
        from_attributes = True
