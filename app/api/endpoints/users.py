### **app/api/endpoints/users.py** (Manejo de usuarios)
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user_schema import UserCreate
from app.database.mongodb import get_user_collection
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.post("/create")
async def create_user(user: UserCreate, users_collection=Depends(get_user_collection)):
    user_dict = user.dict()
    user_dict["created_at"] = datetime.utcnow()
    result = await users_collection.insert_one(user_dict)
    return {"message": "Usuario creado", "user_id": str(result.inserted_id)}
