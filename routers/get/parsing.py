from fastapi import APIRouter, Query
from typing import List
from api.parse_rss import parsing_rss

router = APIRouter()


@router.get("/feed", tags=["파싱"])
def parsing(keywords: List[str] = Query(...)):
    result = parsing_rss(keywords)
    return result
