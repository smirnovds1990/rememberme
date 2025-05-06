from zoneinfo import ZoneInfo

from aiogram import Bot
from apscheduler.triggers.cron import CronTrigger

from constants import MOSCOW_TZ, MY_OWN_SCHEDULE


cron_trigger = CronTrigger(
    hour=MY_OWN_SCHEDULE,
    timezone=ZoneInfo(MOSCOW_TZ),
)


async def send_random_article(bot: Bot, chat_id: int) -> None:
    """Send a random article to a subscribed user according to
    his chosen schedule.
    """
    # get a random article
