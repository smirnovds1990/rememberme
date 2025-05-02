from zoneinfo import ZoneInfo

from aiogram import Bot
from apscheduler.triggers.cron import CronTrigger


cron_trigger = CronTrigger(
    hour="16,17",
    minute="17,18,19,20",
    timezone=ZoneInfo("Europe/Moscow"),
)


async def send_random_article(bot: Bot, chat_id: int) -> None:
    """Send a random article to a subscribed user according to
    his chosen schedule.
    """
    await bot.send_message(chat_id=chat_id, text="It works!")
