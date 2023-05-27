from fastapi import APIRouter, Request
from api.parse_rss import parsing_rss

router = APIRouter()


@router.get("/feed")
def parsing(request: Request):
    result = parsing_rss(request)
    return result
