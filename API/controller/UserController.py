from fastapi import APIRouter
from model.User import User, UpdateUser
from service.UserService import UserService


class UserController:

    router = APIRouter()

    @router.get("/user-management/users")
    async def get_users():
        return UserService.list_users()
    
    @router.get("/user-management/users/{id}")
    async def get_user(id: int):
        return UserService.get_user(id)
    
    @router.post("/user-management/users")
    async def create_user(user: User):
        return UserService.create_user(user)
    
    @router.delete("/user-management/users/{id}")
    async def delete_user(id: int):
        return UserService.delete_user(id)
        
    @router.put("/user-management/users/{id}")
    async def update_user(user_update: UpdateUser, id: int):
        return UserService.uptade_user(user_update, id)
