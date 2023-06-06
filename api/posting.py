import os
from _datetime import datetime
import requests
from dotenv import load_dotenv
from api.parse_rss import parsing_rss

load_dotenv()


def write_content(keyword):
    rss_list = parsing_rss(keyword)
    content = ""
    for rss in rss_list:
        title = rss.get("title")
        link = rss.get("link")
        content += f"<h3 data-ke-size='size23'>{title}</h3>\n"
        content += f"<p data-ke-size='size16'><a href='{link}'>{link}</a></p>\n"
        content += '<hr contenteditable="false" data-ke-type="horizontalRule" data-ke-style="style5" />'
    return content


def post_to_tistory(keyword):
    now = datetime.now()

    url = f"https://www.tistory.com/apis/post/write?" \
          f"access_token={os.getenv('ACCESS_TOKEN')}" \
          f"&output=json" \
          f"&blogName=hyongkui" \
          f"&title={now.month}월 {now.day}일 뉴스" \
          f"&content={write_content(keyword)}" \
          f"&visibility=0" \
          f"&category=1135999" \
          f"&published=time.time()"

    response = requests.post(url)

    if response.status_code == 200:
        result = "게시글이 성공적으로 작성되었습니다."
    else:
        result = "게시글 작성에 실패하였습니다."

    return result
