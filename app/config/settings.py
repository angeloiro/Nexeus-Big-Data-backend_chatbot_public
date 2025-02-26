### **app/config/settings.py** (Configuración y variables de entorno)
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_USER = os.getenv("SMTP_USER", "email@example.com")
SMTP_PASS = os.getenv("SMTP_PASS", "password")
