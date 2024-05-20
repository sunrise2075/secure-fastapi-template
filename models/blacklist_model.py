from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from services.pooled_db_service import Base


class Blacklist(Base):

    __tablename__ = 'blacklist'

    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(512), nullable=False)
    blacklist_on = Column(DateTime, nullable=False)
