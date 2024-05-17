from typing import Optional

from pydantic import BaseModel


class Task(BaseModel):
    task_id: int
    task: Optional[str] = None
    status: Optional[str] = None
