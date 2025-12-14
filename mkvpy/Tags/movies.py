from pathlib import Path

from mkvpy.Tags.base_tags import BaseTags


class MovieTags(BaseTags):
    """Movie-specific tag management class."""

    def __init__(self, file_path: Path | None = None, language_ietf: str = "und") -> None:
        super().__init__(file_path, language_ietf, "movie")

        # Collection level properties
        self.collection: str = ""
        self.movies_number: int = 0

        self.collection_imdb: str = ""
        self.collection_tmdb: str = ""
        self.collection_description: str = ""
        self.collection_synopsis: str = ""
        self.collection_summary: str = ""

        # Movie level properties
        self.title: str = ""
        self.subtitle: str = ""
        self.movie_number: int = 0
        self.movie_imdb: str = ""
        self.movie_tmdb: str = ""
        self.movie_tvdb: str = ""

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
        

        if self._file_path:
            self.load_tags_to_attributes(self.extract_tags_as_dict(self._file_path))

    def _info_targets(self) -> dict[int, str]:
        """Return ordered movie tag information."""
        return {70: "COLLECTION", 50: "MOVIE"}


if __name__ == "__main__":
    path1 = Path(r"C:\Users\gerar\Desktop\The Martian.mkv")
    path2 = Path(r"C:\Users\gerar\Desktop\Harry Potter 3 - The Prisoner of Azkaban.mkv")
    movie_tags = MovieTags()
    print(movie_tags)
    # print(movie_tags.extract_tags_as_dict(path))
    print(movie_tags.actors_characters)
    # movie_tags.extract_tags_file(path.with_suffix(".tags.xml"), True)
    print(movie_tags.execute_command("extract", path1, "chapters", "--simple"))
