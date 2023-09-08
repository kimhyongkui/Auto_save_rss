import os
from _datetime import datetime
import requests
from dotenv import load_dotenv
from fastapi import HTTPException, status
from api.posting import write_content
import time

load_dotenv()


def modify_posting(keywords: list, post_id):
    try:
        now = datetime.now()

        url = "https://www.tistory.com/apis/post/modify"
        data = {"access_token": {os.getenv('ACCESS_TOKEN')},
                "output": "json",
                "blogName": "hyongkui",
                "postId": post_id,
                "title": f"{now.month}월 {now.day}일 뉴스",
                "content": write_content(keywords),
                "visibility": 0,
                "category": 1135999,
                "published": time.time()
                }
        response = requests.post(url, data=data)

        if response.status_code == 200:
            result = "게시글이 성공적으로 수정되었습니다."
        elif response.status_code == 414:
            result = "URI에 담긴 내용이 너무 깁니다."
        elif response.status_code == 400:
            result = "게시글 수정에 실패했습니다."
        else:
            result = f"{response.status_code}에러로 게시글 수정에 실패했습니다."

        return result

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
