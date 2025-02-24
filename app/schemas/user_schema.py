### **app/schemas/user_schema.py** (Validación de datos con Pydantic)
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    requirements: list[str]