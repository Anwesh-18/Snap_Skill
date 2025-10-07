from pydantic import BaseModel, EmailStr

# CLient part
class ClientCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "client"

class ClientLogin(BaseModel):
    email: EmailStr
    password: str

class ClientOut(BaseModel):
    id: str
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True
