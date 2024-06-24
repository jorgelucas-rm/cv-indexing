from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

class UpdateUser(BaseModel):
    name: Optional[str]