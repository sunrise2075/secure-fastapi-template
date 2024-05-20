from typing import Optional

from sqlalchemy import Column, Integer, String, Boolean

from services.pooled_db_service import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)
    is_admin = Column(Boolean, nullable=False)
    hashed_password = Column(String(512), nullable=False)
