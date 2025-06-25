from aiogram.dispatcher.filters.state import State, StatesGroup

class RequestFilm(StatesGroup):
    waiting_text = State()
