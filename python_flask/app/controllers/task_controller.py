from flask import render_template, request, redirect, url_for, flash

from app.models.task import MovieModel, Actor


class TaskController:
    def __init__(self):
        self.model = MovieModel()

    def _parse_actors(self, raw_actors: str) -> list[Actor]:
        actors: list[Actor] = []
        for line in raw_actors.splitlines():
            clean_line = line.strip()
            if not clean_line:
                continue
            for sep in (" — ", " - ", ":"):
                if sep in clean_line:
                    name_part, role_part = clean_line.split(sep, 1)
                    actors.append(Actor(full_name=name_part.strip(), role=role_part.strip()))
                    break
            else:
                actors.append(Actor(full_name=clean_line, role="Роль не вказана"))
        return actors

    def index(self):
        movies = self.model.get_all_movies()
        return render_template("tasks/index.html", movies=movies)

    def store(self):
        title = request.form.get("title", "").strip()
        genre = request.form.get("genre", "").strip()
        director = request.form.get("director", "").strip()
        release_year_raw = request.form.get("release_year", "").strip()
        duration_raw = request.form.get("duration_minutes", "").strip()
        studio = request.form.get("studio", "").strip()
        actors_raw = request.form.get("actors", "")

        if not title or not genre or not director or not studio:
            flash("Заповніть обов'язкові поля фільму!", "error")
            return redirect(url_for("index"))

        try:
            release_year = int(release_year_raw)
            duration_minutes = int(duration_raw)
        except ValueError:
            flash("Рік випуску та тривалість мають бути числами!", "error")
            return redirect(url_for("index"))

        actors = self._parse_actors(actors_raw)

        if self.model.add_movie(
            title=title,
            genre=genre,
            director=director,
            release_year=release_year,
            duration_minutes=duration_minutes,
            studio=studio,
            actors=actors,
        ):
            flash("Фільм додано!", "success")
        else:
            flash("Не вдалося додати фільм", "error")

        return redirect(url_for("index"))

    def mark_done(self, task_id: int):
        movie = self.model.get_movie_by_id(task_id)
        if movie:
            flash(f"Переглянуто акторський склад фільму «{movie.title}»", "success")
        else:
            flash("Фільм не знайдено", "error")
        return redirect(url_for("index"))

    def delete(self, task_id: int):
        if self.model.delete_movie(task_id):
            flash("Фільм видалено!", "success")
        else:
            flash("Фільм не знайдено", "error")
        return redirect(url_for("index"))