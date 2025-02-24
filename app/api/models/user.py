from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    id: str
    name: str
    email: EmailStr
    requirements: list[str]
    created_at: datetime