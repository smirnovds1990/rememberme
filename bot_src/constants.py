import os

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
START_MESSAGE = "Hello to the rememberme bot!"
