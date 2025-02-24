from pydantic import BaseModel

class Budget(BaseModel):
    user_id: str
    hours: int
    rate: float
    total: float