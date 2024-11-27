from fastapi import APIRouter

from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreateScheme

from .TokenWorker import AccessTokenCreater


router = APIRouter(prefix="/auth", tags=["Authorization"])

@router.post("/sign_up")
async def sign_up():
    tkn = AccessTokenCreater()
    print(tkn.get_token({"id": 1, "username": "gleb", "status": "active"}))