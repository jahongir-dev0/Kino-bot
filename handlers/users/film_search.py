import os

import json
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loader import dp
from states.film_search import FilmSearch

FILM_JSON_PATH = "data/films.json"

def load_films():
    if not os.path.exists(FILM_JSON_PATH):
        with open(FILM_JSON_PATH, "w", encoding="utf-8") as f:
            f.write("[]")
    with open(FILM_JSON_PATH, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

@dp.callback_query_handler(text="search_by_name")
async def ask_film_name(call: types.CallbackQuery):
    await call.message.edit_text("🎬 Kino nomini yuboring:")
    await FilmSearch.by_name.set()

@dp.message_handler(state=FilmSearch.by_name)
async def search_by_name(message: types.Message, state: FSMContext):
    films = load_films()
    name = message.text.lower()
    for film in films:
        if name in film['title'].lower():
            await message.answer_video(
                video=film["file_id"],
                caption=f"<b>{film['title']}</b>\nDavlat: {film['country']}\nYil: {film['year']}\nDavomiylik: {film['duration']}\nKod: <code>{film['code']}</code>"
            )
            await state.finish()
            return
    await message.answer("🚫 Kino topilmadi.")
    await state.finish()

@dp.callback_query_handler(text="search_by_code")
async def ask_film_code(call: types.CallbackQuery):
    await call.message.edit_text("🔐 Kino KODini yuboring:")
    await FilmSearch.by_code.set()

@dp.message_handler(state=FilmSearch.by_code)
async def search_by_code(message: types.Message, state: FSMContext):
    films = load_films()
    code = message.text.strip().lower()
    for film in films:
        if code == film['code'].lower():
            await message.answer_video(
                video=film["file_id"],
                caption=f"<b>{film['title']}</b>\nDavlat: {film['country']}\nYil: {film['year']}\nDavomiylik: {film['duration']}\nKod: <code>{film['code']}</code>"
            )
            await state.finish()
            return
    await message.answer("🚫 Kod bo‘yicha kino topilmadi.")
    await state.finish()
