import feedparser
from datetime import datetime


def parsing_rss(keyword):
    donga = "https://rss.donga.com/science.xml"
    hankyung = "https://rss.hankyung.com/feed/it.xml"
    khan = "https://www.khan.co.kr/rss/rssdata/it_news.xml"
    newsis = "https://newsis.com/RSS/health.xml"
    itworld = "https://www.itworld.co.kr/rss/feed/index.php"

    url_list = [
        donga,
        hankyung,
        khan,
        newsis,
        itworld
    ]
    rss_list = []

    today = datetime.today().date()

    for url in url_list:
        parse_rss = feedparser.parse(url)
        for entry in parse_rss.entries:
            title = entry.title if hasattr(entry, "title") else None
            link = entry.link if hasattr(entry, "link") else None
            updated = entry.updated if hasattr(entry, "updated") else None

            parsed_updated = None

            # 날짜 형식에 맞게 파싱하여 연도, 월, 일 추출
            if updated:
                try:
                    # "%a, %d %b %Y %H:%M:%S %z" 형식
                    parsed_updated = datetime.strptime(updated, "%a, %d %b %Y %H:%M:%S %z").date()
                except ValueError:
                    try:
                        # "%Y-%m-%dT%H:%M:%S%z" 형식
                        parsed_updated = datetime.strptime(updated, "%Y-%m-%dT%H:%M:%S%z").date()
                    except ValueError:
                        try:
                            # "%Y-%m-%d %H:%M:%S" 형식
                            parsed_updated = datetime.strptime(updated, "%Y-%m-%d %H:%M:%S").date()
                        except ValueError:
                            # 다른 형식의 경우에는 날짜 정보를 추출할 수 없음
                            pass

            if parsed_updated == today and keyword in title:
                rss_list.append({
                    "title": title,
                    "link": link,
                    "updated": updated
                })

    return rss_list
