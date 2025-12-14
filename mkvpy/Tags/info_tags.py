from __future__ import annotations

info_targets: dict[str, int] = {"COLLECTION": 70, "SEASON": 60, "MOVIE": 50, "EPISODE": 50}

info_tags: dict[str, dict[str, str | tuple | bool | int]] = {
    # Target Type Value 70:
    # Movie
    "collection": {"name": "TITLE", "unique": True, "target": 70},
    "movies_number": {"name": "TOTAL_PARTS", "unique": True, "target": 70},
    "collection_imdb": {"name": "IMDB", "unique": True, "target": 70},
    "collection_tmdb": {"name": "TMDB", "unique": True, "target": 70},
    "collection_description": {"name": "DESCRIPTION", "unique": True, "target": 70},
    "collection_synopsis": {"name": "SYNOPSIS", "unique": True, "target": 70},
    "collection_summary": {"name": "SUMMARY", "unique": True, "target": 70},
    # TV Series
    "series": {"name": "TITLE", "unique": True, "target": 70},
    "seasons_number": {"name": "TOTAL_PARTS", "unique": True, "target": 70},
    "series_imdb": {"name": "IMDB", "unique": True, "target": 70},
    "series_tmdb": {"name": "TMDB", "unique": True, "target": 70},
    "series_tvdb": {"name": "TVDB2", "unique": True, "target": 70},
    "series_description": {"name": "DESCRIPTION", "unique": True, "target": 70},
    "series_synopsis": {"name": "SYNOPSIS", "unique": True, "target": 70},
    "series_summary": {"name": "SUMMARY", "unique": True, "target": 70},
    # Target Type Value 60:
    # TV Series
    "season": {"name": "TITLE", "unique": True, "target": 60},
    "season_number": {"name": "PART_NUMBER", "unique": True, "target": 60},
    "episodes_season_number": {"name": "TOTAL_PARTS", "unique": True, "target": 60},
    # Target Type Value 50:
    # Movie
    "movie_number": {"name": "PART_NUMBER", "unique": True, "target": 50},
    "movie_imdb": {"name": "IMDB", "unique": True, "target": 50},
    "movie_tmdb": {"name": "TMDB", "unique": True, "target": 50},
    "movie_tvdb": {"name": "TVDB2", "unique": True, "target": 50},
    # TV Series
    "episode_number": {"name": "PART_NUMBER", "unique": True, "target": 50},
    "episode_imdb": {"name": "IMDB", "unique": True, "target": 50},
    "episode_tmdb": {"name": "TMDB", "unique": True, "target": 50},
    "episode_tvdb": {"name": "TVDB2", "unique": True, "target": 50},
    # Common
    "title": {"name": "TITLE", "unique": True, "target": 50},
    "subtitle": {"name": "SUBTITLE", "unique": True, "target": 50},
    # Cast (in order of appearance/importance)
    "actors_characters": {"name": ("ACTOR", "CHARACTER"), "unique": False, "target": 50},
    # Key Creative Roles
    "directors": {"name": "DIRECTOR", "unique": False, "target": 50},
    "writers": {"name": "WRITTEN_BY", "unique": False, "target": 50},
    "screenplayers": {"name": "SCREENPLAY_BY", "unique": False, "target": 50},
    # Production Crew (in typical hierarchy)
    "producers": {"name": "PRODUCER", "unique": False, "target": 50},
    "producers_executives": {"name": "EXECUTIVE_PRODUCER", "unique": False, "target": 50},
    "coproducers": {"name": "COPRODUCER", "unique": False, "target": 50},
    # Department Heads
    "directors_photography": {"name": "DIRECTOR_OF_PHOTOGRAPHY", "unique": False, "target": 50},
    "editors": {"name": "EDITOR", "unique": False, "target": 50},
    "designers_production": {"name": "PRODUCTION_DESIGNER", "unique": False, "target": 50},
    "designers_costume": {"name": "COSTUME_DESIGNER", "unique": False, "target": 50},
    # Additional Crew
    "directors_assistant": {"name": "ASSISTANT_DIRECTOR", "unique": False, "target": 50},
    "mastering_engineers": {"name": "MASTERED_BY", "unique": False, "target": 50},
    # Production & Distribution
    "productions_studio": {"name": "PRODUCTION_STUDIO", "unique": False, "target": 50},
    "distributors": {"name": "DISTRIBUTED_BY", "unique": False, "target": 50},
    "publishers": {"name": "PUBLISHER", "unique": False, "target": 50},
    "locations_recording": {"name": "RECORDING_LOCATION", "unique": False, "target": 50},
    # Content Classification & Metadata
    "genres": {"name": "GENRE", "unique": False, "target": 50},
    "rating": {"name": "RATING", "unique": True, "target": 50},
    "content_type": {"name": "CONTENT_TYPE", "unique": True, "target": 50},
    "subject": {"name": "SUBJECT", "unique": True, "target": 50},
    "keywords": {"name": "KEYWORDS", "unique": False, "target": 50},
    "moods": {"name": "MOOD", "unique": False, "target": 50},
    # Descriptions (in order of detail)
    "description": {"name": "DESCRIPTION", "unique": False, "target": 50},
    "synopsis": {"name": "SYNOPSIS", "unique": False, "target": 50},
    "summary": {"name": "SUMMARY", "unique": False, "target": 50},
    "comment": {"name": "COMMENT", "unique": False, "target": 50},
    # Dates
    "date_written": {"name": "DATE_WRITTEN", "unique": True, "target": 50},
    "date_released": {"name": "DATE_RELEASED", "unique": True, "target": 50},
}

