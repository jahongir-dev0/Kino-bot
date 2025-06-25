import json
from aiogram import types
from loader import dp
from utils.db_api.stats import get_top_films

FILM_JSON_PATH = "data/films.json"


def load_films():
    with open(FILM_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


@dp.callback_query_handler(text="top")
async def send_top_films(call: types.CallbackQuery):
    stats = get_top_films()
    if not stats:
        return await call.message.answer("🚫 Hali hech qanday film ko‘rilmagan.")

    films = load_films()
    top_text = "🌟 <b>TOP 10 eng ko‘p ko‘rilgan kinolar:</b>\n\n"
    for i, (code, views) in enumerate(stats, 1):
        film = next((f for f in films if f['code'].lower() == code.lower()), None)
        if film:
            top_text += f"{i}. <b>{film['title']}</b> — 👁 {views} ta ko‘rish\n"
    await call.message.answer(top_text)
