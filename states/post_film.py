from aiogram.dispatcher.filters.state import State, StatesGroup

class PostFilm(StatesGroup):
    code = State()