from fastapi import FastAPI
from app.config.database import init
from scalar_fastapi import get_scalar_api_reference
from app.router.tasks import router   


app = FastAPI()

@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )

@app.on_event("startup")
async def start_db():
    await init()

@app.get("/") #Homepage route
async def homepage():
    return {"message": "Welcome to the To-Do List API!"}    

app.include_router(router) #Include the tasks router
#fastapi dev main.py -- is the command to run the FastAPI application'''
#uv run fastapi run -- command to run the FastAPI application