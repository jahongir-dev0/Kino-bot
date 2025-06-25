from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.channel import get_channels

def check_channels_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    for ch in get_channels():
        markup.add(InlineKeyboardButton(text=f"➕ Obuna bo'lish: {ch}", url=f"https://t.me/{ch.lstrip('@')}"))
    markup.add(InlineKeyboardButton("✅ Obunani tekshirish", callback_data="check_subs"))
    return markup
