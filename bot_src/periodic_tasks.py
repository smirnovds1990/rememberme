import html
import logging
from zoneinfo import ZoneInfo

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from apscheduler.triggers.cron import CronTrigger
from utils import get_random_article

from constants import MOSCOW_TZ


logger = logging.getLogger(__name__)


cron_trigger = CronTrigger(
    hour="9, 12, 15, 18, 21",
    timezone=ZoneInfo(MOSCOW_TZ),
)


async def send_random_article(bot: Bot, chat_id: int) -> None:
    """Send a random article to a subscribed user according to
    his chosen schedule.
    """
    title, article = await get_random_article()
    try:
        await bot.send_message(
            chat_id=chat_id, text=article, parse_mode="HTML"
        )
        logger.info("Sent article: %s", title)
    except TelegramBadRequest as error:
        if "can't parse entities" in str(error):
            await bot.send_message(chat_id=chat_id, text=html.escape(article))
            logger.warning("Got an article with broken HTML tags: %s", title)
        else:
            raise
