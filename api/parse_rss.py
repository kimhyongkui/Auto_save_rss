import feedparser
from datetime import datetime
from db.get.db_data import get_url_list
from fastapi import HTTPException, status


def parsing_rss(keywords: list):
    try:
        url_list = get_url_list()
        rss_list = []
        today = datetime.today().date()

        for url in url_list:
            parse_rss = feedparser.parse(url)
            for entry in parse_rss.entries:
                title = entry.title if hasattr(entry, "title") else None
                link = entry.link if hasattr(entry, "link") else None
                updated = entry.updated if hasattr(entry, "updated") else None

                # 파싱된 업데이트 날짜를 저장 -> 파싱에 성공하면 바뀌고 아니면 None 유지
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
                for keyword in keywords:

                    if parsed_updated == today and keyword in title:
                        rss_list.append({
                            "title": title,
                            "link": link,
                            "updated": updated
                        })
        return rss_list

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
