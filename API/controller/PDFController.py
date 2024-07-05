from fastapi import APIRouter, UploadFile
from service.PDFAnalysisService import PDFAnalysisService
from service.PDFCRUDService import PDFCRUDService


class PDFController:

    router = APIRouter(tags=["PDF"])

    @router.get("/pdf-management/{name}")
    async def get_pdf(name):
        return PDFCRUDService.get_pdf(name)

    @router.post("/pdf-management")
    async def upload_pdf(file: UploadFile):
        return PDFCRUDService.upload_pdf(file)

    @router.delete("/pdf-management/{name}")
    async def delete_pdf(name):
        return PDFCRUDService.delete_pdf(name)

    @router.get("/pdf-analysis/{name}")
    async def analyse_pdf(name):
        return PDFAnalysisService.analyse_pdf(name)
