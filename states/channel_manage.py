from aiogram.dispatcher.filters.state import State, StatesGroup

class ManageChannels(StatesGroup):
    add = State()
    remove = State()
    set_admin = State()
