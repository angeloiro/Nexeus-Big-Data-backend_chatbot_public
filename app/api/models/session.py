### **app/models/session.py** (Modelo de sesión en Redis o MongoDB)
from pydantic import BaseModel

class Session(BaseModel):
    user_id: str
    step: int
    data: dict