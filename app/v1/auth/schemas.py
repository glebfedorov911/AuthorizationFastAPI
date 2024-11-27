from pydantic import BaseModel

from app.core.models.user import UserStatus

from datetime import datetime


class UserCreateScheme(BaseModel):
    username: str
    email: str
    status: UserStatus
    password: bytes
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime