from fastapi import APIRouter
from api.posting import post_to_tistory

router = APIRouter()


@router.get("/feed")
def posting():
    result = post_to_tistory()
    return result
