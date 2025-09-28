from pathlib import Path

from mkvpy.Tags.base_tags import BaseTags


class SeriesTags(BaseTags):
    """Series-specific tag management class."""

    def __init__(self, file_path: Path, language_ietf: str = "und") -> None:
        super().__init__(file_path, language_ietf)

        # Series level properties (changed from collection)
        self.series: str = ""
        self.seasons_number: int = 0
        self.series_imdb: str = ""
        self.series_tmdb: str = ""
        self.series_tvdb: str = ""
        self.series_description: str = ""
        self.series_synopsis: str = ""
        self.series_summary: str = ""

        # Season level properties (new for series)
        self.season: str = ""
        self.season_number: int = 0
        self.episodes_season_number: int = 0

        # Episode level properties (changed from movie)
        self.title: str = ""
        self.subtitle: str = ""
        self.episode_number: int = 0
        self.episode_imdb: str = ""
        self.episode_tmdb: str = ""
        self.episode_tvdb: str = ""

        # Cast (in order of appearance/importance)
        self.actors_characters: list[tuple[str, str]] = []

        # Key Creative Roles
        self.directors: list[str] = []
        self.writers: list[str] = []
        self.screenplayers: list[str] = []

        # Production Crew (in typical hierarchy)
        self.producers: list[str] = []
        self.producers_executives: list[str] = []
        self.coproducers: list[str] = []

        # Department Heads
        self.directors_photography: list[str] = []
        self.editors: list[str] = []
        self.designers_production: list[str] = []
        self.designers_costume: list[str] = []

        # Additional Crew
        self.directors_assistant: list[str] = []
        self.mastering_engineers: list[str] = []

        # Production & Distribution
        self.productions_studio: list[str] = []
        self.distributors: list[str] = []
        self.publishers: list[str] = []
        self.locations_recording: list[str] = []

        # Content Classification & Metadata
        self.genres: list[str] = []
        self.rating: float = 0.0
        self.content_type: str = ""
        self.subject: str = ""
        self.keywords: list[str] = []
        self.moods: list[str] = []

        # Descriptions (in order of detail)
        self.description: str = ""
        self.synopsis: str = ""
        self.summary: str = ""
        self.comment: str = ""

        # Dates
        self.date_written: int = 0
        self.date_released: int = 0

        self.load_tags_to_attributes()

    def _info_targets(self) -> dict[int, str]:
        """Return ordered series tag information."""
        return {70: "SERIES", 60: "SEASON", 50: "EPISODE"}
