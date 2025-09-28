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

if set(info_tags.keys()) != set(order_tags):
    raise ValueError("name_tags keys and ordered_tag_keys do not match")

# Reverse lookup dictionary: target_int -> {TAG_NAME -> original_key}
# Movie-specific tags_by_target: Collection (70) + Movie (50)
movie_tags_by_target: dict[int, dict[str | tuple, dict]] = {
    70: {
        # Collection level tags
        "TITLE": {"name": "collection", "unique": True, "target": 70},
        "TOTAL_PARTS": {"name": "movies_number", "unique": True, "target": 70},
        "IMDB": {"name": "collection_imdb", "unique": True, "target": 70},
        "TMDB": {"name": "collection_tmdb", "unique": True, "target": 70},
        "DESCRIPTION": {"name": "collection_description", "unique": True, "target": 70},
        "SYNOPSIS": {"name": "collection_synopsis", "unique": True, "target": 70},
        "SUMMARY": {"name": "collection_summary", "unique": True, "target": 70},
    },
    50: {
        # Movie level tags
        "PART_NUMBER": {"name": "movie_number", "unique": True, "target": 50},
        "IMDB": {"name": "movie_imdb", "unique": True, "target": 50},
        "TMDB": {"name": "movie_tmdb", "unique": True, "target": 50},
        "TVDB2": {"name": "movie_tvdb", "unique": True, "target": 50},
        # Common tags
        "TITLE": {"name": "title", "unique": True, "target": 50},
        "SUBTITLE": {"name": "subtitle", "unique": True, "target": 50},
        ("ACTOR", "CHARACTER"): {"name": "actors_characters", "unique": False, "target": 50},
        "DIRECTOR": {"name": "directors", "unique": False, "target": 50},
        "WRITTEN_BY": {"name": "writers", "unique": False, "target": 50},
        "SCREENPLAY_BY": {"name": "screenplayers", "unique": False, "target": 50},
        "PRODUCER": {"name": "producers", "unique": False, "target": 50},
        "EXECUTIVE_PRODUCER": {"name": "producers_executives", "unique": False, "target": 50},
        "COPRODUCER": {"name": "coproducers", "unique": False, "target": 50},
        "DIRECTOR_OF_PHOTOGRAPHY": {"name": "directors_photography", "unique": False, "target": 50},
        "EDITOR": {"name": "editors", "unique": False, "target": 50},
        "PRODUCTION_DESIGNER": {"name": "designers_production", "unique": False, "target": 50},
        "COSTUME_DESIGNER": {"name": "designers_costume", "unique": False, "target": 50},
        "ASSISTANT_DIRECTOR": {"name": "directors_assistant", "unique": False, "target": 50},
        "MASTERED_BY": {"name": "mastering_engineers", "unique": False, "target": 50},
        "PRODUCTION_STUDIO": {"name": "productions_studio", "unique": False, "target": 50},
        "DISTRIBUTED_BY": {"name": "distributors", "unique": False, "target": 50},
        "PUBLISHER": {"name": "publishers", "unique": False, "target": 50},
        "RECORDING_LOCATION": {"name": "locations_recording", "unique": False, "target": 50},
        "GENRE": {"name": "genres", "unique": False, "target": 50},
        "RATING": {"name": "rating", "unique": True, "target": 50},
        "CONTENT_TYPE": {"name": "content_type", "unique": True, "target": 50},
        "SUBJECT": {"name": "subject", "unique": True, "target": 50},
        "KEYWORDS": {"name": "keywords", "unique": False, "target": 50},
        "MOOD": {"name": "moods", "unique": False, "target": 50},
        "DESCRIPTION": {"name": "description", "unique": False, "target": 50},
        "SYNOPSIS": {"name": "synopsis", "unique": False, "target": 50},
        "SUMMARY": {"name": "summary", "unique": False, "target": 50},
        "COMMENT": {"name": "comment", "unique": False, "target": 50},
        "DATE_WRITTEN": {"name": "date_written", "unique": True, "target": 50},
        "DATE_RELEASED": {"name": "date_released", "unique": True, "target": 50},
    }
}

