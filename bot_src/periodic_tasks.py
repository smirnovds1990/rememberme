from zoneinfo import ZoneInfo

from aiogram import Bot
from apscheduler.triggers.cron import CronTrigger
from utils import get_random_article

from constants import MOSCOW_TZ


cron_trigger = CronTrigger(
    hour="9, 12, 15, 18, 21",
    minute="3, 4, 5, 6, 7, 8",
    timezone=ZoneInfo(MOSCOW_TZ),
)


async def send_random_article(bot: Bot, chat_id: int) -> None:
    """Send a random article to a subscribed user according to
    his chosen schedule.
    """
    article = await get_random_article()
    await bot.send_message(chat_id=chat_id, text=article, parse_mode="HTML")
