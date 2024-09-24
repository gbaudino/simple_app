from pydantic import BaseModel, EmailStr

class LeadBase(BaseModel):
    name: str
    surname: str
    email: EmailStr

class LeadCreate(LeadBase):
    pass

class LeadUpdate(BaseModel):
    email: EmailStr

class LeadInDB(LeadBase):
    id: int

    class Config:
        from_attributes = True
