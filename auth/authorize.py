from typing import Annotated

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from models.token_model import TokenData
from auth.hashing import verify_password, is_token_blacklisted, SECRET_KEY, ALGORITHM
from models.user_model import User
from services.pooled_db_service import get_db
from services.user_service import UserService

"""
    authorization function middleware
"""

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://127.0.0.1:8000/auth/login")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


async def authenticate_user(username: str, password: str, db: AsyncSession):
    user: User = await UserService.get_user(username, db)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: AsyncSession = Depends(get_db)):
    is_blocked: bool = await is_token_blacklisted(token, db)
    print("is_blocked------> ???", is_blocked)
    if is_blocked:
        raise credentials_exception
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        print("username------> ???", username)
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await UserService.get_user(username=token_data.username, db=db)
    if user is None:
        raise credentials_exception
    return user
