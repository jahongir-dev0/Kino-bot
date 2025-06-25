# handlers/users/start.py (update)
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from data.config import ADMINS
from keyboards.inline.subscription import check_channels_keyboard
from keyboards.inline.menu import main_menu
from utils.db_api.channel import get_channels

async def check_user_subscriptions(user_id):
    result = []
    for ch in get_channels():
        try:
            member = await bot.get_chat_member(ch, user_id)
            if member.status not in ("member", "creator", "administrator"):
                result.append(False)
            else:
                result.append(True)
        except:
            result.append(False)
    return all(result)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    if not await check_user_subscriptions(message.from_user.id):
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=check_channels_keyboard())
    else:
        is_admin = str(message.from_user.id) in ADMINS
        await message.answer(f"Xush kelibsiz, <b>{message.from_user.full_name}</b>!", reply_markup=main_menu(is_admin))