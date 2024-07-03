from database.UserDatabase import db
from model.User import UpdateUser
from service.ExeptionService import CustomException, UserErrorType


class UserService:

    def list_users():
        return db

    def get_user(id: int):
        for User in db:
            if User.id == id:
                return User

        return CustomException(UserErrorType.USER_NOT_FOUND)

    def create_user(newUser):
        for User in db:
            if newUser == User:
                return CustomException(UserErrorType.USER_ALREDY_EXIST)

        db.append(newUser)
        return {"id": newUser.id}

    def delete_user(id: int):
        for User in db:
            if User.id == id:
                db.remove(User)
                return {"detail": "User deleted successfully"}

        return CustomException(UserErrorType.USER_NOT_FOUND)

    def uptade_user(user_update: UpdateUser, id: int):
        for User in db:
            if User.id == id:
                if user_update.name is not None:
                    User.name = user_update.name
                    return User

        return CustomException(UserErrorType.USER_NOT_FOUND)
