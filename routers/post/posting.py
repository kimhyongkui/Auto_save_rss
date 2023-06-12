from fastapi import APIRouter
from api.posting import post_to_tistory

router = APIRouter()


@router.get("/feed")
def posting(keywords):
    result = post_to_tistory(keywords)
    return result
