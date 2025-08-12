from pymongo import AsyncMongoClient
from beanie import init_beanie   
from app.models.task import Task
from app.config.settings import Settings

settings = Settings() 

client: AsyncMongoClient | None = None

async def init_db():
    global client
    client = AsyncMongoClient(settings.mongo_uri, serverSelectionTimeoutMS=5000)
    try:
        await client.admin.command("ping")  # check connection/auth quickly
        await init_beanie(database=client.ToDoDB, document_models=[Task])
        print("\nPing successful, MongoDB connection established\n")

    except Exception as e:
        # ALWAYS close if startup fails, then re-raise so app doesn’t half-start
        if client:
            await client.close()
        client = None
        raise RuntimeError(f"MongoDB/Beanie init failed: {e}") from e
        
async def close_db():
    if client:
        await client.close()