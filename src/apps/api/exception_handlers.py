import decimal
import json
import logging
import typing

from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.apps.api.models import ErrorResponseModel
from src.core.shared.exceptions import DomainError

logger = logging.getLogger(__name__)


class JSONResponseEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)

        if isinstance(obj, (tuple, set)):
            return [i for i in obj]

        return super(JSONResponseEncoder, self).default(obj)


class JSONDecimalAndTupleResponse(JSONResponse):
    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
            cls=JSONResponseEncoder,
        ).encode("utf-8")


async def domain_exception_handler(
    request: Request,
    exc: DomainError,
):
    return JSONDecimalAndTupleResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ErrorResponseModel(code=str(exc), details=exc.details).model_dump(),
    )


async def internal_exception_handler(
    request: Request, exc: Exception
) -> JSONDecimalAndTupleResponse:
    logger.exception(exc)
    return JSONDecimalAndTupleResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponseModel(code="INTERNAL").model_dump(),
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.exception(exc)
    try:
        errors = exc.errors()
    except RuntimeError:
        # Непонятная ошибка от pydantic
        errors = exc.raw_errors

    return JSONDecimalAndTupleResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ErrorResponseModel(code="VALIDATION_ERROR", details=errors).model_dump(),
    )
