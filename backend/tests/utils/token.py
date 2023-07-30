from jose import jwt

from core.config import settings

def verify_jwt_token_sub(sub: dict, token: str) -> bool:
    decoded_token = jwt.decode(token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM]) 

    token_sub = decoded_token.get("sub", None)

    if not token_sub:
        return False

    if sub != token_sub:
        return False

    return True