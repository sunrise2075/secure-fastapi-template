from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import config

host: str = config.get("database", "database.host")
user: str = config.get("database", "database.user")
password: str = config.get("database", "database.password")
database: str = config.get("database", "database.dbname")

SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://{0}:{1}@{2}:3306/{3}".format(user, password, host, database)

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
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
