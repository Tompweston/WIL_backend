from fastapi import APIRouter, HTTPException
from app.models.task import Task, TaskUpdate
from app.models.session import session
from beanie import PydanticObjectId
from typing import List
from bson import ObjectId
from datetime import datetime
from fastapi import FastAPI, Header
from typing import Annotated


# Authenticates user based on session validity and expiry
async def authenticate_user(user_id: str, type: str) -> bool:
    print ("\nAUTHENTICATION\n----------------")

    print("   Authenticating user...", user_id)
    user_obj_id = PydanticObjectId(user_id)
    valid_session = await session.find({"userId": user_obj_id}).to_list()
    session_dicts = [
    {
        "id": str(s.id),
        "revision_id": s.revision_id,
        "expiresAt": s.expiresAt.isoformat(),
        "user_id": str(s.user_id)
    }
    for s in valid_session
    ]

    if not valid_session:
        print("   No valid session found.")
        return False
    
    if valid_session:
        for s in session_dicts:
            exp_time = datetime.fromisoformat(s["expiresAt"])
            if exp_time < datetime.utcnow():
                print("   Session expired at", exp_time)
                await session.get(ObjectId(s["id"])).delete()
                return False
            else:
                print("   Session is not expired and valid until", exp_time)
        print("   User authenticated successfully for", type, "route")
        print("----------------\n")
    return True

#places task routes under the /tasks prefix and tags them as "Tasks" in the API documentation
tasks_router = APIRouter( prefix="/tasks", tags=["Tasks"] )
#==================================================================================================================
# Create a new task
@tasks_router.post("/", response_model=Task)
async def create_task(task: Task, userID: Annotated[str, Header()] = None):
    user_id = userID
    validated = await authenticate_user(user_id, "create")
    if not validated:
        raise HTTPException(status_code=401, detail="Unauthorized")
        return {"message": "Not Authenticated"}
    if validated:
        print("POST A NEW TASK HEADER:", user_id, "\n")
        task.user_id = user_id
        await task.create()
        return task

#==================================================================================================================

#Get tasks by user ID
@tasks_router.get("/", response_model=List[Task])
async def get_tasks_by_user_id(userID: Annotated[str, Header()] = None):
    user_id = userID
    validated = await authenticate_user(user_id, "read")
    print("GET ALL TASKS HEADER:", user_id, "\n")
    if not validated:
        raise HTTPException(status_code=401, detail="Unauthorized")
        return {"message": "Not Authenticated"}
    if validated:
        tasks = await Task.find({"user_id": user_id}).to_list()
        if not tasks:
            raise HTTPException(status_code=404, detail="No tasks found for this user")
        return tasks

#==================================================================================================================

# Update a task by ID
@tasks_router.patch("/{id}", response_model=Task)
async def update_task(id: str, task_data: TaskUpdate, userID: Annotated[str, Header()] = None):
    user_id = userID
    validated = await authenticate_user(user_id, "update")
    print("\nUPDATE TASK HEADER:", user_id, "\n")
    if not validated:
        raise HTTPException(status_code=401, detail="Unauthorized")
        return {"message": "Not Authenticated"}
    if validated:
        task = await Task.get(id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        recived = task_data.dict(exclude_unset=True)
        for key, value in recived.items():
            setattr(task, key, value)
        await task.save()
        return task

#==================================================================================================================

# Delete a task by ID
@tasks_router.delete("/{id}")
async def delete_task(id: str, userID: Annotated[str, Header()] = None):
    user_id = userID
    validated = await authenticate_user(user_id, "delete")
    print("\nDELETE SINGLE TASK HEADER:", user_id, "\n")
    if not validated:
        raise HTTPException(status_code=401, detail="Unauthorized")
        return {"message": "Not Authenticated"}
    if validated:
        task = await Task.get(id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        await task.delete()
        return {"message": "Task deleted"}

#==================================================================================================================

#delete tasks by user ID
@tasks_router.delete("/")
async def delete_tasks_by_user_id(userID: Annotated[str, Header()] = None):
    user_id = userID
    print("\nDELETE ALL TASKS HEADER:", user_id, "\n")
    validated = await authenticate_user(user_id, "delete all")
    if not validated:
        print("Not Authenticated delete")
        raise HTTPException(status_code=401, detail="Unauthorized")
        return {"message": "Not Authenticated"}
    if validated:
        await Task.find({"user_id": user_id}).delete_many()
        return {"message": f"All tasks for user {user_id} deleted"}

#================================================================================================================== 

#ADMIN ROUTES - not exposed in main app.py
# Get all tasks (admin only)
@tasks_router.get("/all", response_model=List[Task])
async def get_all_tasks():
    tasks = await Task.find_all().to_list()
    return tasks
# Delete all tasks (admin only)
@tasks_router.delete("/all")
async def delete_all_tasks():
    await Task.find_all().delete_many()
    return {"message": "All tasks deleted"}