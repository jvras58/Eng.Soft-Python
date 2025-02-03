from models.task import TaskStatus
from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    description: str

class TaskCreate(TaskBase):
    urgent: Optional[bool] = False

class TaskUpdate(BaseModel):
    status: TaskStatus

class TaskOut(TaskBase):
    id: int
    status: TaskStatus

    class Config:
        orm_mode = True
