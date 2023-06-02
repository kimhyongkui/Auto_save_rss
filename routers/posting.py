from fastapi import APIRouter
from api.posting import post_to_tistory

router = APIRouter()


@router.get("/feed")
def posting(keyword):
    result = post_to_tistory(keyword)
    return result
