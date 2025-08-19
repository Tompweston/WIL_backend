from fastapi import APIRouter, HTTPException
from app.models.user import User
from typing import List

#places task routes under the /users prefix and tags them as "Tasks" in the API documentation
user_router = APIRouter(prefix="/users", tags=["Users"])    

#CRUD operations for tasks

### NEED TO ADD BETTER ERROR HANDLING FOR 500 and 422 HTTP ERRORS ###

# Create a new user 
@user_router.post("/", response_model=User)
async def create_user(user: User):
    await user.create()
    return user

# Get all users
@user_router.get("/", response_model=List[User])
async def get_all_users():
    users = await User.find_all().to_list()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

# Get a user by ID
@user_router.get("/{id}", response_model=User)
async def get_user(id: str):
    user = await User.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Delete a user by ID
@user_router.delete("/{id}")
async def delete_user(id: str):
    user = await User.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await user.delete()
    return {"message": "User deleted"}
