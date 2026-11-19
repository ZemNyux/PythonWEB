from dataclasses import dataclass, field
from typing import List


@dataclass
class Actor:
    full_name: str
    role: str


@dataclass
class Movie:
    id: int
    title: str
    genre: str
    director: str
    release_year: int
    duration_minutes: int
    studio: str
    actors: List[Actor] = field(default_factory=list)


class MovieModel:
    def __init__(self):
        self._movies: List[Movie] = []
        self._next_id = 1
        self._seed_data()

    def _seed_data(self):
        taxi_5_actors = [
            Actor("Франк Гастамбид (Franck Gastambide)", "Сильвен Маро (инспектор полиции)"),
            Actor("Малик Бенталха (Malik Bentalha)", "Эдди Маклуф (племянник Даниэля)"),
            Actor("Бернар Фарси (Bernard Farcy)", "Жерар Жибер (мэр Марселя, бывший комиссар)"),
            Actor("Сабрина Уазани (Sabrina Ouazani)", "Самия Маклуф (сестра Эдди)"),
            Actor("Сальваторе Эспозито (Salvatore Esposito)", "Тони Дог (главарь «банды итальянцев»)"),
            Actor("Эдуар Монтут (Édouard Montoute)", "Ален Трезор (инспектор полиции)"),
            Actor("Санд Ван Рой (Sand Van Roy)", "Сэнди"),
            Actor("Ануар Тубали (Anouar Toubali)", "Мишель Петруччиани"),
            Actor("Месье Пульп (Monsieur Poulpe)", "Менар"),
            Actor("Сисси Дюпарк (Sissi Duparc)", "Сандрин Броссар"),
            Actor("Рамзи Бедиа (Ramzy Bedia)", "Рашид"),
            Actor("Мусса Мааскри (Moussa Maaskri)", "Лопес"),
            Actor("Эрик Фратичелли (Eric Fraticelli)", "Паоли"),
            Actor("Сопрано (Soprano)", "Баба"),
            Actor("Франсуа Леванталь (François Levantal)", "Комиссар Морзини"),
            Actor("Элиза Ларниколь (Elise Larnicol)", "Министр экологии"),
            Actor("Ромен Ланкри (Romain Lancry)", "Бишон"),
            Actor("Фабрицио Невола (Fabrizio Nevola)", "Рокко"),
            Actor("Фатса Буяхмед (Fatsah Bouyahmed)", "Дядя Хамид"),
        ]

        self.add_movie(
            title="Такси 5 (Taxi 5)",
            genre="Боевик, комедия, криминал, приключения",
            director="Франк Гастамбид",
            release_year=2018,
            duration_minutes=102,
            studio="EuropaCorp",
            actors=taxi_5_actors
        )

    def add_movie(
        self,
        title: str,
        genre: str,
        director: str,
        release_year: int,
        duration_minutes: int,
        studio: str,
        actors: List[Actor] = None
    ) -> bool:
        clean_title = title.strip()
        if not clean_title:
            return False

        movie = Movie(
            id=self._next_id,
            title=clean_title,
            genre=genre.strip(),
            director=director.strip(),
            release_year=int(release_year),
            duration_minutes=int(duration_minutes),
            studio=studio.strip(),
            actors=actors or []
        )
        self._movies.append(movie)
        self._next_id += 1
        return True

    def get_all_movies(self) -> List[Movie]:
        return self._movies.copy()

    def get_movie_by_id(self, movie_id: int) -> Movie | None:
        for movie in self._movies:
            if movie.id == movie_id:
                return movie
        return None

    def delete_movie(self, movie_id: int) -> bool:
        initial_len = len(self._movies)
        self._movies = [m for m in self._movies if m.id != movie_id]
        return len(self._movies) < initial_len