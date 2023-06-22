import os
import datetime
import requests
from dotenv import load_dotenv
from api.parse_rss import parsing_rss

load_dotenv()


def post_to_tistory():
    now = datetime.datetime.now()

    url = f"https://www.tistory.com/apis/post/write?" \
          f"access_token={os.getenv('ACCESS_TOKEN')}" \
          f"&output=json" \
          f"&blogName=hyongkui" \
          f"&title={now.month}월 {now.day}일 뉴스" \
          f"&content={parsing_rss()}" \
          f"&visibility=0" \
          f"&category=1" \
          f"&published=time.time()"

    response = requests.post(url)

    if response.status_code == 200:
        result = "게시글이 성공적으로 작성되었습니다."
    else:
        result = "게시글 작성에 실패하였습니다."

    return result
