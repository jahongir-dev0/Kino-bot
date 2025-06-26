from aiogram import types
from aiogram.utils.exceptions import MessageNotModified
from loader import dp, bot
from data.config import ADMINS
from utils.user import check_user_subscriptions
from keyboards.inline.subscription import check_channels_keyboard
from keyboards.inline.menu import main_menu

@dp.callback_query_handler(text="check_subs")
async def recheck_subscription(call: types.CallbackQuery):
    user_id = call.from_user.id
    is_subscribed = await check_user_subscriptions(bot, user_id)
    if not is_subscribed:
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