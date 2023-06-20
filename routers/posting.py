from fastapi import APIRouter
from api.posting import post_to_tistory

router = APIRouter()


@router.get("/feed")
def posting(title, content):
    result = post_to_tistory(title, content)
    return result
