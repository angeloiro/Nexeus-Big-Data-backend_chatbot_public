from fastapi import APIRouter, Depends
from app.services.email_sender import send_email

router = APIRouter()

@router.post("/send")
async def send_budget_email(user_email: str, pdf_path: str):
    send_email(user_email, pdf_path)
    return {"message": "Correo enviado"}