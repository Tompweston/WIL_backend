from pydantic_settings import BaseSettings


# this file is used to load environment variables and set up the database connection
class Settings(BaseSettings): # MongoDB connection settings
    model_config = {"env_file": ".env"}
    mongo_uri: str