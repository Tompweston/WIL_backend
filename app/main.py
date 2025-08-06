from fastapi import FastAPI
from app.config.database import init
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = FastAPI()

@app.on_event("startup")
async def start_db():
    await init()

@app.get("/") #Homepage route
async def homepage():
    return {"message": "Welcome to the To-Do List API!"}    


#fastapi dev main.py -- is the command to run the FastAPI application'''
#uv run fastapi run -- command to run the FastAPI application