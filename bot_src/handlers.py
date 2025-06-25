from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from states import RegistrationForm

from constants import START_MESSAGE
from keyboards import (  # main_keyboard,
    cancel_keyboard,
    hour_keyboard,
    topic_keyboard,
)


main_router = Router()


@main_router.message(CommandStart())
async def start(message: Message) -> None:
    """Handle /start command."""

    await message.answer(START_MESSAGE)


@main_router.message(F.text == "Cancel")
async def cancel_action(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("Cancelled", reply_markup=ReplyKeyboardRemove())


@main_router.message(F.text == "Start registration.")
async def start_registration(message: Message, state: FSMContext) -> None:
    await message.answer("Let's start.", reply_markup=cancel_keyboard)
    await state.clear()
    await state.set_state(RegistrationForm.username)
    await message.answer("Write your username.")


@main_router.message(RegistrationForm.username)
async def username_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(username=message.text)
    await state.set_state(RegistrationForm.topics)
    await message.answer(
        "Choose the topics you are interested in.",
        reply_markup=topic_keyboard(set()),
    )


@main_router.callback_query(
    RegistrationForm.topics, F.data.startswith("toggle_topic")
)
async def toggle_topic_handler(
    callback: CallbackQuery, state: FSMContext
) -> None:
    topic = callback.data.split(":")[1]
    data = await state.get_data()
    selected = set(data.get("topics", []))
    if topic in selected:
        selected.remove(topic)
    else:
        selected.add(topic)
    await state.update_data(topics=list(selected))
    await callback.message.edit_reply_markup(
        reply_markup=topic_keyboard(selected)
    )
    await callback.answer()


@main_router.callback_query(RegistrationForm.topics, F.data == "done_topics")
async def done_topics_handler(
    callback: CallbackQuery, state: FSMContext
) -> None:
    data = await state.get_data()
    if not data.get("topics"):
        await callback.answer("Choose at least one topic.", show_alert=True)
        return
    await state.set_state(RegistrationForm.messages_schedule)
    await callback.message.answer(
        "Choose the time for messaging", reply_markup=hour_keyboard(set())
    )
    await callback.answer()


@main_router.callback_query(
    RegistrationForm.messages_schedule, F.data.startswith("toggle_hour")
)
async def toggle_hour_handler(
    callback: CallbackQuery,
    state: FSMContext,
) -> None:
    hour = int(callback.data.split(":")[1])
    data = await state.get_data()
    selected = set(data.get("messaging_schedule", []))
    if hour in selected:
        selected.remove(hour)
    else:
        selected.add(hour)
    await state.update_data(messaging_schedule=list(selected))
    await callback.message.edit_reply_markup(
        reply_markup=hour_keyboard(selected)
    )
    await callback.answer()


@main_router.callback_query(
    RegistrationForm.messages_schedule, F.data == "done_hours"
)
async def done_hours_handler(
    callback: CallbackQuery, state: FSMContext
) -> None:
    data = await state.get_data()
    if not data.get("messaging_schedule"):
        await callback.answer(
            "Choose at least one messaging hour.", show_alert=True
        )
        return
    await callback.message.answer(
        "Thank you! Your data are saved.", reply_markup=ReplyKeyboardRemove()
    )
    # save data to DB here
    await callback.message.answer(
        f"Username: {data["username"]}\n"
        f"Topics: {",".join(data["topics"])}\n"
        f"Messaging hours: {",".join(map(str, data["messaging_schedule"]))}"
    )
    await state.clear()
    await callback.answer()
