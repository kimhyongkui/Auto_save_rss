from fastapi import APIRouter
from app.auth import get_access_token, get_auth_url

router = APIRouter()


@router.get("/auth-url", tags=["인증관련"])
def auth_url():
    result = get_auth_url()
    return result


@router.get("/access-token", tags=["인증관련"])
def access_token(auth_code):
    result = get_access_token(auth_code)
    return result
