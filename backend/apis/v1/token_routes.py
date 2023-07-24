from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session

from core.security import generate_access_token
from db.session import get_db
from apis.utils.user import authenticate_user
from schemas.token import Token as TokenSchema


router = APIRouter()


@router.post("/token", response_model=TokenSchema, status_code=status.HTTP_200_OK)
def generate_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            detail="Incorect credentials",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    token = generate_access_token(
        data={ "sub": user.email }
    )

    return {"access_token": token, "token_type": "bearer"}