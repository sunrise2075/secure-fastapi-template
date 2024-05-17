from typing import List, Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from auth.authorize import oauth2_scheme, get_current_user
from models.task_model import Task
from models.user_model import UserInDB
from services.task_service import find_all_tasks

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
async def get_all_task(current_user: Annotated[UserInDB, Depends(get_current_user)]):
    """
    The endpoint for getting a list of task

    Args:
        token (oauth2 bearer token): the token for the user

    Returns:
        (list[Task]) The list of task stored in db
    """
    if current_user is not None:
        tasks: list[Task] = find_all_tasks()
        return tasks
    else:
        return []
