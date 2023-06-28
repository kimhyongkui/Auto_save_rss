from sqlalchemy import VARCHAR, Column
from db.connection import Base


class Rss_list(Base):
    __tablename__ = "rss_list"

    rssNm = Column(VARCHAR(45), primary_key=True, nullable=False)
    rssUrl = Column(VARCHAR(45), nullable=False)
