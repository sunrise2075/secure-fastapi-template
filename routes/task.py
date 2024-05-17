from typing import List

from fastapi import APIRouter, Depends

from auth.authorize import oauth2_scheme
from models.task_model import Task
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


@router.get("/all")
async def get_all_task(token: str = Depends(oauth2_scheme)):
    """
    The endpoint for getting a list of task

    Args:
        token (oauth2 bearer token): the token for the user

    Returns:
        (list[Task]) The list of task stored in db
    """
    tasks: list[Task] = find_all_tasks()
    return tasks
