from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Rss_list
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status

Session = sessionmaker(bind=engine)
session = Session()


def patch_rss(rss_name, rss_url):
    try:
        result = session.query(Rss_list).filter(Rss_list.rssNm == rss_name).first()
        if result:
            result.rssNm = rss_name
            result.rssUrl = rss_url
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "삭제 완료"})
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터가 존재하지 않습니다.")

    except Exception as err:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()