# Ordered list of all available tag keys
order_tags: list[str] = [
    # Target Type Value 70: Collection/Series Level
    "collection",
    "movies_number",
    "collection_imdb",
    "collection_tmdb",
    "collection_description",
    "collection_synopsis",
    "collection_summary",
    "series",
    "seasons_number",
    "series_imdb",
    "series_tmdb",
    "series_tvdb",
    "series_description",
    "series_synopsis",
    "series_summary",
    # Target Type Value 60: Season Level
    "season",
    "season_number",
    "episodes_season_number",
    # Target Type Value 50: Movie/Episode Level
    "movie_number",
    "movie_imdb",
    "movie_tmdb",
    "movie_tvdb",
    "episode_number",
    "episode_imdb",
    "episode_tmdb",
    "episode_tvdb",
    "title",
    "subtitle",
    "actors_characters",
    "directors",
    "writers",
    "screenplayers",
    "producers",
    "producers_executives",
    "coproducers",
    "directors_photography",
    "editors",
    "designers_production",
    "designers_costume",
    "directors_assistant",
    "mastering_engineers",
    "productions_studio",
    "distributors",
    "publishers",
    "locations_recording",
    "genres",
    "rating",
    "content_type",
    "subject",
    "keywords",
    "moods",
    "description",
    "synopsis",
    "summary",
    "comment",
    "date_written",
    "date_released",
]

common_tags_by_target: dict[str | tuple, dict] = {
    "TITLE": {"name": "title", "unique": True},
    "SUBTITLE": {"name": "subtitle", "unique": True},
    ("ACTOR", "CHARACTER"): {"name": "actors_characters", "unique": False},
    "DIRECTOR": {"name": "directors", "unique": False},
    "WRITTEN_BY": {"name": "writers", "unique": False},
    "SCREENPLAY_BY": {"name": "screenplayers", "unique": False},
    "PRODUCER": {"name": "producers", "unique": False},
    "EXECUTIVE_PRODUCER": {"name": "producers_executives", "unique": False},
    "COPRODUCER": {"name": "coproducers", "unique": False},
    "DIRECTOR_OF_PHOTOGRAPHY": {"name": "directors_photography", "unique": False},
    "EDITOR": {"name": "editors", "unique": False},
    "PRODUCTION_DESIGNER": {"name": "designers_production", "unique": False},
    "COSTUME_DESIGNER": {"name": "designers_costume", "unique": False},
    "ASSISTANT_DIRECTOR": {"name": "directors_assistant", "unique": False},
    "MASTERED_BY": {"name": "mastering_engineers", "unique": False},
    "PRODUCTION_STUDIO": {"name": "productions_studio", "unique": False},
    "DISTRIBUTED_BY": {"name": "distributors", "unique": False},
    "PUBLISHER": {"name": "publishers", "unique": False},
    "RECORDING_LOCATION": {"name": "locations_recording", "unique": False},
    "GENRE": {"name": "genres", "unique": False},
    "RATING": {"name": "rating", "unique": True},
    "CONTENT_TYPE": {"name": "content_type", "unique": True},
    "SUBJECT": {"name": "subject", "unique": True},
    "KEYWORDS": {"name": "keywords", "unique": False},
    "MOOD": {"name": "moods", "unique": False},
    "DESCRIPTION": {"name": "description", "unique": False},
    "SYNOPSIS": {"name": "synopsis", "unique": False},
    "SUMMARY": {"name": "summary", "unique": False},
    "COMMENT": {"name": "comment", "unique": False},
    "DATE_WRITTEN": {"name": "date_written", "unique": True},
    "DATE_RELEASED": {"name": "date_released", "unique": True},
}

level_70 = lambda text: {
    "TITLE": {"name": f"{text}", "unique": True},
    "IMDB": {"name": f"{text}_imdb", "unique": True},
    "TMDB": {"name": f"{text}_tmdb", "unique": True},
    "TVDB2": {"name": f"{text}_tvdb", "unique": True},
    "DESCRIPTION": {"name": f"{text}_description", "unique": True},
    "SYNOPSIS": {"name": f"{text}_synopsis", "unique": True},
    "SUMMARY": {"name": f"{text}_summary", "unique": True},
}

level_50 = lambda text: {
    "PART_NUMBER": {"name": f"{text}_number", "unique": True},
    "IMDB": {"name": f"{text}_imdb", "unique": True},
    "TMDB": {"name": f"{text}_tmdb", "unique": True},
    "TVDB2": {"name": f"{text}_tvdb", "unique": True},
    **common_tags_by_target,
}

movie_tags_by_target: dict[int, dict[str | tuple, dict]] = {
    70: {**level_70("collection"), "TOTAL_PARTS": {"name": "movies_number", "unique": True}},
    50: level_50("movie"),
}

series_tags_by_target: dict[int, dict[str | tuple, dict]] = {
    70: {**level_70("series"), "TOTAL_PARTS": {"name": "seasons_number", "unique": True}},
    60: {
        "TITLE": {"name": "season", "unique": True},
        "PART_NUMBER": {"name": "season_number", "unique": True},
        "TOTAL_PARTS": {"name": "episodes_season_number", "unique": True},
    },
    50: level_50("episode"),
}
