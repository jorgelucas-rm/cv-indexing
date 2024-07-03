import os
import shutil

from dotenv import load_dotenv
from fastapi import UploadFile
from fastapi.responses import FileResponse
from service.ExeptionService import CustomException, PDFErrorType

load_dotenv()
directory = os.getenv("file_path")


class PDFCRUDService:

    def get_pdf(name: str):
        file_path = os.path.join(directory, name)

        headers = {"Content-Disposition": f"inline; filename={name}"}

        if not os.path.exists(file_path):
            return CustomException(PDFErrorType.FILE_NOT_FOUND)

        return FileResponse(file_path, media_type="application/pdf", headers=headers)

    def upload_pdf(file: UploadFile):
        file_path = os.path.join(directory, file.filename)

        if os.path.exists(file_path):
            return CustomException(PDFErrorType.FILE_ALREDY_EXIST)

        with open(file_path, "wb") as file_object:
            shutil.copyfileobj(file.file, file_object)
            return {"filename": file.filename}

    def delete_pdf(name: str):
        file_path = os.path.join(directory, name)

        if not os.path.exists(file_path):
            return CustomException(PDFErrorType.FILE_NOT_FOUND)
        else:
            os.remove(file_path)
            return {"detail": "File deleted successfully"}
