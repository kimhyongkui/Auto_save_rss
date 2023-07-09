from fastapi import APIRouter, Query
from api.posting import post_to_tistory
from typing import List

router = APIRouter()


@router.post("/post", tags=["Tistory 포스팅"])
def posting(keywords: List[str] = Query(...)):
    result = post_to_tistory(keywords)
    return result
