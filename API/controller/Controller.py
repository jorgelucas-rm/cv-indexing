from fastapi import APIRouter


class Controller:

    router = APIRouter(tags=["Home"])

    @router.get("/")
    def hello_world_root():
        return {"Hello world"}
