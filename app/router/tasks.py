from fastapi import APIRouter, HTTPException
from app.models.task import Task, TaskUpdate
from app.models.session import session
from beanie import PydanticObjectId
from typing import List
from bson import ObjectId
from datetime import datetime

#places task routes under the /tasks prefix and tags them as "Tasks" in the API documentation
tasks_router = APIRouter( tags=["Tasks"] )    


# Create a new task
@tasks_router.post("/", response_model=Task)
async def create_task(task: Task):
    await task.create()
    return task

# Get all tasks
@tasks_router.get("/", response_model=List[Task])
async def get_all_tasks():
    tasks = await Task.find_all().to_list()
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found")
    return tasks

# Get tasks by user ID
@tasks_router.get("/{user_id}", response_model=List[Task])
async def get_tasks_by_user_id(user_id: str):
    user_obj_id = PydanticObjectId(user_id)
    print(f"\nUser ID: {user_id}\n\n")
    print(f"\nUser ID Comparison: {user_id_comparison}\n\n")
    valid_session = await session.find({"userId": user_id_comparison}).to_list()
    session_dicts = [
    {
        "id": str(s.id),
        "revision_id": s.revision_id,
        "expiresAt": s.expiresAt.isoformat(),
        "user_id": str(s.user_id)
    }
    for s in valid_session
    ]

    print(f"\nSession Dicts: {session_dicts}\n\n")
    print(f"\nValid Document: {valid_session}\n\n")

    if not valid_session:
        raise HTTPException(status_code=401, detail="Unauthorized")

    tasks = await Task.find({"user_id": user_id}).to_list()
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this user")
    return tasks
    

# Get a task by ID
@tasks_router.get("/{id}", response_model=Task)
async def get_task(id: str):
    task = await Task.get(id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update a task by ID
@tasks_router.patch("/{id}", response_model=Task)
async def update_task(id: str, task_data: TaskUpdate):
    task = await Task.get(id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    recived = task_data.dict(exclude_unset=True)
    for key, value in recived.items():
        setattr(task, key, value)
    await task.save()
    return task

# Delete a task by ID
@tasks_router.delete("/{id}")
async def delete_task(id: str):
    task = await Task.get(id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    await task.delete()
    return {"message": "Task deleted"}

# Delete all tasks
@tasks_router.delete("/")
async def delete_all_tasks():
    await Task.delete_all()
    return {"message": "All tasks deleted"}