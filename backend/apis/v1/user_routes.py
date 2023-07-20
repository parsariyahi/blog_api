from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schemas.user import UserShow, User as UserSchema
from db.repository.user import create_user
from db.session import get_db


router = APIRouter()

@router.post("/add", response_model=UserShow, status_code=status.HTTP_201_CREATED)
def register_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = create_user(user, db)
    return new_user