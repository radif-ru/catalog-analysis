"""Анализ каталога фильмов стримингового сервиса на чистом Python."""

import math
from typing import TypedDict


class Movie(TypedDict):
    """Запись о фильме в каталоге."""

    title: str
    year: int
    genres: set[str]
    rating: float
    duration_min: int
    actors: list[str]


# fmt: off
movies: list[Movie] = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},  # noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]
# fmt: on


# --- Этап 1. Числа и math ---


def average_rating(movies: list[Movie]) -> float:
    """Возвращает средний рейтинг каталога, округлённый до одного знака.

    >>> average_rating(movies)
    7.2
    """
    return round(sum(movie["rating"] for movie in movies) / len(movies), 1)


def catalog_age_stats(
    movies: list[Movie], current_year: int = 2026
) -> tuple[int, int, int]:
    """Возвращает возраст самого старого и самого нового фильма и средний.

    Средний возраст округляется вверх до целого числа лет через math.ceil.

    >>> catalog_age_stats(movies)
    (15, 2, 8)
    """
    ages = [current_year - movie["year"] for movie in movies]
    return max(ages), min(ages), math.ceil(sum(ages) / len(ages))


def duration_in_hours(minutes: int) -> str:
    """Переводит длительность в минутах в строку вида «2ч 35м».

    >>> duration_in_hours(155)
    '2ч 35м'
    >>> duration_in_hours(124)
    '2ч 4м'
    """
    return f"{minutes // 60}ч {minutes % 60}м"


# --- Этап 2. Условия и match ---


def rating_tier(rating: float) -> str:
    """Возвращает категорию оценки: «шедевр», «хорошо», «средне» или «слабо».

    >>> rating_tier(9.0)
    'шедевр'
    >>> rating_tier(8.9)
    'хорошо'
    >>> rating_tier(7.0)
    'хорошо'
    >>> rating_tier(5.0)
    'средне'
    >>> rating_tier(4.9)
    'слабо'
    """
    if rating >= 7:
        return "шедевр" if rating >= 9 else "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"


def decade_label(year: int) -> str:
    """Возвращает метку периода выпуска: «новые», «недавние» или «старые».

    >>> decade_label(2021)
    'новые'
    >>> decade_label(2020)
    'недавние'
    >>> decade_label(2015)
    'недавние'
    >>> decade_label(2014)
    'старые'
    """
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# --- Этап 3. Циклы ---


def print_non_comedy_titles(movies: list[Movie]) -> None:
    """Печатает названия фильмов, не относящихся к жанру «comedy».

    >>> print_non_comedy_titles(movies)
    The Dune Chronicles
    silent hours
    Comet Racers
    midnight in oslo
    Garden of Static
    The Quiet Algorithm
    Red Harbor
    """
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies: list[Movie], threshold: float = 9.0) -> Movie | None:
    """Ищет первый по порядку фильм с рейтингом выше threshold.

    Цикл while прерывается через break при первой находке; ветка else
    срабатывает, когда подходящих фильмов в списке нет.

    >>> found = find_first_masterpiece(movies)
    Первый шедевр: "The Quiet Algorithm" — 9.2
    >>> found["title"]
    'The Quiet Algorithm'
    >>> find_first_masterpiece([m for m in movies if m["rating"] <= 9.0])
    Шедевров не найдено
    """
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > threshold:
            print(f'Первый шедевр: "{movie["title"]}" — {movie["rating"]}')
            break
        index += 1
    else:
        print("Шедевров не найдено")
        return None
    return movie


def count_long_movies(movies: list[Movie], threshold: int = 120) -> int:
    """Считает фильмы длиннее threshold минут накоплением счётчика в цикле.

    >>> count_long_movies(movies)
    4
    >>> count_long_movies(movies, 130)
    2
    """
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# --- Этап 4. Строки ---


def normalize_title(title: str) -> str:
    """Приводит название к виду Title Case вручную, без str.title().

    >>> normalize_title("silent hours")
    'Silent Hours'
    """
    return " ".join(word[0].upper() + word[1:] for word in title.split())


def make_slug(title: str) -> str:
    """Превращает нормализованное название в слаг вида «the-quiet-algorithm».

    >>> make_slug("Silent Hours")
    'silent-hours'
    """
    return title.lower().replace(" ", "-")


def format_report_line(movie: Movie) -> str:
    """Собирает единую строку описания фильма через f-строку.

    >>> format_report_line(movies[7])
    '"The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi'
    """
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{normalize_title(movie["title"])}" ({movie["year"]})'
        f" — {movie['rating']}/10, {duration_in_hours(movie['duration_min'])},"
        f" жанры: {genres}"
    )


# --- Этап 5. Списки ---


def top_movies(movies: list[Movie], n: int = 3) -> list[Movie]:
    """Возвращает n фильмов с наивысшим рейтингом.

    >>> [movie["title"] for movie in top_movies(movies)]
    ['The Quiet Algorithm', 'midnight in oslo', 'The Dune Chronicles']
    """
    return sorted(movies, key=lambda movie: movie["rating"], reverse=True)[:n]


def top_n_by_rating(movies: list[Movie], n: int = 3) -> list[tuple[str, float]]:
    """Возвращает топ-n кортежей (название, рейтинг) по убыванию рейтинга.

    >>> top_n_by_rating(movies, 2)
    [('The Quiet Algorithm', 9.2), ('midnight in oslo', 8.9)]
    """
    return [(movie["title"], movie["rating"]) for movie in top_movies(movies, n)]


def titles_sorted_by_rating(movies: list[Movie]) -> list[str]:
    """Возвращает названия всех фильмов по убыванию рейтинга, не меняя вход.

    >>> titles_sorted_by_rating(movies)[:3]
    ['The Quiet Algorithm', 'midnight in oslo', 'The Dune Chronicles']
    """
    ordered = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in ordered]


def main():
    print("Hello from catalog-analysis!")


if __name__ == "__main__":
    main()
