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
    rss_dic = []

    for url in url_list:
        parse_rss = feedparser.parse(url)

        for entry in parse_rss.entries:
            title = entry.title if hasattr(entry, "title") else None
            link = entry.link if hasattr(entry, "link") else None
            published = entry.published if hasattr(entry, "published") else None

            rss_dic.append({
                "title": title,
                "link": link,
                "published": published
            })

    return rss_dic
