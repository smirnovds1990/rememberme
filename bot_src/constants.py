import os

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
START_MESSAGE = "Hello to the rememberme bot!"
MY_TELEGRAM_CHAT_ID = os.getenv("MY_TELEGRAM_CHAT_ID")
MY_OWN_SCHEDULE = "9,12,15,18,21"
MOSCOW_TZ = "Europe/Moscow"
