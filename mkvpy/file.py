from __future__ import annotations

from pathlib import Path
from typing import Any

from mkvpy import MKVToolNix
from mkvpy.Tags.movies import MovieTags
from mkvpy.Tags.series import SeriesTags
from mkvpy.Tracks.track import Track
from mkvpy.chapters import Chapters
from .utils import check_file_path
from typing import Literal


class MKVFile(MKVToolNix):

    def __init__(self, file_path: str | Path, style_tags: Literal["movie", "series"] | None = None):

        self.file_path: Path = check_file_path(file_path)
        self.info_file: dict[str, Any] = self.get_file_info(self.file_path)
        self.tracks: list[Track] = [Track(self.file_path, i) for i in range(len(self.info_file.get("tracks", [])))]
        tags = {"movie": MovieTags, "series": SeriesTags}
        self.tags: SeriesTags | MovieTags | None = tags[style_tags](self.file_path) if style_tags else None
        self.chapters: Chapters = Chapters(self.file_path)


if __name__ == "__main__":
    file = r"C:\Users\gerar\Desktop\The Martian.mkv"
    mkv_file = MKVFile(file, "movie")
    print(f"Number of tracks: {len(mkv_file.tracks)}")
    for track in mkv_file.tracks:
        print(track)
    print(f"Number of chapters: {mkv_file.chapters.timestamps}")
    print(mkv_file.chapters.names)
    # for track in mkv_file.tracks:
    #     print(track)
    if mkv_file.tags:
        print(mkv_file.tags)
        for target, tag, value in mkv_file.tags:
            print(f"{target}: {tag} = {value}")