class RJBaseException(Exception):
    def __init__(self, errmsg: str, errcode: int = 500):
        self.errmsg = errmsg
        self.errcode = errcode


class UnauthorizedException(RJBaseException):
    def __init__(self, errmsg: str = "Could not validate credentials"):
        self.errmsg = errmsg
        self.errcode = 401


class BadRequestException(RJBaseException):
    def __init__(self, errmsg: str):
        self.errmsg = errmsg
        self.errcode = 400


class InternalServerErrorException(RJBaseException):
    def __init__(self, errmsg: str):
        self.errmsg = errmsg
        self.errcode = 500

class NotFoundException(RJBaseException):
    def __init__(self, errmsg: str):
        self.errmsg = errmsg
        self.errcode = 404
