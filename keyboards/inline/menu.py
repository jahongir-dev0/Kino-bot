from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu(is_admin=False):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("🔎 Film Qidiruv", callback_data="search_menu"),
        InlineKeyboardButton("🎬 Barcha Filmlar", url="https://t.me/testovykanalfilm")
    )
    markup.add(
        InlineKeyboardButton("🎲 Tasodifiy Film", callback_data="random"),
        InlineKeyboardButton("📦 Film Buyurtma", callback_data="request")
    )
    markup.add(InlineKeyboardButton("📊 TOP Filmlar", callback_data="top"))
    if is_admin:
        markup.add(InlineKeyboardButton("⚙️ Admin Panel", callback_data="admin_panel"))
    return markup