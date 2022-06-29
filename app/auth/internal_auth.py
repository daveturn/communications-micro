from fastapi import HTTPException, Header, status
from app.core.config import settings


def check_internal_auth(authorization: str = Header(...)) -> None:
    if authorization == settings.INTERNAL_API_KEY:
        return

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Authorization header is not valid",
    )
