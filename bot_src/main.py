import asyncio

from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from constants import BOT_TOKEN
from handlers import main_router
from periodic_tasks import cron_trigger, send_random_article


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler()


async def main() -> None:
    dp.include_router(main_router)
    scheduler.add_job(
        func=send_random_article,
        trigger=cron_trigger,
        kwargs={"bot": bot, "chat_id": 882103941},
    )
    scheduler.start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
