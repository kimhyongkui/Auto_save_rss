import os
from dotenv import load_dotenv
import requests

load_dotenv()


def get_category_info():
    url = f"https://www.tistory.com/apis/category/list?" \
          f"access_token={os.getenv('ACCESS_TOKEN')}" \
          f"&output=json" \
          f"&blogName=hyongkui"
    result = requests.get(url)
    category = result.json()
    categories = category['tistory']['item']['categories']
    categories_list = []
    for data in categories:
        categories_dict = {
            "id": data["id"],
            "name": data["name"],
            "parent": data["parent"],
            "label": data["label"],
            "entries": data["entries"]
        }
        categories_list.append(categories_dict)

    return categories_list
