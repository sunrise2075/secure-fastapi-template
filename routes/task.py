from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.authorize import get_current_user
from models.task_model import Task
from models.user_model import User
from services.pooled_db_service import get_db

"""
    API router for task management

    Attributes:
        router (APIRouter): the router for the endpoint

    Methods:
        [GET] /api/task
        get_all_task: the endpoint for getting the list of task
"""

router = APIRouter(
    prefix="/api/task",
    tags=["task"],
    responses={404: {"description": "The requested page was not found"}},
)

oauth2_scheme2 = OAuth2PasswordBearer(tokenUrl="http://127.0.0.1:8000/task/all")


@router.get("/all")
async def get_all_task(current_user: Annotated[User, Depends(get_current_user)], db: AsyncSession = Depends(get_db)):
    """
    The endpoint for getting a list of task

    Args:
        current_user object of the user

    Returns:
        (list[Task]) The list of task stored in db
    """
    if current_user is not None:
        result = await db.execute(select(Task))
        task_list = result.scalars().all()
        return [Task(task_id=task.task_id, task=task.task, status=task.status) for task in task_list]
    else:
        return []


@router.get("/{id}")
async def get_all_task(id: int, current_user: Annotated[User, Depends(get_current_user)], db: AsyncSession = Depends(get_db)):
    """
    The endpoint for getting tas by id

    Args:
        current_user object of the user

    Returns:
        (list[Task]) The targeting task stored in db
    """
    if current_user is not None:
        result = await db.execute(select(Task).filter(Task.task_id == id))
        task: Task = result.scalars().first()
        if task is not None:
            return Task(task_id= task.task_id, task=task.task, status=task.status)
        else:
            return None
    else:
        return None
