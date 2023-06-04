from aiogram.fsm.state import StatesGroup, State


class FindSG(StatesGroup):
    location = State()
    next_places = State()
