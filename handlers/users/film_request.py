from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from data.config import ADMINS
from states.request_film import RequestFilm


@dp.callback_query_handler(text="request")
async def request_film_start(call: types.CallbackQuery):
    await call.message.edit_text("📩 Iltimos, qaysi filmni qidirayotganingizni yozing:")
    await RequestFilm.waiting_text.set()


@dp.message_handler(state=RequestFilm.waiting_text)
async def receive_request_text(message: types.Message, state: FSMContext):
    user = message.from_user
    text = f"📩 <b>Film so‘rovi:</b>\n\n👤 <b>{user.full_name}</b> (@{user.username})\n🆔 <code>{user.id}</code>\n\n📝 {message.text}"

    for admin_id in ADMINS:
        try:
            await bot.send_message(admin_id, text)
        except Exception:
            continue

    await message.answer("✅ So‘rovingiz yuborildi! Tez orada adminlar ko‘rib chiqadi.")
    await state.finish()
