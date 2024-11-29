from pydantic import BaseModel

from app.core.models.user import UserStatus

from datetime import datetime


class UserCreateScheme(BaseModel):
    username: str
    email: str
    status: UserStatus = UserStatus.NOT_CONFIRMED
    password: str
    created_at: datetime = datetime.now()
    updated_at: datetime = None
    deleted_at: datetime = None