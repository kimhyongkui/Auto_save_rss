from fastapi import APIRouter
from db.post.rss_url import add_rss
from db.delete.delete_feed import delete_rss
from db.rss_feed_list.rss_feed_list import patch_rss

router = APIRouter()


@router.post("/rss-feed", tags=["RSS URL 추가"])
def add_rss_feed(rss_name, rss_url):
    result = add_rss(rss_name, rss_url)
    return result


@router.delete("/rss-feed", tags=["RSS FEED 삭제"])
def delete_rss_feed(rss_name):
    result = delete_rss(rss_name)
    return result


@router.patch("/rss-feed", tags=["RSS FEED 수정"])
def patch_rss_feed(rss_name, rss_url):
    result = patch_rss(rss_name, rss_url)
    return result
