import feedparser


def parsing_rss():
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

    for url in url_list:
        parse_rss = feedparser.parse(url)
        # 지금 코드를 그대로 사용하면 RSS 피드 메인페이지의 목록을 그대로 긁어옴.
        # 내가 원하는 날짜의 기사만 필터링 할 필요가 있다.
        for entry in parse_rss.entries:
            title = entry.title if hasattr(entry, "title") else None
            link = entry.link if hasattr(entry, "link") else None
            updated = entry.updated if hasattr(entry, "updated") else None

            rss_list.append({
                "title": title,
                "link": link,
                "updated": updated
            })

    return rss_list
