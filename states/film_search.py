from aiogram.dispatcher.filters.state import State, StatesGroup

class FilmSearch(StatesGroup):
    by_name = State()
    by_code = State()