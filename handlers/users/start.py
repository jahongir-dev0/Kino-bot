# handlers/users/start.py
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot
from data.config import ADMINS
from keyboards.inline.subscription import check_channels_keyboard
from keyboards.inline.menu import main_menu
from utils.user import check_user_subscriptions

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    is_subscribed = await check_user_subscriptions(bot, message.from_user.id)
    if not is_subscribed:
        return await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=check_channels_keyboard())
    is_admin = str(message.from_user.id) in ADMINS
    await message.answer(f"Xush kelibsiz, <b>{message.from_user.full_name}</b>!", reply_markup=main_menu(is_admin))
