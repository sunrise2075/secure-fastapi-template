from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from dao.user_dao import UserDAO
from models.user_model import User


class UserService:
    @staticmethod
    async def add_new_user(user: User, db: AsyncSession):
        await UserDAO.create_user(user, db)

    @staticmethod
    async def user_exists(username: str, db: AsyncSession) -> bool:
        user: User = await UserDAO.get_user_by_username(username, db)
        return user is not None

    @staticmethod
    async def get_next_avail_id(db: AsyncSession) -> int:
        last_id = await UserDAO.get_last_user_id(db)
        return 1 if last_id is None else last_id + 1

    @staticmethod
    async def get_user(username: str, db: AsyncSession) -> Optional[User]:
        user: User = await UserDAO.get_user_by_username(username, db)
        return user
