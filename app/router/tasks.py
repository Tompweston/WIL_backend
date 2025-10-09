from fastapi import APIRouter, HTTPException
from app.models.task import Task, TaskUpdate
from typing import List

#places task routes under the /tasks prefix and tags them as "Tasks" in the API documentation
tasks_router = APIRouter(prefix="/tasks", tags=["Tasks"])    

#CRUD operations for tasks
# Showed me how to change http responses, something that will be addressed later 
#responses={
    #422: {"description": "Validation Error"}, #=
    #500: {"description": "Internal Server Error"}
#}

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
    received = task_data.dict(exclude_unset=True)
    for key, value in received.items():
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