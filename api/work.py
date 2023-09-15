import time
import schedule
from api.posting import post_to_tistory


def main():
    schedule.every().day.at("23:33").do(lambda: post_to_tistory(['AI', '구글', 'GPT', '카카오', '로봇']))

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
