import time
import schedule
from api.posting import post_to_tistory


def posting():
    schedule.every().day.at("13:30").do(lambda: post_to_tistory(['AI', '구글', 'GPT', '코딩', 'it']))

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    posting()
