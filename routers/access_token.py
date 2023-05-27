from fastapi import APIRouter
from app.auth import get_access_token, get_auth_code

router = APIRouter()


@router.get("/access-token")
def access_token(auth_code):
    result = get_access_token(auth_code)
    return result


@router.get("/auth-code")
def auth_code():
    result = get_auth_code()
    return result
