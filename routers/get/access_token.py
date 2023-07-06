from fastapi import APIRouter
from app.auth import get_access_token, get_auth_url

router = APIRouter(tags=["인증관련"])


@router.get("/auth-url")
def auth_url():
    result = get_auth_url()
    return result


@router.get("/access-token")
def access_token(auth_code):
    result = get_access_token(auth_code)
    return result
