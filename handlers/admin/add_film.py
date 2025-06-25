import json
import os
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from data.config import ADMINS
from states.add_film import AddFilm

FILM_JSON_PATH = "data/films.json"

def save_film_to_json(film_data: dict):
    if not os.path.exists(FILM_JSON_PATH):
        with open(FILM_JSON_PATH, "w", encoding="utf-8") as f:
            f.write("[]")

    try:
        with open(FILM_JSON_PATH, "r", encoding="utf-8") as f:
            films = json.load(f)
    except json.JSONDecodeError:
        films = []

    films.append(film_data)

    with open(FILM_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(films, f, indent=2, ensure_ascii=False)
@dp.callback_query_handler(text="add_film")
async def start_add_film(call: types.CallbackQuery):
    if str(call.from_user.id) not in ADMINS:
        return await call.answer("Ruxsat yo‘q!", show_alert=True)
    await call.message.edit_text("🎬 Kino nomini kiriting:")
    await AddFilm.title.set()

@dp.message_handler(state=AddFilm.title)
async def set_title(message: types.Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("🌍 Davlatni kiriting:")
    await AddFilm.country.set()

@dp.message_handler(state=AddFilm.country)
async def set_country(message: types.Message, state: FSMContext):
    await state.update_data(country=message.text)
    await message.answer("📅 Chiqqan yilini kiriting:")
    await AddFilm.year.set()

@dp.message_handler(state=AddFilm.year)
async def set_year(message: types.Message, state: FSMContext):
    await state.update_data(year=message.text)
    await message.answer("⏱ Davomiyligini kiriting:")
    await AddFilm.duration.set()

@dp.message_handler(state=AddFilm.duration)
async def set_duration(message: types.Message, state: FSMContext):
    await state.update_data(duration=message.text)
    await message.answer("🔐 Kino KODINI kiriting (unikal):")
    await AddFilm.code.set()

@dp.message_handler(state=AddFilm.code)
async def set_code(message: types.Message, state: FSMContext):
    await state.update_data(code=message.text)
    await message.answer("📥 Kinoning video faylini yuboring:")
    await AddFilm.file.set()

@dp.message_handler(content_types=types.ContentType.VIDEO, state=AddFilm.file)
async def save_film(message: types.Message, state: FSMContext):
    data = await state.get_data()
    file_id = message.video.file_id
    film_data = {
        "title": data["title"],
        "country": data["country"],
        "year": data["year"],
        "duration": data["duration"],
        "code": data["code"],
        "file_id": file_id
    }
    save_film_to_json(film_data)
    await message.answer("✅ Kino muvaffaqiyatli qo‘shildi!")
    await state.finish()