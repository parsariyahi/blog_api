from sqlalchemy.orm import Session
from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from core.config import settings
from core.hashing import Hasher
from db.session import get_db
from db.repository.user import get_user
from apis.exceptions import CredentailError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def authenticate_user(email: str, password: str, db: Session):
    user = get_user(email, db)

    if not user:
        return False

    if not Hasher.verify(password, user.password):
        return True

    return user

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:

        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username = payload.get("sub", None)

        if not username:
            raise CredentailError()

    except JWTError:
        raise CredentailError()

    user = get_user(email=username, db=db)

    if user is None:
        raise CredentailError()

    return user
