from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    email: EmailStr
    password: Field(..., min_length=4)