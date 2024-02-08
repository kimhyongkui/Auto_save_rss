import os
from _datetime import datetime
import requests
from dotenv import load_dotenv
from api.parse_rss import parsing_rss
from fastapi import HTTPException, status
import time

load_dotenv()


def write_content(keywords: list):
    rss_list = parsing_rss(keywords)
    content = ""
    duplicate_titles_and_links = set()
    for rss in rss_list:
        title = rss.get("title")
        link = rss.get("link")

        if (title, link) not in duplicate_titles_and_links:
            duplicate_titles_and_links.add((title, link))
            content += f"<h3 data-ke-size='size23'>{title}</h3>\n"
            content += f"<p data-ke-size='size16'><a href='{link}'>{link}</a></p>\n"
            content += f"<ul style='list-style-type: disc;' data-ke-list-type='disc'><li>&nbsp;</li></ul>"
            content += '<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />'

    return content


def post_to_tistory(keywords: list):
    try:
        now = datetime.now()

        url = "https://www.tistory.com/apis/post/write"
        data = {"access_token": {os.getenv('ACCESS_TOKEN')},
                "output": "json",
                "blogName": "hyongkui",
                "title": f"{now.month}월 {now.day}일 뉴스",
                "content": write_content(keywords),
                "visibility": 0,
                "category": 1135999,
                "published": time.time()
                }
        response = requests.post(url, data=data)

        if response.status_code == 200:
            result = "게시글이 성공적으로 작성되었습니다."
        elif response.status_code == 414:
            result = "URI에 담긴 내용이 너무 깁니다."
        elif response.status_code == 400:
            result = "게시글 작성에 실패했습니다."
        else:
            result = f"{response.status_code}에러로 게시글 작성에 실패했습니다."

        return result

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


post_to_tistory(['AI', '구글', 'GPT', '코딩', 'it'])
