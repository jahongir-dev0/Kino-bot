import json
import os
import random

FILM_JSON_PATH = "data/films.json"

def ensure_film_file():
    """Agar film fayli mavjud bo'lmasa, uni yaratadi."""
    if not os.path.exists(FILM_JSON_PATH):
        with open(FILM_JSON_PATH, "w", encoding="utf-8") as f:
            f.write("[]")

def load_films() -> list:
    """Barcha filmlarni yuklab beradi."""
    ensure_film_file()
    try:
        with open(FILM_JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_film(film_data: dict):
    """Yangi filmni json faylga qo'shadi."""
    films = load_films()
    films.append(film_data)
    with open(FILM_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(films, f, indent=2, ensure_ascii=False)

def get_film_by_code(code: str):
    """Kod bo'yicha filmni topadi."""
    code = code.lower().strip()
    films = load_films()
    return next((f for f in films if f['code'].lower() == code), None)

def search_film_by_name(name: str):
    """Nom bo'yicha film qidiradi (qisman)."""
    name = name.lower().strip()
    films = load_films()
    return [f for f in films if name in f["title"].lower()]

def get_random_film():
    """Tasodifiy filmni tanlaydi."""
    films = load_films()
    return random.choice(films) if films else None
