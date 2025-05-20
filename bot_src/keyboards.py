from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


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


TOPICS = ["IT", "English", "Science"]  # THAT'S A MOCK, USE DB


def topic_keyboard(selected: set[str]) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{'✅ ' if t in selected else ''}{t}",
                callback_data=f"toggle_topic:{t}",
            )
        ]
        for t in TOPICS  # SHOULD BE DB INSTANCES
    ] + [[InlineKeyboardButton(text="✅ Готово", callback_data="done_topics")]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def hour_keyboard(selected: set[int]) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{'✅ ' if h in selected else ''}{h}",
                callback_data=f"toggle_hour:{h}",
            )
            for h in range(i, min(i + 6, 24))
        ]
        for i in range(0, 24, 6)
    ] + [[InlineKeyboardButton(text="✅ Готово", callback_data="done_hours")]]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
