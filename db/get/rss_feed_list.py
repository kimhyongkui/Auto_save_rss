from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Rss_list
from fastapi import HTTPException, status

Session = sessionmaker(bind=engine)
session = Session()


def get_rss(rss_name):
    try:
        result = session.query(Rss_list).filter(Rss_list.rssNm == rss_name).first()
        if result:
            return result
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터가 존재하지 않습니다.")

    except HTTPException:
        raise
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))


def get_rss_all():
    try:
        result = session.query(Rss_list).filter().all()
        if result:
            return result
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="데이터가 존재하지 않습니다.")

    except HTTPException:
        raise
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
