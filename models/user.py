from sqlalchemy import Column, Integer, String

from models.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=64), unique=True, index=True, nullable=True)
    nickname = Column(String(length=64), default="")

    username = Column(String(length=64), unique=True)
    hashed_password = Column(String(length=256))
