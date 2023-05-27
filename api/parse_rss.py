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
    for parse_list in url_list:
        parse_rss = feedparser.parse(parse_list)
        for entry in parse_rss.entries:
            try:
                title = entry.title
                link = entry.link
                published = entry.published
            except AttributeError:
                title = None
                link = None
                published = None

            rss_dic.append({
                "title": title,
                "link": link,
                "published": published
            })
    return rss_dic
