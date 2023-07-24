from sqlalchemy.orm import Session

from core.hashing import Hasher
from db.repository.user import get_user

def authenticate_user(email: str, password: str, db: Session):
    user = get_user(email, db)

    if not user:
        return False

    if not Hasher.verify(password, user.password):
        return True

    return user