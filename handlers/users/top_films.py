from aiogram import types
from loader import dp
from utils.db_api.stats import get_top_films
from utils.film import get_film_by_code

@dp.callback_query_handler(text="top")
async def send_top_films(call: types.CallbackQuery):
    stats = get_top_films()
    if not stats:
        return await call.message.answer("🚫 Hali hech qanday film ko‘rilmagan.")

    text = "🌟 <b>TOP 10 eng ko‘p ko‘rilgan kinolar:</b>\n\n"
    for i, (code, views) in enumerate(stats, 1):
        film = get_film_by_code(code)
        if film:
            text += f"{i}. <b>{film['title']}</b> — 👁 {views} ta ko‘rish\n"
    await call.message.answer(text)