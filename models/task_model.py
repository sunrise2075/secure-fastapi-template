from sqlalchemy import Column, Integer, String

from services.pooled_db_service import Base


class Task(Base):
    __tablename__ = "task"

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    task = Column(String(256), nullable=False)
    status = Column(String(256), nullable=False)
