from pymongo import AsyncMongoClient
from beanie import init_beanie   
from app.models.task import task
from app.config.settings import Settings

settings = Settings() 
async def init():
    # builds the MongoDB URI directly using settings variables
    mongo_uri = (
        f"mongodb+srv://{settings.mongo_username}:{settings.mongo_password}@{settings.mongo_server}"
    )
    client = AsyncMongoClient(mongo_uri)
    await init_beanie(database=client.ToDoDB, document_models=[task])