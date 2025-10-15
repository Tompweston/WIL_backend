from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from scalar_fastapi import get_scalar_api_reference
from app.router.tasks import tasks_router
from app.config.settings import Settings
from app.config.database import lifespan
from app.errors.handlers import (
    http_exception_handler,
    validation_exception_handler,
    unhandled_exception_handler,
    not_found_exception_handler,
)
from fastapi.exceptions import RequestValidationError


settings = Settings()  # Initialize settings

# Initialize the FastAPI application with lifespan context manager & Create FastAPI app instance
app = FastAPI(title="Todo API", lifespan=lifespan)


# API scalar documentation formatting
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )


@app.get("/")
async def root_path():
    return {"message": "Backend is up and running, you can now close this tab!"}


# Include Routes
app.include_router(tasks_router)  # Include the tasks router

# Include Exception Handlers for routes
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)
app.add_exception_handler(HTTPException, not_found_exception_handler)

# fastapi dev main.py -- is the command to run the FastAPI application
# uv run fastapi run -- command to run the FastAPI application
