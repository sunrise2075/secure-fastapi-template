from sqlalchemy.ext.asyncio import AsyncSession

from dao.user_dao import UserDAO


class TokenService:

    @staticmethod
    async def add_token_to_blacklist(token: str, db: AsyncSession):
        await UserDAO.blacklist_token(token, db)

    @staticmethod
    async def check_if_token_is_blacklisted(token: str, db: AsyncSession) -> bool:
        return await UserDAO.is_token_blacklisted(token, db)
