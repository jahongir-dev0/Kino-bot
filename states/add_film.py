from aiogram.dispatcher.filters.state import State, StatesGroup

class AddFilm(StatesGroup):
    title = State()
    country = State()
    year = State()
    duration = State()
    code = State()
    file = State()
