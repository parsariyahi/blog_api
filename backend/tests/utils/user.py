from sqlalchemy.orm import Session

from core.config import settings
from db.repository.user import  create_user
from schemas.user import User as UserSchema

def create_random_user(db: Session, email=settings.TEST_USER_EMAIL, password=settings.TEST_USER_PASSWORD):
    user = UserSchema(
        email=email,
        password=password,
    )
    user = create_user(user, db)

    return user


def force_authentication(client, user) -> str:
    response = client.post("/auth/token", data=user)

    token = response.json()["access_token"]

    return token

