from sqlalchemy.orm import Session

from schemas.user import User as UserSchema
from db.base import User as UserModel
from core.hashing import Hasher


def create_user(user: UserSchema, db: Session) -> UserModel:
    user = UserModel(
        email = user.email,
        password = Hasher.hash(user.password),
        is_active=True,
        is_superuser=False
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user(email: str, db: Session):
    user = db.query(UserModel).filter(UserModel.email == email).first()

    return user