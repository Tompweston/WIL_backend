from pydantic_settings import BaseSettings

# this file is used to load environment variables 
class Settings(BaseSettings): 
    model_config = {"env_file": ".env"}
    mongo_uri: str # MongoDB connection URI
    allowed_servers: list[str]  # List of allowed server origins