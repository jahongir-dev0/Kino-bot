from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def channel_settings_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("➕ Kanal Qo‘shish", callback_data="add_channel"),
        InlineKeyboardButton("➖ Olib tashlash", callback_data="remove_channel")
    )
    markup.add(
        InlineKeyboardButton("📋 Ro‘yxat", callback_data="list_channels"),
        InlineKeyboardButton("🔗 Admin kanal", callback_data="set_admin_channel")
    )
    markup.add(InlineKeyboardButton("⬅️ Admin Panel", callback_data="admin_panel"))
    return markup