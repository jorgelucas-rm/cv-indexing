from controller.Controller import Controller
from controller.PDFController import PDFController
from controller.UserController import UserController
from fastapi import FastAPI

app = FastAPI()

app.include_router(Controller.router)
app.include_router(UserController.router)
app.include_router(PDFController.router)
