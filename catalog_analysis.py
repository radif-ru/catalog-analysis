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


def main():
    print("Hello from catalog-analysis!")


if __name__ == "__main__":
    main()
