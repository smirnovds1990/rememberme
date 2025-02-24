from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from constants import START_MESSAGE
from keyboards import main_keyboard


main_router = Router()


@main_router.message(CommandStart())
async def start(message: Message) -> None:
    """Handle /start command."""
    await message.answer(START_MESSAGE, reply_markup=main_keyboard())


@main_router.message(F.text == "Start registration.")
async def start_registration(message: Message):
    await message.answer("Let's start.")
