from aiogram import types
from loader import dp
from keyboards.inline.search_menu import search_menu
from keyboards.inline.menu import main_menu
from data.config import ADMINS

@dp.callback_query_handler(text="search_menu")
async def show_search_menu(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text("🔍 Qidiruv bo‘limi:", reply_markup=search_menu())

@dp.callback_query_handler(text="main_menu")
async def back_to_main_menu(call: types.CallbackQuery):
    is_admin = str(call.from_user.id) in ADMINS
    await call.message.edit_text(f"🏠 Asosiy menyu:", reply_markup=main_menu(is_admin))
