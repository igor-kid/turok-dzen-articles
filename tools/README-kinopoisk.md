# Kinopoisk Unofficial API

Используется для автоматической проверки названий сериалов и фильмов.

- **Base**: `https://kinopoiskapiunofficial.tech`
- **Заголовок**: `X-API-KEY`
- **Поиск**: `GET /api/v2.1/films/search-by-keyword?keyword=...`
- **Карточка**: `GET /api/v2.2/films/{id}`

Скрипт: `kinopoisk_check.py`

Пример:
```bash
python3 tools/kinopoisk_check.py "Полнолуние"
```

Выдаёт:
```
Полнолуние (Dolunay, 2017) [TV_SERIES]  id:1046960
```

Дата настройки: 2026-11-14
