from pathlib import Path

from mkvpy.Tags.base_tags import BaseTags


class EpisodeTags(BaseTags):
    """Episode-specific tag management class."""

    def __init__(self, file_path: str | Path, language_ietf: str = "und") -> None:
        super().__init__(file_path, language_ietf)

        # Episode-specific properties
        self.series_title: str = ""
        self.season_number: int = 0
        self.total_seasons: int = 0
        self.episode_number: int = 0
        self.total_episodes: int = 0
        self.title: str = ""
        self.director: str = ""
        self.director_photography: str = ""
        self.producer: str = ""
        self.executive_producer: str = ""
        self.writer: list[str] = []
        self.actors_characters: list[tuple[str, str]] = []
        self.synopsis: str = ""
        self.summary: str = ""
        self.description: str = ""
        self.date_episode: int = 0
        self.genres: list[str] = []
        self.rating: float = 0.0
        self.imdb: str = ""
        self.tvdb: str = ""
        self.tmdb: str = ""
        self.language: str = ""
        self.network: str = ""
        self.studio: str = ""
        self.comment: str = ""

    def _ordered_info(self) -> dict[tuple[int, str], list[tuple]]:
        """Return ordered episode tag information."""
        return {
            (70, "COLLECTION"): [
                ("COLLECTION", self.series_title),
                ("TOTAL_PARTS", self.total_seasons),
            ],
            (60, "SEASON"): [
                ("PART_NUMBER", self.season_number),
                ("TOTAL_PARTS", self.total_episodes),
            ],
            (50, "EPISODE"): [
                ("TITLE", self.title),
                ("PART_NUMBER", self.episode_number),
                ("DIRECTOR", self.director),
                ("DIRECTOR_OF_PHOTOGRAPHY", self.director_photography),
                ("PRODUCER", self.producer),
                ("EXECUTIVE_PRODUCER", self.executive_producer),
                ("WRITTEN_BY", self.writer),
                ("ACTOR", self.actors_characters),
                ("GENRE", self.genres),
                ("SYNOPSIS", self.synopsis),
                ("SUMMARY", self.summary),
                ("DESCRIPTION", self.description),
                ("DATE_RELEASED", self.date_episode),
                ("RATING", self.rating),
                ("IMDB", self.imdb),
                ("TVDB", self.tvdb),
                ("TMDB", self.tmdb),
                ("LANGUAGE", self.language),
                ("NETWORK", self.network),
                ("STUDIO", self.studio),
                ("COMMENT", self.comment),
            ],
        }
