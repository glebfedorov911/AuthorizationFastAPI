from fastapi import APIRouter

from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserCreateScheme

from .TokenWorker import AccessTokenCreater, RefreshTokenCreater


router = APIRouter(prefix="/auth", tags=["Authorization"])

@router.post("/check_tkn_a")
async def check_tkn_a():
    tkn: AccessTokenCreater = AccessTokenCreater()
    token = (tkn.get_token({"id": 1, "username": "gleb", "status": "active"}))
    print(token)
    return tkn.read_token(token)

@router.post("/check_tkn_r")
async def check_tkn_r():
    tkn: RefreshTokenCreater = RefreshTokenCreater()
    token = (tkn.get_token({"id": 1, "username": "gleb", "status": "active"}))
    print(token)
    return tkn.read_token(token)