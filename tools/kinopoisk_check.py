#!/usr/bin/env python3
"""
Проверка названий сериалов/фильмов через Kinopoisk Unofficial API.
Использование: python3 kinopoisk_check.py "Полнолуние"
"""
import sys
import requests

API_KEY = "4abc7c56-a6bd-45fe-b82d-aeeb1d8c90c0"
BASE = "https://kinopoiskapiunofficial.tech"

def search(keyword: str, limit: int = 5):
    url = f"{BASE}/api/v2.1/films/search-by-keyword"
    headers = {"X-API-KEY": API_KEY, "accept": "application/json"}
    params = {"keyword": keyword}
    r = requests.get(url, headers=headers, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()
    films = data.get("films", [])[:limit]
    return films

def get_details(film_id: int):
    url = f"{BASE}/api/v2.2/films/{film_id}"
    headers = {"X-API-KEY": API_KEY, "accept": "application/json"}
    r = requests.get(url, headers=headers, timeout=15)
    r.raise_for_status()
    return r.json()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Укажи название: python3 kinopoisk_check.py \"Полнолуние\"")
        sys.exit(1)
    query = " ".join(sys.argv[1:])
    results = search(query)
    if not results:
        print("Ничего не найдено")
        sys.exit(0)
    for f in results:
        name_ru = f.get("nameRu") or "—"
        name_orig = f.get("nameEn") or f.get("nameOriginal") or "—"
        year = f.get("year") or "—"
        typ = f.get("type", "")
        film_id = f.get("filmId")
        print(f"{name_ru} ({name_orig}, {year}) [{typ}]  id:{film_id}")

        # Подтягиваем рейтинг и жанры из полной карточки
        try:
            details = get_details(film_id)
            rating = details.get("ratingKinopoisk")
            votes = details.get("ratingKinopoiskVoteCount")
            genres = ", ".join(g.get("genre", "") for g in details.get("genres", []))
            print(f"  Рейтинг КП: {rating} ({votes} голосов)")
            print(f"  Жанры: {genres or '—'}")
        except Exception as e:
            print(f"  (не удалось получить детали: {e})")
        print()
