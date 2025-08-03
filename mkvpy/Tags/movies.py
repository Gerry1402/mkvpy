from pathlib import Path

from mkvpy.Tags.base_tags import BaseTags


class MovieTags(BaseTags):
    """Movie-specific tag management class."""

    def __init__(self, file_path: str | Path, language_ietf: str = "und") -> None:
        super().__init__(file_path, language_ietf)

        # Collection level properties
        self.collection: str = ""
        self.movies_number: int = 0
        self.collection_imdb: str = ""
        self.collection_tmdb: str = ""

        # Movie level properties
        self.title: str = ""
        self.movie_number: int = 0
        self.movie_imdb: str = ""
        self.movie_tmdb: str = ""
        self.movie_tvdb: str = ""

        # Cast and crew
        self.directors: list[str] = []
        self.directors_assistant: list[str] = []
        self.directors_photography: list[str] = []
        self.designers_production: list[str] = []
        self.designers_costume: list[str] = []
        self.actors_characters: list[tuple[str, str]] = []
        self.writers: list[str] = []
        self.screenplayers: list[str] = []
        self.editors: list[str] = []
        self.producers: list[str] = []
        self.coproducers: list[str] = []
        self.producers_executives: list[str] = []
        self.distributors: list[str] = []
        self.mastering_engineers: list[str] = []
        self.productions_studio: list[str] = []
        self.publishers: list[str] = []
        self.locations_recording: list[str] = []

        # Content metadata
        self.genres: list[str] = []
        self.keywords: list[str] = []
        self.moods: list[str] = []
        self.rating: float = 0.0
        self.content_type: str = ""
        self.subject: str = ""
        self.description: str = ""
        self.synopsis: str = ""
        self.summary: str = ""
        self.comment: str = ""

        # Dates
        self.date_written: int = 0
        self.date_released: int = 0

    def _ordered_info(self) -> dict[tuple[int, str], list[tuple]]:
        """Return ordered movie tag information."""
        return {
            (70, "COLLECTION"): [
                ("TITLE", self.collection),
                ("TOTAL_PARTS", self.movies_number),
                ("IMDB", self.collection_imdb),
                ("TMDB", self.collection_tmdb),
            ],
            (50, "MOVIE"): [
                ("TITLE", self.title),
                ("PART_NUMBER", self.movie_number),
                ("IMDB", self.movie_imdb),
                ("TMDB", self.movie_tmdb),
                ("TVDB", self.movie_tvdb),
                ("DIRECTOR", self.directors),
                ("ASSISTANT_DIRECTOR", self.directors_assistant),
                ("DIRECTOR_OF_PHOTOGRAPHY", self.directors_photography),
                ("PRODUCTION_DESIGNER", self.designers_production),
                ("COSTUME_DESIGNER", self.designers_costume),
                ("ACTOR", self.actors_characters),
                ("WRITTEN_BY", self.writers),
                ("SCREENPLAY_BY", self.screenplayers),
                ("EDITOR", self.editors),
                ("PRODUCER", self.producers),
                ("COPRODUCER", self.coproducers),
                ("EXECUTIVE_PRODUCER", self.producers_executives),
                ("DISTRIBUTED_BY", self.distributors),
                ("MASTERED_BY", self.mastering_engineers),
                ("PRODUCTION_STUDIO", self.productions_studio),
                ("PUBLISHER", self.publishers),
                ("RECORDING_LOCATION", self.locations_recording),
                ("GENRE", self.genres),
                ("KEYWORDS", self.keywords),
                ("MOOD", self.moods),
                ("RATING", self.rating),
                ("CONTENT_TYPE", self.content_type),
                ("SUBJECT", self.subject),
                ("DESCRIPTION", self.description),
                ("SYNOPSIS", self.synopsis),
                ("SUMMARY", self.summary),
                ("COMMENT", self.comment),
                ("DATE_WRITTEN", self.date_written),
                ("DATE_RELEASED", self.date_released),
            ],
        }
