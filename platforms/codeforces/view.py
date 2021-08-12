from fastapi import Depends, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from config.errcode import BadRequestException, NotFoundException
from models.db import get_db
from models.user import User
from platforms.codeforces.api import userinfo_async, login
from platforms.codeforces.model import UserInfo
from platforms.codeforces.schema import UserInfo as UserInfoSchema
from schemas.auth import get_current_auth

router = APIRouter(prefix="/codeforces")


class BindRequest(BaseModel):
    handle: str
    password: str
    api_key: str
    secret: str


@router.get("/me", response_model=UserInfoSchema)
def me(user: User = Depends(get_current_auth)):
    if user.codeforces is None:
        raise NotFoundException("codeforces not found")
    return user.codeforces


@router.post("/bind")
async def bind(
    request: BindRequest,
    user: User = Depends(get_current_auth),
    db: Session = Depends(get_db),
):
    if request.api_key == "" or request.secret == "":
        raise BadRequestException("请提供 apiKey 与 secret")
    cf_user = db.query(UserInfo).filter(UserInfo.handle == request.handle).first()
    if cf_user:
        raise BadRequestException("该账号已经被绑定")
    logged = await login(request.handle, request.password)
    if logged is False:
        raise BadRequestException("用户名或密码错误")
    resp = await userinfo_async(request.handle, request.api_key, request.secret)
    cf_user = UserInfo(
        **resp.dict(),
        password=request.password,
        api_key=request.api_key,
        secret=request.secret,
        user=user
    )
    db.add(cf_user)
    db.commit()
    db.refresh(cf_user)
    return resp
