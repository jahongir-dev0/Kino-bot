# handlers/users/random_film.py
from aiogram import types
from loader import dp
from utils.film import get_random_film

@dp.callback_query_handler(text="random")
async def send_random_film(call: types.CallbackQuery):
    film = get_random_film()
    if not film:
        return await call.message.answer("🚫 Film bazasi bo‘sh.")
    await call.message.answer_video(
        video=film["file_id"],
        caption=(
            f"<b>{film['title']}</b>\n"
            f"🌍 Davlat: {film['country']}\n"
            f"📅 Yil: {film['year']}\n"
            f"⏱ Davomiylik: {film['duration']}\n"
            f"🔐 Kod: <code>{film['code']}</code>"
        )
    )