# Series-specific tags_by_target: Series (70) + Season (60) + Episode (50)
series_tags_by_target: dict[int, dict[str | tuple, dict]] = {
    70: {
        # Series level tags
        "TITLE": {"name": "series", "unique": True, "target": 70},
        "TOTAL_PARTS": {"name": "seasons_number", "unique": True, "target": 70},
        "IMDB": {"name": "series_imdb", "unique": True, "target": 70},
        "TMDB": {"name": "series_tmdb", "unique": True, "target": 70},
        "TVDB2": {"name": "series_tvdb", "unique": True, "target": 70},
        "DESCRIPTION": {"name": "series_description", "unique": True, "target": 70},
        "SYNOPSIS": {"name": "series_synopsis", "unique": True, "target": 70},
        "SUMMARY": {"name": "series_summary", "unique": True, "target": 70},
    },
    60: {
        # Season level tags
        "TITLE": {"name": "season", "unique": True, "target": 60},
        "PART_NUMBER": {"name": "season_number", "unique": True, "target": 60},
        "TOTAL_PARTS": {"name": "episodes_season_number", "unique": True, "target": 60},
    },
    50: {
        # Episode level tags
        "PART_NUMBER": {"name": "episode_number", "unique": True, "target": 50},
        "IMDB": {"name": "episode_imdb", "unique": True, "target": 50},
        "TMDB": {"name": "episode_tmdb", "unique": True, "target": 50},
        "TVDB2": {"name": "episode_tvdb", "unique": True, "target": 50},
        # Common tags (same as movie level 50)
        "TITLE": {"name": "title", "unique": True, "target": 50},
        "SUBTITLE": {"name": "subtitle", "unique": True, "target": 50},
        ("ACTOR", "CHARACTER"): {"name": "actors_characters", "unique": False, "target": 50},
        "DIRECTOR": {"name": "directors", "unique": False, "target": 50},
        "WRITTEN_BY": {"name": "writers", "unique": False, "target": 50},
        "SCREENPLAY_BY": {"name": "screenplayers", "unique": False, "target": 50},
        "PRODUCER": {"name": "producers", "unique": False, "target": 50},
        "EXECUTIVE_PRODUCER": {"name": "producers_executives", "unique": False, "target": 50},
        "COPRODUCER": {"name": "coproducers", "unique": False, "target": 50},
        "DIRECTOR_OF_PHOTOGRAPHY": {"name": "directors_photography", "unique": False, "target": 50},
        "EDITOR": {"name": "editors", "unique": False, "target": 50},
        "PRODUCTION_DESIGNER": {"name": "designers_production", "unique": False, "target": 50},
        "COSTUME_DESIGNER": {"name": "designers_costume", "unique": False, "target": 50},
        "ASSISTANT_DIRECTOR": {"name": "directors_assistant", "unique": False, "target": 50},
        "MASTERED_BY": {"name": "mastering_engineers", "unique": False, "target": 50},
        "PRODUCTION_STUDIO": {"name": "productions_studio", "unique": False, "target": 50},
        "DISTRIBUTED_BY": {"name": "distributors", "unique": False, "target": 50},
        "PUBLISHER": {"name": "publishers", "unique": False, "target": 50},
        "RECORDING_LOCATION": {"name": "locations_recording", "unique": False, "target": 50},
        "GENRE": {"name": "genres", "unique": False, "target": 50},
        "RATING": {"name": "rating", "unique": True, "target": 50},
        "CONTENT_TYPE": {"name": "content_type", "unique": True, "target": 50},
        "SUBJECT": {"name": "subject", "unique": True, "target": 50},
        "KEYWORDS": {"name": "keywords", "unique": False, "target": 50},
        "MOOD": {"name": "moods", "unique": False, "target": 50},
        "DESCRIPTION": {"name": "description", "unique": False, "target": 50},
        "SYNOPSIS": {"name": "synopsis", "unique": False, "target": 50},
        "SUMMARY": {"name": "summary", "unique": False, "target": 50},
        "COMMENT": {"name": "comment", "unique": False, "target": 50},
        "DATE_WRITTEN": {"name": "date_written", "unique": True, "target": 50},
        "DATE_RELEASED": {"name": "date_released", "unique": True, "target": 50},
    }
}