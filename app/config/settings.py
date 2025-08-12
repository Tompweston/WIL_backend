from pydantic_settings import BaseSettings

class Settings(BaseSettings): # MongoDB connection settings
    model_config = {"env_file": ".env"}
    mongo_uri: str