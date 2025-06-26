from aiogram import Dispatcher
from data.config import ADMINS
import logging

async def notify_admins(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "✅ Bot ishga tushdi.")
        except Exception as e:
            logging.warning(f"Adminga habar yuborib bo‘lmadi: {e}")
