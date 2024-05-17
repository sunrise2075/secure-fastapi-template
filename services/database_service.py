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

try:
    user_dao.connect()
    print("User DB connection successful")

    task_dao.connect()
    print("task DB connection successful")
except Exception as e:
    print("DB connection error:", e)
