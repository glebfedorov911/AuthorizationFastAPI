from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreateScheme

from .TokenWorker import AccessTokenCreater, RefreshTokenCreater

from app.core.models.db_helper import db_helper


router = APIRouter(prefix="/auth", tags=["Authorization"])

@router.post("/sign_up")
async def signUp(userIn: UserCreateScheme, session: AsyncSession = Depends(db_helper.session_depends)):
    pass