import feedparser
from fastapi import Request
from fastapi.templating import Jinja2Templates

template = Jinja2Templates(directory="templates")


def parsing_rss(request: Request):
    donga = "https://rss.donga.com/science.xml"
    hankyung = "https://rss.hankyung.com/feed/it.xml"
    url_list = [
        donga,
        hankyung
    ]
    rss_dic = []
    for p in url_list:
        parse_rss = feedparser.parse(p)
        if p is donga:
            for i in parse_rss.entries:
                rss_dic.append(
                    {
                        "title": i.title,
                        "link": i.link,
                        "published": i.published,
                        "summary": i.summary
                    }
                )
        if p is hankyung:
            for i in parse_rss.entries:
                rss_dic.append(
                    {
                        "title": i.title,
                        "link": i.link,
                        "published": i.publishedg
                    }
                )
    return template.TemplateResponse("feed.html", {"request": request, "rss_dic": rss_dic})
