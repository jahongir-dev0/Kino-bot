from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from data.config import ADMINS
from states.add_film import AddFilm
from utils.film import save_film

@dp.callback_query_handler(text="add_film")
async def start_add_film(call: types.CallbackQuery):
    if str(call.from_user.id) not in ADMINS:
        return await call.answer("Ruxsat yo‘q!", show_alert=True)
    await call.message.edit_text("🎬 Kino nomini kiriting:")
    await AddFilm.title.set()

@dp.message_handler(state=AddFilm.title)
async def set_title(message: types.Message, state: FSMContext):
    title = message.text.strip()
    if not title:
        return await message.answer("❌ Kino nomi bo‘sh bo‘lmasligi mumkin.")
    await state.update_data(title=title)
    await message.answer("🌍 Davlatni kiriting:")
    await AddFilm.country.set()

@dp.message_handler(state=AddFilm.country)
async def set_country(message: types.Message, state: FSMContext):
    await state.update_data(country=message.text.strip())
    await message.answer("📅 Chiqqan yilini kiriting:")
    await AddFilm.year.set()

@dp.message_handler(state=AddFilm.year)
async def set_year(message: types.Message, state: FSMContext):
    year = message.text.strip()
    if not year.isdigit():
        return await message.answer("❌ Yil faqat son bo‘lishi kerak.")
    await state.update_data(year=year)
    await message.answer("⏱ Davomiylikni kiriting:")
    await AddFilm.duration.set()

@dp.message_handler(state=AddFilm.duration)
async def set_duration(message: types.Message, state: FSMContext):
    await state.update_data(duration=message.text.strip())
    await message.answer("🔐 Kino KODINI kiriting:")
    await AddFilm.code.set()

@dp.message_handler(state=AddFilm.code)
async def set_code(message: types.Message, state: FSMContext):
    code = message.text.strip()
    if not code:
        return await message.answer("❌ Kod bo‘sh bo‘lmasligi kerak.")
    await state.update_data(code=code)
    await message.answer("📥 Video faylni yuboring:")
    await AddFilm.file.set()

@dp.message_handler(content_types=types.ContentType.VIDEO, state=AddFilm.file)
async def save_film_handler(message: types.Message, state: FSMContext):
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

    try:
        save_film(film_data)
        await message.answer("✅ Kino muvaffaqiyatli qo‘shildi!")
    except Exception as e:
        await message.answer(f"❌ Xatolik: {e}")
    await state.finish()