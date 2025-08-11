from pymongo import AsyncMongoClient
from beanie import init_beanie   
from app.models.task import Task
from app.config.settings import Settings

settings = Settings() 

client: AsyncMongoClient | None = None

async def init():
    mongo_uri = (
    f"mongodb+srv://{settings.mongo_username}:{settings.mongo_password}@{settings.mongo_server}"
    )
    global client
    client = AsyncMongoClient(mongo_uri)
    await client.admin.command("ping")  # quick “is Mongo alive?”
    print("\nPing Successful,MongoDB connection established\n")
    await init_beanie(database=client.ToDoDB, document_models=[Task])

async def close():
    if client:
        await client.close()