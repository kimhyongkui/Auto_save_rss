from fastapi import APIRouter
from api.parse_rss import parsing_rss

router = APIRouter()


@router.get("/feed")
def parsing(keyword):
    result = parsing_rss(keyword)
    return result
