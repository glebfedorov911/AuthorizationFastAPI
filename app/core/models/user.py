from app.core.models.base import Base

from datetime import datetime

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

import enum


class UserStatus(enum.Enum):
    ACTIVE = "active"
    DELETED = "deleted"
    NOT_CONFIRMED = "not_confirmed"

class User(Base):
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    status: Mapped[UserStatus] = mapped_column(Enum(UserStatus), nullable=False, default=UserStatus.NOT_CONFIRMED) 
    password: Mapped[bytes] = mapped_column(nullable=False)
    access_token: Mapped[str] = mapped_column(nullable=False)
    refresh_token: Mapped[str] = mapped_column(nullable=False)
    expired_access: Mapped[datetime] = mapped_column(nullable=False)
    expired_refresh: Mapped[datetime] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(nullable=True)
    deleted_at: Mapped[datetime] = mapped_column(nullable=True)