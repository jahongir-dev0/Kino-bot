from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from data.config import ADMINS
from states.post_film import PostFilm
from utils.film import get_film_by_code

CHANNEL_USERNAME = "@testovykanalfilm"

@dp.callback_query_handler(text="post_film")
async def ask_film_code(call: types.CallbackQuery):
    if str(call.from_user.id) not in ADMINS:
        return await call.answer("Ruxsat yo‘q!", show_alert=True)
    await call.message.edit_text("🆔 Kino KODINI yuboring:")
    await PostFilm.code.set()

@dp.message_handler(state=PostFilm.code)
async def post_film(message: types.Message, state: FSMContext):
    code = message.text.strip()
    film = get_film_by_code(code)

    if not film:
        await message.answer("🚫 Kod bo‘yicha kino topilmadi.")
        return await state.finish()

    try:
        await bot.send_video(
            chat_id=CHANNEL_USERNAME,
            video=film["file_id"],
            caption=(
                f"<b>{film['title']}</b>\n"
                f"🌍 Davlat: {film['country']}\n"
                f"📅 Yil: {film['year']}\n"
                f"⏱ Davomiylik: {film['duration']}\n"
                f"🔐 Kod: <code>{film['code']}</code>"
            )
        )
        await message.answer("✅ Kino kanalga yuborildi!")
    except Exception as e:
        await message.answer(f"❌ Xatolik: {e}")
    await state.finish()