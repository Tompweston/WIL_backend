from fastapi import FastAPI
from app.config.database import init_db, close_db
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi.middleware.cors import CORSMiddleware
from scalar_fastapi import get_scalar_api_reference
from app.router.tasks import tasks_router   
from app.router.users import user_router
from app.config.settings import Settings

settings = Settings()  # Initialize settings

# lifespan event to initialize and close the database connection
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await init_db()
    try:
        yield
    finally:
        await close_db()

# Create FastAPI app instance
app = FastAPI(title="Todo API", lifespan=lifespan)

# API scalar documentation formatting
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )

# CORS middleware to allow cross-origin requests

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.vite_dev_server_url.split(","),  # Allow origins from settings
    allow_credentials=True,  # set to False if not using cookies/auth via cookies
    allow_methods=["*"],
    allow_headers=["*"],
)


# Homepage route
@app.get("/")
async def homepage():
    return {"message": "Welcome to the To-Do List API!"}    

# Include Routes
app.include_router(tasks_router)  # Include the tasks router
app.include_router(user_router)  # Include the users router

# fastapi dev main.py -- is the command to run the FastAPI application
# uv run fastapi run -- command to run the FastAPI application