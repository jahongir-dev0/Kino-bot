from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_panel():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("➕ Film Qo‘shish", callback_data="add_film"),
        InlineKeyboardButton("📤 POST qilish", callback_data="post_film")
    )
    markup.add(
        InlineKeyboardButton("🛠 Kanal Sozlash", callback_data="channel_settings"),
        InlineKeyboardButton("🏘 Asosiy menyu", callback_data="main_menu")
    )
    return markup