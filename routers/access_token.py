from fastapi import APIRouter
from app.auth import get_access_token

router = APIRouter()


@router.get("/access-token")
def access_token():
    result = get_access_token()
    return result
