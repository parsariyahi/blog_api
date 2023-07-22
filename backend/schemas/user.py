from pydantic import BaseModel, EmailStr, Field, ConfigDict

class User(BaseModel):
    email: EmailStr
    # password: Field(..., min_length=4)
    password: str

class UserShow(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

    # class Config:
    #     from_attributes = True