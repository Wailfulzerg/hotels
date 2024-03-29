import re


class BaseError(Exception):
    def __init__(self, message: str = None):
        self.message = message


class InternalError(BaseError):
    pass


class DomainError(BaseError):
    def __init__(self, message: str = None, details=None):
        self.message = message
        self.details = details

    def __str__(self):
        s = re.sub(r"Error$", "", self.__class__.__name__)
        return "".join(["_" + c if c.isupper() else c.upper() for c in s]).lstrip("_")


class DatesNotAvailableError(DomainError):
    pass
