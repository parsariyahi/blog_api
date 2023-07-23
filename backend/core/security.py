from datetime import datetime, timedelta
from typing import Optional
from jose import jwt

from core.config import settings


def generate_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    jwt_token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return jwt_token