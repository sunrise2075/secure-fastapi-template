from typing import Optional

from models.task_model import Task
from services.database_service import task_dao


def find_all_tasks() -> list[Task]:
    return task_dao.find_all_tasks()


def get_task_by_id(task_id) -> Optional[Task]:
    return task_dao.get_task_by_id(task_id)
