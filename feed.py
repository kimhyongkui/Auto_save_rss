import requests
import feedparser


def parsing_rss():
    url_list = [
        "https://rss.donga.com/science.xml",
        "https://rss.hankyung.com/feed/it.xml"

    ]
    rss_dic = []
    for p in url_list:
        parse_rss = feedparser.parse(p)
        for i in parse_rss.entries:
            rss_dic.append(
                {
                    'title': i.title,
                    'link': i.link,
                    'published': i.published,
                    'summary': i.summary
                }
            )
    return rss_dic
