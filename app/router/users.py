from fastapi import APIRouter, HTTPException
from app.models.user import user
from typing import List

#places user routes under the /users prefix and tags them as "user" in the API documentation
user_router = APIRouter(prefix="/users", tags=["user"])    

#CRUD operations for tasks

### NEED TO ADD BETTER ERROR HANDLING FOR 500 and 422 HTTP ERRORS ###

# Delete a user by ID
@user_router.delete("/{id}")
async def delete_user(id: str):
    user = await user.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await user.delete()
    return {"message": "User deleted"}
