from typing import Optional

import mysql.connector
from mysql.connector import errorcode

from models.task_model import Task

"""
    middleware for accessing the task database and performing CRUD operations on the user table
"""


class TaskDAO:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def disconnect(self):
        if self.cnx is not None:
            self.cnx.close()

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
