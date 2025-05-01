from aiogram.fsm.state import State, StatesGroup


class RegistrationForm(StatesGroup):
    """Provide options for mesaging schedule for a user."""

    username = State()
    topics = State()
    messages_schedule = State()
