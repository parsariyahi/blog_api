from typing import Any, Dict, Optional
from fastapi import HTTPException, status


class CredentailError(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail: Any = "the credentials is not valid",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)