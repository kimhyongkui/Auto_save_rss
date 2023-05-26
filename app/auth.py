from dotenv import load_dotenv
import os

load_dotenv()


def get_auth_code():
    url = f"https://www.tistory.com/oauth/authorize?" \
          f"client_id={os.getenv('APP_ID')}" \
          f"&redirect_uri=http://www.tistory.com/member/blog" \
          f"&response_type=code"
    return url


def get_access_token():
    url = f"https://www.tistory.com/oauth/access_token?client_id={os.getenv('APP_ID')}" \
          f"&client_secret={os.getenv('SECRET_KEY')}" \
          f"&redirect_uri=http://www.tistory.com/member/blog" \
          f"&code=5dc7de828e88450ed60983b3e09890aa02666c696062a92f580a20a0c8ffb1ccaf622122" \
          f"&grant_type=authorization_code"
    return url

