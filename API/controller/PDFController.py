from fastapi import APIRouter, UploadFile
from service.PDFCRUDService import PDFService

class PDFController:

    router = APIRouter()

    @router.get("/pdf-management/{name}")
    async def get_pdf(name):
        return PDFService.get_pdf(name)

    @router.post("/pdf-management")
    async def upload_pdf(file: UploadFile):
        return PDFService.upload_pdf(file)

    @router.delete("/pdf-management/{name}")
    async def delete_pdf(name):
        return PDFService.delete_pdf(name)