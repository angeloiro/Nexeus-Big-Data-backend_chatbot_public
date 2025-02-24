from fastapi import APIRouter, Depends
from app.schemas.budget_schema import BudgetRequest
from app.services.budget_service import calculate_budget

router = APIRouter()

@router.post("/calculate")
async def get_budget(data: BudgetRequest):
    budget = calculate_budget(data)
    return {"message": "Presupuesto generado", "budget": budget}
