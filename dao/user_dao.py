from datetime import datetime
from typing import Optional

import mysql.connector
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from models.blacklist_model import Blacklist
from models.user_model import User

"""
    middleware for accessing the user database and performing CRUD operations on the user table
"""


class UserDAO:

    @staticmethod
    async def create_user(new_user: User, db: AsyncSession):
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user

    @staticmethod
    async def get_user_by_username(username: str, db: AsyncSession) -> Optional[User]:
        result = await db.execute(select(User).filter(User.username == username))
        user: User = result.scalars().one_or_none()
        return user

    @staticmethod
    async def get_last_user_id(db: AsyncSession) -> int:
        rs = await db.execute(text("SELECT MAX(id) FROM users"))
        max_id = rs.scalar_one_or_none()
        return max_id

    @staticmethod
    async def blacklist_token(token: str, db: AsyncSession):
        """
        Add a token to the blacklist table with the current timestamp
        """
        black_list = Blacklist(token=token, blacklist_on=datetime.now())
        db.add(black_list)
        await db.commit()
        await db.refresh(black_list)
        return black_list

    @staticmethod
    async def is_token_blacklisted(token: str, db: AsyncSession) -> bool:
        """
        Check if a token exists in the blacklist table
        """
        result = await db.execute(select(Blacklist).filter(Blacklist.token == token))
        black_list: Blacklist = result.scalars().one_or_none()
        return black_list is not None
