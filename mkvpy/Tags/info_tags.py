info_targets: dict[str, int] = {
    "COLLECTION": 70,
    "SEASON": 60,
    "MOVIE": 50,
    "EPISODE": 50,
}

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
    "actor": {"name": ("ACTOR", "CHARACTER"), "unique": False, "target": 50},
    # Key Creative Roles
    "director": {"name": "DIRECTOR", "unique": False, "target": 50},
    "writer": {"name": "WRITTEN_BY", "unique": False, "target": 50},
    "screenplayer": {"name": "SCREENPLAY_BY", "unique": False, "target": 50},
    # Production Crew (in typical hierarchy)
    "producer": {"name": "PRODUCER", "unique": False, "target": 50},
    "producer_executive": {"name": "EXECUTIVE_PRODUCER", "unique": False, "target": 50},
    "coproducer": {"name": "COPRODUCER", "unique": False, "target": 50},
    # Department Heads
    "director_photography": {
        "name": "DIRECTOR_OF_PHOTOGRAPHY",
        "unique": False,
        "target": 50,
    },
    "editor": {"name": "EDITOR", "unique": False, "target": 50},
    "designer_production": {
        "name": "PRODUCTION_DESIGNER",
        "unique": False,
        "target": 50,
    },
    "designer_costume": {"name": "COSTUME_DESIGNER", "unique": False, "target": 50},
    # Additional Crew
    "director_assistant": {"name": "ASSISTANT_DIRECTOR", "unique": False, "target": 50},
    "mastering_engineer": {"name": "MASTERED_BY", "unique": False, "target": 50},
    # Production & Distribution
    "production_studio": {"name": "PRODUCTION_STUDIO", "unique": False, "target": 50},
    "distributor": {"name": "DISTRIBUTED_BY", "unique": False, "target": 50},
    "publisher": {"name": "PUBLISHER", "unique": False, "target": 50},
    "location_recording": {"name": "RECORDING_LOCATION", "unique": False, "target": 50},
    # Content Classification & Metadata
    "genre": {"name": "GENRE", "unique": False, "target": 50},
    "rating": {"name": "RATING", "unique": True, "target": 50},
    "content_type": {"name": "CONTENT_TYPE", "unique": True, "target": 50},
    "subject": {"name": "SUBJECT", "unique": True, "target": 50},
    "keyword": {"name": "KEYWORDS", "unique": False, "target": 50},
    "mood": {"name": "MOOD", "unique": False, "target": 50},
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
    "actor",
    "director",
    "writer",
    "screenplayer",
    "producer",
    "producer_executive",
    "coproducer",
    "director_photography",
    "editor",
    "designer_production",
    "designer_costume",
    "director_assistant",
    "mastering_engineer",
    "production_studio",
    "distributor",
    "publisher",
    "location_recording",
    "genre",
    "rating",
    "content_type",
    "subject",
    "keyword",
    "mood",
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
tags_by_target: dict[int, dict[str | tuple, str]] = {}

for key, info_tag in info_tags.items():

    if not isinstance(info_tag["target"], int):
        continue

    if not isinstance(info_tag["name"], (str, tuple)):
        continue

    tags_by_target.setdefault(info_tag["target"], {})[info_tag["name"]] = key
