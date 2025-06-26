from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.film_search import FilmSearch
from utils.film import search_film_by_name, get_film_by_code

@dp.callback_query_handler(text="search_by_name")
async def ask_film_name(call: types.CallbackQuery):
    await call.message.edit_text("🎬 Kino nomini yuboring:")
    await FilmSearch.by_name.set()

@dp.message_handler(state=FilmSearch.by_name)
async def search_by_name_handler(message: types.Message, state: FSMContext):
    name = message.text.strip()
    results = search_film_by_name(name)
    if not results:
        await message.answer("🚫 Kino topilmadi.")
        return await state.finish()
    for film in results:
        await message.answer_video(
            video=film["file_id"],
            caption=(
                f"<b>{film['title']}</b>\n"
                f"🌍 Davlat: {film['country']}\n"
                f"📅 Yil: {film['year']}\n"
                f"⏱ Davomiylik: {film['duration']}\n"
                f"🔐 Kod: <code>{film['code']}</code>"
            )
        )
    await state.finish()

@dp.callback_query_handler(text="search_by_code")
async def ask_film_code(call: types.CallbackQuery):
    await call.message.edit_text("🔐 Kino KODINI yuboring:")
    await FilmSearch.by_code.set()

@dp.message_handler(state=FilmSearch.by_code)
async def search_by_code_handler(message: types.Message, state: FSMContext):
    code = message.text.strip()
    film = get_film_by_code(code)
    if not film:
        await message.answer("🚫 Kod bo‘yicha kino topilmadi.")
    else:
        await message.answer_video(
            video=film["file_id"],
            caption=(
                f"<b>{film['title']}</b>\n"
                f"🌍 Davlat: {film['country']}\n"
                f"📅 Yil: {film['year']}\n"
                f"⏱ Davomiylik: {film['duration']}\n"
                f"🔐 Kod: <code>{film['code']}</code>"
            )
        )
    await state.finish()