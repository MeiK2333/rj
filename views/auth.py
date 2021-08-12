import re

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from config import EMAIL_PATTERN
from config.errcode import UnauthorizedException, BadRequestException
from config.logger import module_logger
from models.db import get_db
from models.user import User
from schemas.auth import (
    verify_password,
    create_access_token,
    get_password_hash,
    get_current_auth,
    Auth,
)

router = APIRouter()
logger = module_logger("auth")


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise UnauthorizedException("用户名或密码错误")
    access_token = create_access_token(user, db=db)
    logger.info(f"login user: {user.handle}")
    return {"access_token": access_token, "token_type": "bearer"}


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


@router.post("/register")
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if user:
        raise UnauthorizedException("用户已存在")
    if (not 0 < len(request.username) < 64) or (not request.username.isalnum()):
        raise BadRequestException(errmsg="用户名必须由 1-64 位的大小写字母与数字组成")

    # TODO: 发送验证码到邮箱
    if not re.match(EMAIL_PATTERN, request.email):
        raise BadRequestException(errmsg="邮箱验证失败")

    user = User(
        username=request.username,
        hashed_password=get_password_hash(request.password),
        email=request.email,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    logger.info(f"register new user: {user.username}")
    return {}


@router.get("/me", response_model=Auth)
def me(user: User = Depends(get_current_auth)):
    return user
