### **app/services/pdf_generator.py** (Generación de PDF)
from reportlab.pdfgen import canvas

def generate_pdf(user_id):
    pdf_path = f"presupuesto_{user_id}.pdf"
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, f"Presupuesto para Usuario ID: {user_id}")
    c.save()
    return pdf_path