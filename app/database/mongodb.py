### **app/database/mongodb.py** (Conexión con MongoDB)
from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URI)
db = client["chatbot"]

def get_user_collection():
    return db["users"]