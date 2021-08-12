from sqlalchemy import Column, Integer, String, ForeignKey

from models.db import Base
from sqlalchemy.orm import relationship, backref


class UserInfo(Base):
    __tablename__ = "codeforces_userinfo"
    id = Column(Integer, primary_key=True, index=True)

    handle = Column(String(length=64), unique=True, index=True)
    rating = Column(Integer)
    maxRating = Column(Integer)
    titlePhoto = Column(String(length=512))
    avatar = Column(String(length=512))

    password = Column(String(length=256))
    api_key = Column(String(length=64))
    secret = Column(String(length=64))

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref=backref("codeforces", uselist=False))
