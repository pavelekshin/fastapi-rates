from src.exceptions import (
    BadRequestError,
    ExternalError,
    NotAuthenticatedError,
    PermissionDeniedError,
)
from src.exchange.constants import ErrorCode


class InvalidResponseError(ExternalError):
    error_code = ErrorCode.INVALID_RESPONSE


class InvalidTokenError(NotAuthenticatedError):
    error_code = ErrorCode.INVALID_TOKEN


class NotAuthorizedOperationError(PermissionDeniedError):
    error_code = ErrorCode.AUTHORIZATION_FAILED


class ConvertOperationError(BadRequestError):
    error_code = ErrorCode.CONVERT_OPERATION_FAILED
