import logging
import os

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
START_MESSAGE = "Hello to the rememberme bot!"
MY_TELEGRAM_CHAT_ID = os.getenv("MY_TELEGRAM_CHAT_ID")
MY_OWN_SCHEDULE = "9,12,15,18,21"
MOSCOW_TZ = "Europe/Moscow"
RANDOM_ARTICLE_URL = os.getenv("RANDOM_ARTICLE_URL")
LOG_FORMAT = os.getenv("LOG_FORMAT")
LOG_LEVEL = os.getenv("LOG_LEVEL", logging.INFO)
