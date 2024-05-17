from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: Optional[str] = None
    email: Optional[str] = None
    is_admin: Optional[bool] = None


class UserInDB(User):
    hashed_password: str
