from fastapi import APIRouter
from api.category import get_category

router = APIRouter()


@router.get("/category", tags=["카테고리 ID 얻기"])
def category():
    result = get_category()
    return result


