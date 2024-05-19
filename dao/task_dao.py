from typing import Optional, List

from sqlalchemy.future import select

from sqlalchemy.ext.asyncio import AsyncSession

from models.task_model import Task

"""
    middleware for accessing the task database and performing CRUD operations on the user table
"""


