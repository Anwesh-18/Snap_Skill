from fastapi import APIRouter, Depends, HTTPException, status
from schemas.user import UserOut, UserCreate, UserLogin
from core.security import hash_password, verify_password, create_access_token
from db import db

auth = APIRouter()

@auth.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    if await db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    user_dict["role"] = "freelancer"
    result = await db.users.insert_one(user_dict)
    return {
        "id": str(result.inserted_id),  # convert ObjectId to string
        "name": user.name,
        "email": user.email,
        "role": user_dict["role"]
    }

@auth.post("/login")
async def login(user: UserLogin):
    db_user = await db.users.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": db_user["email"]})
    return {"access_token": token, "token_type": "bearer"}