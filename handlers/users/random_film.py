import os
import json
import random
from aiogram import types
from loader import dp

FILM_JSON_PATH = "data/films.json"

def get_random_film():
    if not os.path.exists(FILM_JSON_PATH):
        with open(FILM_JSON_PATH, "w", encoding="utf-8") as f:
            f.write("[]")

    try:
        with open(FILM_JSON_PATH, "r", encoding="utf-8") as f:
            films = json.load(f)
            return random.choice(films) if films else None
    except json.JSONDecodeError:
        return None

@dp.callback_query_handler(text="random")
async def send_random_film(call: types.CallbackQuery):
    film = get_random_film()
    if not film:
        await call.message.answer("🚫 Film bazasi bo‘sh.")
        return

    await call.message.answer_video(
        video=film["file_id"],
        caption=f"<b>{film['title']}</b>\nDavlat: {film['country']}\nYil: {film['year']}\nDavomiylik: {film['duration']}\nKod: <code>{film['code']}</code>"
    )
