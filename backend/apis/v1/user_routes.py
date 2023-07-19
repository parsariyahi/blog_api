from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.user import User as UserSchema
from db.repository.user import create_user
from db.session import get_db


router = APIRouter()

@router.post("/")
def register(user: UserSchema, db: Session = Depends(get_db)):
    new_user = create_user(user, db)
    return new_user