from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
async def all_users():
    return {"message": "List of all users"}

@router.get("/{user_id}")
async def user_by_id(user_id: int):
    return {"message": f"User with ID {user_id}"}

@router.post("/")
async def create_user():
    return {"message": "User created"}

@router.put("/{user_id}")
async def update_user(user_id: int):
    return {"message": f"User with ID {user_id} updated"}

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return {"message": f"User with ID {user_id} deleted"}

