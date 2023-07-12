from aiogram.dispatcher.filters.state import State, StatesGroup


class MainState(StatesGroup):
    command = State()
    next_com = State()
    mess = State()
