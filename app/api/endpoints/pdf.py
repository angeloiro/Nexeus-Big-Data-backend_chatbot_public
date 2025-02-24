### **app/api/endpoints/pdf.py** (Generación de PDF)
from fastapi import APIRouter, Depends
from app.services.pdf_generator import generate_pdf

router = APIRouter()

@router.get("/generate/{user_id}")
async def generate_user_pdf(user_id: str):
    pdf_path = generate_pdf(user_id)
    return {"message": "PDF generado", "pdf_path": pdf_path}
