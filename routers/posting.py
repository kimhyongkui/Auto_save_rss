from fastapi import APIRouter, Request
from api.posting import post_to_tistory

router = APIRouter()


@router.get("/posting")
def posting(request: Request):
    result = parsing_rss(request)
    return result
