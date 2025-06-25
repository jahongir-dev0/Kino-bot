from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def search_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🔍 Nomi orqali", callback_data="search_by_name"),
        InlineKeyboardButton("🔎 Kod orqali", callback_data="search_by_code"),
        InlineKeyboardButton("🏘 Asosiy menyu", callback_data="main_menu")
    )
    return markup