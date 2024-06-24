from fastapi import FastAPI
from controller.Controller import Controller
from controller.UserController import UserController
from controller.PDFController import PDFController
app = FastAPI()

app.include_router(Controller.router)
app.include_router(UserController.router)
app.include_router(PDFController.router)