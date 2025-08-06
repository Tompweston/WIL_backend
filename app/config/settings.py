from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings): # MongoDB connection settings
    model_config = {"env_file": ".env"}
    mongo_username: str
    mongo_password: str
    mongo_server: str


    