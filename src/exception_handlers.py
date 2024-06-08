from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.exceptions import ErrorItem, ErrorResponse
from src.exchange.exceptions import (
    ConvertOperationError,
    InvalidResponseError,
    InvalidTokenError,
    NotAuthorizedOperationError,
)


async def exchange_auth_failed_exception_handler(
    request: Request,
    exception: [
        InvalidTokenError,
    ],
):
    error = ErrorItem(
        error_code=exception.error_code,
        error_message=exception.error_message,
        error_detail=exception.error_detail,
    )
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=jsonable_encoder(
            ErrorResponse(error=error), exclude_none=True, exclude_unset=True
        ),
    )


async def exchange_permission_denied_exception_handler(
    request: Request,
    exception: [
        NotAuthorizedOperationError,
    ],
):
    error = ErrorItem(
        error_code=exception.error_code,
        error_message=exception.error_message,
        error_detail=exception.error_detail,
    )
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=jsonable_encoder(
            ErrorResponse(error=error), exclude_none=True, exclude_unset=True
        ),
    )


async def exchange_bad_response_failed_exception_handler(
    request: Request, exception: [InvalidResponseError]
):
    error = ErrorItem(
        error_code=exception.error_code,
        error_message=exception.error_message,
        error_detail=exception.error_detail,
    )
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            ErrorResponse(error=error), exclude_none=True, exclude_unset=True
        ),
    )


async def convert_failed_exception_handler(
    request: Request, exception: [ConvertOperationError]
):
    error = ErrorItem(
        error_code=exception.error_code,
        error_message=exception.error_message,
        error_detail=exception.error_detail,
    )
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            ErrorResponse(error=error), exclude_none=True, exclude_unset=True
        ),
    )


async def request_validation_exception_handler(
    request: Request, exception: [RequestValidationError]
):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {"detail": exception.errors(), "body": exception.body}
        ),
    )


def register_error_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        RequestValidationError, request_validation_exception_handler
    )
    app.add_exception_handler(
        InvalidResponseError, exchange_bad_response_failed_exception_handler
    )
    app.add_exception_handler(InvalidTokenError, exchange_auth_failed_exception_handler)
    app.add_exception_handler(
        NotAuthorizedOperationError, exchange_permission_denied_exception_handler
    )
    app.add_exception_handler(ConvertOperationError, convert_failed_exception_handler)
