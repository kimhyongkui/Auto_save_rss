import requests
from dotenv import load_dotenv
import os
from fastapi import status, HTTPException

load_dotenv()


def post_to_tistory(title, content):
    url = "https://hyongkui.tistory.com/"
    tistory_id = f"{os.getenv('86e49ccf400b197fd82342837b9406e3')}"
    tistory_access_token = f"{os.getenv('SECRET_KEY')}"
    data = {
        "access_token": tistory_access_token,
        "output": "json",
        "blogName": tistory_id,
        "title": title,
        "content": content
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("게시글이 성공적으로 작성되었습니다.")
    else:
        print("게시글 작성에 실패하였습니다.")



# 게시글 작성 예시
title = "제목"
content = "본문 내용"
post_to_tistory('title', 'content')
