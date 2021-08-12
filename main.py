from fastapi import FastAPI

from config.errcode import RJBaseException
from platforms.codeforces.view import router as cf_router
from schemas.exception import exception_handler
from views.auth import router as auth_router

app = FastAPI()
app.add_exception_handler(RJBaseException, exception_handler)
app.include_router(auth_router)
app.include_router(cf_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
