from fastapi import APIRouter
from db.delete.delete_feed import delete

router = APIRouter()


@router.delete("/rss-feed", tags=["RSS FEED 삭제"])
def delete_rss_feed(name):
    result = delete(name)
    return result
