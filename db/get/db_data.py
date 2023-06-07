from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Rss_list

Session = sessionmaker(bind=engine)
session = Session()


def get_url_list():
    result = session.query(Rss_list.rssUrl).all()
    rss_url = []
    for url in result:
        rss_url.append(url[0])

    return rss_url
