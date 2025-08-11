from fastapi import APIRouter, HTTPException
from app.models.task import Task, TaskUpdate
from typing import List

#places task routes under the /tasks prefix and tags them as "Tasks" in the API documentation
router = APIRouter(prefix="/tasks", tags=["Tasks"])    

#CRUD operations for tasks
# Create a new task

@router.post("/", response_model=Task)
async def create_task(task: Task):
    await task.create()
    return task

# Get all tasks
@router.get("/", response_model=List[Task])
async def get_all_tasks():
    tasks = await Task.find_all().to_list()
    return tasks

# Get a task by ID
@router.get("/{id}", response_model=Task)
async def get_task(id: str):
    task = await Task.get(id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update a task by ID 
@router.patch("/{id}", response_model=Task)
async def update_task(id: str, task_data: TaskUpdate):
    task = await Task.get(id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.description = task_data.description
    task.completed = task_data.completed
    await task.save()
    return task

# Delete a task by ID
@router.delete("/{id}")
async def delete_task(id: str):
    task = await Task.get(id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    await task.delete()
    return {"message": "Task deleted"}


    