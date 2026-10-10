# catalog-analysis

Анализ каталога фильмов стримингового сервиса на чистом Python.

[![CI](https://github.com/radif-ru/catalog-analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/radif-ru/catalog-analysis/actions/workflows/ci.yml)
[![Python 3.12](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-package%20manager-DE5FE9?logo=uv&logoColor=white)](https://docs.astral.sh/uv/)
[![Ruff](https://img.shields.io/badge/ruff-linter-D7FF64?logo=ruff)](https://docs.astral.sh/ruff/)
[![Dependencies](https://img.shields.io/badge/dependencies-stdlib%20only-success?logo=python&logoColor=white)](https://docs.python.org/3.12/library/)

Проект выполнен в рамках дисциплины «Программирование на Python» магистерской
программы [«Обработка данных и применение искусственного интеллекта»](https://eis2.mephi.ru/programs/Program/Details/1354)
(направление 01.04.02 «Прикладная математика и информатика»),
[Институт интеллектуальных кибернетических систем](https://icis.mephi.ru/)
[НИЯУ МИФИ](https://mephi.ru/).

## Задача

Внутренний отчёт по каталогу фильмов стримингового сервиса: базовая статистика,
категоризация по рейтингу и периоду выпуска, отчёты по жанрам и актёрам,
топ-списки. Всё реализовано вручную на чистом Python без pandas — так видно,
что однострочники библиотек делают под капотом.

## Принципы реализации

- Только стандартная библиотека: единственный импорт для вычислений — `math`.
- Процедурный стиль без классов; структура записи описана через `TypedDict`.
- Каждая функция использует языковую конструкцию, заданную её этапом
  (тернарный оператор, `match`, `while`/`break`/`else`, `dict.get`,
  операции над множествами, `yield`, генераторные выражения).
- Аннотации типов и docstring с примерами в формате doctest у всех функций.
- Линт и форматирование — ruff (правила E, F, I); проверки запускаются в CI.

## Этапы

| № | Тема | Функции | Ключевые конструкции |
|---|------|---------|----------------------|
| 1 | Числа и math | `average_rating`, `catalog_age_stats`, `duration_in_hours` | `round`, `math.ceil`, `//`, `%` |
| 2 | Условия и match | `rating_tier`, `decade_label` | `if`/`elif`, тернарный оператор, `match` + `case _ if` |
| 3 | Циклы | `print_non_comedy_titles`, `find_first_masterpiece`, `count_long_movies` | `for` + `continue`, `while` + `break` + `else`, счётчик |
| 4 | Строки | `normalize_title`, `make_slug`, `format_report_line` | срезы, `split`/`join`, f-строки |
| 5 | Списки | `top_movies`, `top_n_by_rating`, `titles_sorted_by_rating` | `sorted(key=)`, срезы, кортежи |
| 6 | Словари | `count_by_genre`, `actor_filmography`, `above_average_ratings` | `dict.get`, dict comprehension |
| 7 | Множества | `all_genres`, `common_actors`, `genres_only_in_one` | `\|`, `&`, `-` |
| 8 | Итераторы и генераторы | `iter_high_rated`, `print_high_rated`, `total_duration_above` | `yield`, genexpr внутри `sum()` |
| 9 | Итоговый отчёт | `build_report`, `run_demos` | композиция функций всех этапов |

## Запуск

Нужен [uv](https://docs.astral.sh/uv/):

```bash
uv sync
uv run catalog_analysis.py
```

## Проверки

```bash
uv run ruff check .
uv run ruff format --check .
uv run python -m doctest catalog_analysis.py
```

## Пример вывода

```text
ОТЧЁТ ПО КАТАЛОГУ
Средний рейтинг: 7.2
Средний возраст фильмов: 8 лет

Топ-3 фильма:
  "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi
  "Midnight In Oslo" (2020) — 8.9/10, 2ч 4м, жанры: mystery, thriller
  "The Dune Chronicles" (2021) — 8.6/10, 2ч 35м, жанры: drama, sci-fi

Фильмов по жанрам:
  drama — 5
  comedy — 3
  sci-fi — 3
  thriller — 3
  action — 2
  mystery — 1

Все жанры каталога: action, comedy, drama, mystery, sci-fi, thriller
```

## Структура проекта

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml          # проверки в CI: ruff, запуск, doctest
├── .gitignore
├── .python-version         # закреплённая версия Python
├── catalog_analysis.py     # весь код: данные, функции этапов, отчёт
├── pyproject.toml          # метаданные проекта и настройки ruff
├── README.md
└── uv.lock                 # зафиксированные версии зависимостей
```

---

Автор — [Радиф Илалтдинов](https://radif.ru)
