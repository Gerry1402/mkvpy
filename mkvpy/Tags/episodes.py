from __future__ import annotations

from dataclasses import dataclass

from mkvpy.Tags.base_tags import BaseTags


@dataclass
class EpisodeTags(BaseTags):
    # Series level properties
    series: str | None = None
    seasons_number: int | None = None
    series_imdb: str | None = None
    series_tmdb: str | None = None
    series_tvdb: str | None = None
    series_description: str | None = None
    series_synopsis: str | None = None
    series_summary: str | None = None

    # Season level properties
    season: str | None = None
    season_number: int | None = None
    episodes_season_number: int | None = None

    # Episode level properties
    title: str | None = None
    subtitle: str | None = None
    episode_number: int | None = None
    episode_imdb: str | None = None
    episode_tmdb: str | None = None
    episode_tvdb: str | None = None

    # Cast
    actors_characters: list[tuple[str, str]] | None = None

    # Key Creative Roles
    directors: list[str] | None = None
    writers: list[str] | None = None
    screenplayers: list[str] | None = None

    # Production Crew
    producers: list[str] | None = None
    producers_executives: list[str] | None = None
    coproducers: list[str] | None = None

    # Department Heads
    directors_photography: list[str] | None = None
    editors: list[str] | None = None
    designers_production: list[str] | None = None
    designers_costume: list[str] | None = None

    # Additional Crew
    directors_assistant: list[str] | None = None
    mastering_engineers: list[str] | None = None

    # Production & Distribution
    productions_studio: list[str] | None = None
    distributors: list[str] | None = None
    publishers: list[str] | None = None
    locations_recording: list[str] | None = None

    # Content Classification & Metadata
    genres: list[str] | None = None
    rating: float | None = None
    content_type: str | None = None
    subject: str | None = None
    keywords: list[str] | None = None
    moods: list[str] | None = None

    # Descriptions
    description: str | None = None
    synopsis: str | None = None
    summary: str | None = None
    comment: str | None = None

    # Dates
    date_written: int | None = None
    date_released: int | None = None

    def __post_init__(self):
        pass

    def _info_targets(self) -> dict[int, str]:
        """Return ordered episode tag information."""
        return {70: "COLLECTION", 60: "SEASON", 50: "EPISODE"}
