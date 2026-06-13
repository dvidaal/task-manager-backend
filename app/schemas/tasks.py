from pydantic import BaseModel, ConfigDict
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "todo"

class TaskResponse(TaskCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
