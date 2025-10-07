from pymongo import AsyncMongoClient
from beanie import init_beanie   
from app.models.task import Task
from app.models.user import user
from app.models.session import session
from app.config.settings import Settings
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI


# Initialize settings
settings = Settings() 

# Initialize the database, ensure connection is established. Closes connection if it fails.
### NEED TO ADD MORE ROBUST ERROR HANDLING FOR CONNECTION ISSUES ###

# Lifespan event to initialize and close the database connection (moved all logic and references from main to db file)
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    client = AsyncMongoClient(settings.mongo_uri, serverSelectionTimeoutMS=5000)
    try:
        await client.admin.command("ping")  # check connection/auth quickly
        await init_beanie(database=client.ToDoDB, document_models=[Task, user, session])
        print("\nPing successful, MongoDB connection established\n")
    except Exception as e:
        if client:
            await client.close()
        client = None
        raise RuntimeError(f"MongoDB/Beanie init failed: {e}") from e
    try:
        yield
    finally:
        if client:
            await client.close()

