### **app/services/budget_service.py** (Lógica de cálculo de presupuesto)
from app.schemas.budget_schema import BudgetRequest

def calculate_budget(data: BudgetRequest):
    return data.hours * data.rate