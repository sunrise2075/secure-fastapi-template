import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import config

use_cloud: bool = config.get("database", "database.usecloud")
host: str = config.get("database", "database.host")
user: str = config.get("database", "database.user")
password: str = config.get("database", "database.password")
database: str = config.get("database", "database.dbname")

if use_cloud:
    DATABASE_URL = "postgresql+asyncpg://{0}:{1}@{2}:5432/{3}".format(user, password, host, database)
else:
    DATABASE_URL = os.getenv("DATABASE_URL", "")

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_size=10,
    max_overflow=20
)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()


# Dependency to get DB session
async def get_db():
    async with SessionLocal() as session:
        yield session
