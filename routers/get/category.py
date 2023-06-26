from fastapi import APIRouter
from api.category import get_category_info

router = APIRouter()


@router.get("/category", tags=["카테고리 데이터 얻기"])
def get_category():
    result = get_category_info()
    return result