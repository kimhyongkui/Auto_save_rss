import requests
from dotenv import load_dotenv
from api.parse_rss import parsing_rss


def post_to_tistory():
    url = f"https://www.tistory.com/apis/post/write?" \
          "access_token=5c8e29d8da48f1c7c5f7a26f939e7a7f_9d321dba72c62fb3e3633515bd73011b" \
          "&output=json" \
          "&blogName=hyongkui" \
          "&title=테스트 중" \
          "&content=안녕하세요 테스트 중입니다" \
          "&visibility=0" \
          "&category=뉴스거리" \
          "&published=time.time()"
    response = requests.post(url)

    if response.status_code == 200:
        print("게시글이 성공적으로 작성되었습니다.")
    else:
        print("게시글 작성에 실패하였습니다.")
