from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Rss_list

Session = sessionmaker(bind=engine)
session = Session()


def add_rss(rss_name, rss_url):
    result = Rss_list(rssNm=rss_name, rssUrl=rss_url)
    session.add(result)
    session.commit()
    session.close()
    return "저장 완료"
