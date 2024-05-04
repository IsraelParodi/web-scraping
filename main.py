import os
from dotenv import load_dotenv
from utils import webdriver_handler

load_dotenv()


def main():
    web = os.environ.get("WEB")
    path = os.environ.get("CHROMEDRIVER_PATH")
    webdriver_handler.start_scrapping(web, path)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
