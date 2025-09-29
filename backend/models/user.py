from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def _get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr
    name: Optional[str] = None
    password: str
    role: str = "freelancer"

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

class UpdateUserModel(BaseModel):
    email: Optional[EmailStr]
    name: Optional[str]
    password: Optional[str]
    role: Optional[str]

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}