from fastapi import APIRouter
from db.post.rss_url import add_rss

router = APIRouter()


@router.post("/rss-feed")
def posting(name, url):
    result = add_rss(name, url)
    return result
