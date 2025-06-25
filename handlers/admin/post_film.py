import json
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from data.config import ADMINS
from states.post_film import PostFilm

FILM_JSON_PATH = "data/films.json"
CHANNEL_USERNAME = "@mymusics_fr"

def get_film_by_code(code):
    try:
        with open(FILM_JSON_PATH, "r", encoding="utf-8") as f:
            films = json.load(f)
        for film in films:
            if film['code'].lower() == code.lower():
                return film
    except FileNotFoundError:
        return None
    return None

@dp.callback_query_handler(text="post_film")
async def ask_film_code(call: types.CallbackQuery):
    if str(call.from_user.id) not in ADMINS:
        return await call.answer("Ruxsat yo‘q!", show_alert=True)
    await call.message.edit_text("🆔 Kino KODINI yuboring:")
    await PostFilm.code.set()

@dp.message_handler(state=PostFilm.code)
async def post_film_to_channel(message: types.Message, state: FSMContext):
    code = message.text.strip()
    film = get_film_by_code(code)
    if not film:
        await message.answer("🚫 Kod bo‘yicha kino topilmadi.")
        return await state.finish()

    try:
        await bot.send_video(
            chat_id=CHANNEL_USERNAME,
            video=film["file_id"],
            caption=f"<b>{film['title']}</b>\nDavlat: {film['country']}\nYil: {film['year']}\nDavomiylik: {film['duration']}\nKod: <code>{film['code']}</code>"
        )
        await message.answer("✅ Kino kanalga yuborildi!")
    except Exception as e:
        await message.answer(f"❌ Xatolik: {str(e)}")

    await state.finish()
