from typing import Optional

import mysql.connector
from mysql.connector import errorcode

from dao.base_dao import BaseDao
from models.task_model import Task

"""
    middleware for accessing the task database and performing CRUD operations on the user table
"""


class TaskDAO(BaseDao):

    def get_task_by_id(self, task_id) -> Optional[Task]:
        cursor = self.cnx.cursor()
        query = ("SELECT * "
                 "FROM task "
                 "WHERE task_id = %s")
        cursor.execute(query, (task_id,))
        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None
        return Task(**dict(zip(['task_id', 'task', 'status'], row)))

    def find_all_tasks(self) -> list[Task]:
        cursor = self.cnx.cursor()
        query = "SELECT * FROM task"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        result = []
        for row in rows:
            result.append(Task(**dict(zip(['task_id', 'task', 'status'], row))))
        return result
