### **app/services/email_sender.py** (Envío de correos SMTP)
import smtplib
from email.message import EmailMessage

def send_email(to_email, pdf_path):
    msg = EmailMessage()
    msg["Subject"] = "Tu presupuesto personalizado"
    msg["From"] = "tuemail@example.com"
    msg["To"] = to_email
    with open(pdf_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=pdf_path)
    with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
        server.login("tuemail@example.com", "tupassword")
        server.send_message(msg)