from pymongo import AsyncMongoClient
from beanie import init_beanie   
from app.models.task import Task
from app.models.user import User
from app.config.settings import Settings

# Initialize settings
settings = Settings() 

# Global MongoDB client
client: AsyncMongoClient | None = None

# Initialize the database, ensure connection is established. Closes connection if it fails.
### NEED TO ADD MORE ROBUST ERROR HANDLING FOR CONNECTION ISSUES ###


async def init_db():
    global client
    client = AsyncMongoClient(settings.mongo_uri, serverSelectionTimeoutMS=5000)
    try:
        await client.admin.command("ping")  # check connection/auth quickly
        await init_beanie(database=client.ToDoDB, document_models=[Task, User])
        print("\nPing successful, MongoDB connection established\n")
    except Exception as e:
        if client:
            await client.close()
        client = None
        raise RuntimeError(f"MongoDB/Beanie init failed: {e}") from e
    
# Close the database connection
async def close_db():
    if client:
        await client.close()