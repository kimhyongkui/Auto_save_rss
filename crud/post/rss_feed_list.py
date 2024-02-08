from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Rss_list

Session = sessionmaker(bind=engine)
session = Session()


def add_rss(rss_name, rss_url):
    try:
        result = Rss_list(rssNm=rss_name, rssUrl=rss_url)
        session.add(result)
        session.commit()
        return "저장 완료"

    except Exception as err:
        session.rollback()
        return str(err)

    finally:
        session.close()
