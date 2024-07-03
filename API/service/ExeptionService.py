from enum import Enum

from fastapi import HTTPException


class PDFErrorType(Enum):
    FILE_NOT_FOUND = (404, "File Not Found")
    FILE_ERROR = (400, "File Error")
    FILE_ALREDY_EXIST = (400, "File Alredy Exist")


class UserErrorType(Enum):
    USER_NOT_FOUND = (404, "User Not Found")
    USER_ERROR = (400, "User Error")
    USER_ALREDY_EXIST = (400, "User Alredy Exist")


class CustomException(HTTPException):
    def __init__(self, error_type: any, detail=None):
        self.error_code = error_type.value[0]
        self.error_type = error_type.value[1]
        self.detail = detail or self.error_type
        super().__init__(status_code=self.error_code, detail=f": {self.detail}")

    def __str__(self):
        return f"{self.error_code} {self.error_type}: {self.detail}"
