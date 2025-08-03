from pathlib import Path

from mkvpy.Tags.base_tags import BaseTags


class MovieTags(BaseTags):
    """Movie-specific tag management class."""

    def __init__(self, file_path: str | Path, language_ietf: str = "und") -> None:
        super().__init__(file_path, language_ietf)

        # Movie-specific properties
        self.title: str = ""
        self.collection: str = ""
        self.director: str = ""
        self.director_photography: str = ""
        self.producer: str = ""
        self.executive_producer: str = ""
        self.writer: list[str] = []
        self.composer: str = ""
        self.genres: list[str] = []
        self.actors_characters: list[tuple[str, str]] = []
        self.synopsis: str = ""
        self.summary: str = ""
        self.description: str = ""
        self.date_released: int = 0
        self.rating: float = 0.0
        self.duration: float = 0.0
        self.total_movies: int = 0
        self.movie_number: int = 0
        self.imdb: str = ""
        self.tmdb: str = ""
        self.country: str = ""
        self.language: str = ""
        self.studio: str = ""
        self.distributor: str = ""
        self.comment: str = ""
        self.subject: str = ""

    def _ordered_info(self) -> dict[tuple[int, str], list[tuple]]:
        """Return ordered movie tag information."""
        return {
            (70, "COLLECTION"): [
                ("COLLECTION", self.collection),
                ("TOTAL_PARTS", self.total_movies),
            ],
            (50, "MOVIE"): [
                ("TITLE", self.title),
                ("PART_NUMBER", self.movie_number),
                ("DIRECTOR", self.director),
                ("DIRECTOR_OF_PHOTOGRAPHY", self.director_photography),
                ("PRODUCER", self.producer),
                ("EXECUTIVE_PRODUCER", self.executive_producer),
                ("WRITTEN_BY", self.writer),
                ("COMPOSER", self.composer),
                ("ACTOR", self.actors_characters),
                ("GENRE", self.genres),
                ("SYNOPSIS", self.synopsis),
                ("SUMMARY", self.summary),
                ("DESCRIPTION", self.description),
                ("DATE_RELEASED", self.date_released),
                ("RATING", self.rating),
                ("DURATION", self.duration),
                ("IMDB", self.imdb),
                ("TMDB", self.tmdb),
                ("COUNTRY", self.country),
                ("LANGUAGE", self.language),
                ("STUDIO", self.studio),
                ("DISTRIBUTOR", self.distributor),
                ("SUBJECT", self.subject),
                ("COMMENT", self.comment),
            ],
        }
