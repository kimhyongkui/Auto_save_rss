from fastapi import APIRouter
from crud.post.rss_feed_list import add_rss
from crud.get.rss_feed_list import get_rss, get_rss_all
from crud.delete.rss_feed_list import delete_rss
from crud.update.rss_feed_list import patch_rss

router = APIRouter()


@router.post("/rss-feed", tags=["RSS URL 추가"])
def add_rss_feed(rss_name, rss_url):
    result = add_rss(rss_name, rss_url)
    return result


@router.get("/rss-feed/specific", tags=["RSS URL 검색"])
def get_rss_feed(rss_name):
    result = get_rss(rss_name)
    return result


@router.get("/rss-feed/all", tags=["RSS URL 검색"])
def get_rss_feed_all():
    result = get_rss_all()
    return result


@router.delete("/rss-feed", tags=["RSS FEED 삭제"])
def delete_rss_feed(rss_name):
    result = delete_rss(rss_name)
    return result


@router.patch("/rss-feed", tags=["RSS FEED 수정"])
def patch_rss_feed(rss_name, rss_url):
    result = patch_rss(rss_name, rss_url)
    return result
