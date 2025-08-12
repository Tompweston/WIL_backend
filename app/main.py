from fastapi import FastAPI
from app.config.database import init_db, close_db
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi.middleware.cors import CORSMiddleware
from scalar_fastapi import get_scalar_api_reference
from app.router.tasks import tasks_router   
from app.router.users import user_router
# lifespan event to initialize and close the database connection
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await init_db()
    try:
        yield
    finally:
        await close_db()

app = FastAPI(title="Todo API", lifespan=lifespan)

# API documentation formatting
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )


# Homepage route
@app.get("/")
async def homepage():
    return {"message": "Welcome to the To-Do List API!"}    

app.include_router(tasks_router)  # Include the tasks router
app.include_router(user_router)  # Include the users router

# fastapi dev main.py -- is the command to run the FastAPI application
# uv run fastapi run -- command to run the FastAPI application