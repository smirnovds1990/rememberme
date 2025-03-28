from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


cancel_button = KeyboardButton(text="Cancel")
cancel_keyboard = ReplyKeyboardMarkup(
    keyboard=[[cancel_button]],
    resize_keyboard=True,
    one_time_keyboard=True,
)


def main_keyboard() -> ReplyKeyboardMarkup:
    buttons = [[KeyboardButton(text="Start registration.")]]
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=True,
    )
