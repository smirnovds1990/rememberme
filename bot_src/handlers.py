from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from constants import START_MESSAGE


main_router = Router()


@main_router.message(CommandStart())
async def start(message: Message) -> None:
    """Handle /start command."""
    await message.answer(START_MESSAGE)
