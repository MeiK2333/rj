from pydantic import BaseModel


class UserInfo(BaseModel):
    rating: int
    titlePhoto: str
    handle: str
    avatar: str
    maxRating: int

    class Config:
        orm_mode = True
