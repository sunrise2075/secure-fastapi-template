from config import config

from dao.user_dao import UserDAO
from dao.task_dao import TaskDAO

user_dao = UserDAO(
    host=config.get("database", "database.host"),
    user=config.get("database", "database.user"),
    password=config.get("database", "database.password"),
    database=config.get("database", "database.dbname")
)

task_dao = TaskDAO(
    host=config.get("database", "database.host"),
    user=config.get("database", "database.user"),
    password=config.get("database", "database.password"),
    database=config.get("database", "database.dbname")
)


def connect_all():
    try:
        user_dao.connect()
        print("User DB connection open successfully")

        task_dao.connect()
        print("task DB connection open successfully")
    except Exception as e:
        print("DB connection error:", e)


def dis_connect_all():
    try:
        user_dao.disconnect()
        print("User DB connection closing successfully")

        task_dao.disconnect()
        print("task DB connection closing successfully")
    except Exception as e:
        print("DB connection closing error:", e)