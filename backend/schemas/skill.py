from pydantic import BaseModel, EmailStr

# Skill part
class SkillCreate(BaseModel):
    name: str
    description: str