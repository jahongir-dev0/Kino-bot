from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from data.config import ADMINS
from utils.db_api.channel import get_channels
from keyboards.inline.subscription import check_channels_keyboard
from keyboards.inline.menu import main_menu
from aiogram.utils.exceptions import MessageNotModified

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


@dp.callback_query_handler(text="check_subs")
async def recheck_subscription(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=2)
    user_id = call.from_user.id
    if not await check_user_subscriptions(user_id):
        try:
            await call.message.edit_text("❗ Obuna hali ham tekshirilmagan. Kanallarga obuna bo‘ling:", reply_markup=check_channels_keyboard())
        except MessageNotModified:
            await call.answer("⛔ Obuna holati o‘zgarmagan.")
    else:
        is_admin = str(user_id) in ADMINS
        await call.message.edit_text(
            f"✅ Rahmat, {call.from_user.full_name}!\nBotdan foydalanishingiz mumkin.",
            reply_markup=main_menu(is_admin)
        )