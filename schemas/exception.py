from fastapi import Request
from starlette.responses import JSONResponse

from config.errcode import RJBaseException


async def exception_handler(request: Request, exc: RJBaseException):
    return JSONResponse(status_code=exc.errcode, content={"errmsg": exc.errmsg})
