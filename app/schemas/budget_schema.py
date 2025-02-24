### **app/schemas/budget_schema.py** (Validación de datos para presupuestos)
from pydantic import BaseModel

class BudgetRequest(BaseModel):
    hours: int
    rate: float

def calculate_budget(data: BudgetRequest):
    return data.hours * data.rate
