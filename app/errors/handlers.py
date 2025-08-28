from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


# Handles 404 HTTP exceptions
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={
            "error": exc.detail,
            "path": str(request.url),
        },
    )


# Handles HTTP exceptions
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "HTTP error occurred",
            "path": str(request.url),
        },
    )

# Handles FastAPI request validation errors (422)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation failed",
            "path": str(request.url),
        },
    )

# Handles server exceptions (500)
async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "path": str(request.url),
        },
    )

