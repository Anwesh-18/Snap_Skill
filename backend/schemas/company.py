from pydantic import BaseModel, EmailStr

# Company part
class CompanyCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "company"

class CompanyLogin(BaseModel):
    email: EmailStr
    password: str

class CompanyOut(BaseModel):
    id: str
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True
