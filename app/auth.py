from dotenv import load_dotenv
import os
import requests

load_dotenv()


# 1시간 이후 만료됨
def get_auth_url():
    auth_url = f"https://www.tistory.com/oauth/authorize?" \
               f"client_id={os.getenv('APP_ID')}" \
               f"&redirect_uri=http://www.tistory.com/member/blog" \
               f"&response_type=code"
    return auth_url


# 3개월 정도 이후 만료
def get_access_token(auth_code):
    url = f"https://www.tistory.com/oauth/access_token?client_id={os.getenv('APP_ID')}" \
          f"&client_secret={os.getenv('SECRET_KEY')}" \
          f"&redirect_uri=http://www.tistory.com/member/blog" \
          f"&code={auth_code}" \
          f"&grant_type=authorization_code"
    response = requests.get(url)
    access_token = response.text.split("=")[1]
    return access_token
