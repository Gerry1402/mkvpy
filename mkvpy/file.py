from __future__ import annotations

from pathlib import Path
from typing import Any, Literal, Iterable

from mkvpy import MKVToolNix
from mkvpy.chapters import Chapters
from mkvpy.Tags.movies import MovieTags
from mkvpy.Tags.series import SeriesTags
from mkvpy.Tracks.track import Track

from .utils import check_file_path

tags = {"movie": MovieTags, "series": SeriesTags}

class MKVFile(MKVToolNix):

    def __init__(self, file_path: str | Path | None = None, style_tags: Literal["movie", "series"] | None = None):

        if file_path:
            self.file_path: Path | None = check_file_path(file_path)
            self.info_file: dict[str, Any] = self.get_file_info(self.file_path)
            self.tracks: list[Track] = [Track(self.file_path, i) for i in range(len(self.info_file.get("tracks", [])))]
            self.tags: SeriesTags | MovieTags | None = tags[style_tags](self.file_path) if style_tags else None
            self.chapters: Chapters | None = Chapters(self.file_path)
        else:
            self.file_path = None
            self.tracks = []
            self.tags = None
            self.chapters = None

        def _aux_tracks(self, file_path: str | Path, ids: Iterable[int] | None = None) -> list[Track]:
            file_path = check_file_path(file_path)
            info_file = self.get_file_info(file_path)
            num_tracks = len(info_file.get("tracks", []))
            ids = ids or range(num_tracks)
            if min(ids) < 0 or max(ids) >= num_tracks:
                raise ValueError(f"Track ids must be between 0 and {num_tracks - 1}.")
            return [Track(file_path, i) for i in range(num_tracks) if i in ids]

        def add_tracks(self, file_path: str | Path, ids: Iterable[int] | None = None) -> None:
            self.tracks += self._aux_tracks(file_path, ids)

        def set_tracks(self, file_path: str | Path, ids: Iterable[int] | None = None) -> None:
            self.tracks = self._aux_tracks(file_path, ids)

        def set_tags(self, file_path: str | Path, style_tags: Literal["movie", "series"] = "movie") -> None:
            file_path = check_file_path(file_path)
            self.tags = tags[style_tags](file_path)
        
        def set_chapters(self, file_path: str | Path) -> None:
            file_path = check_file_path(file_path)
            self.chapters = Chapters(file_path)
        
        def set_file(self, file_path: str | Path, style_tags: Literal["movie", "series"] | None = None) -> None:
            file_path = check_file_path(file_path)
            self.set_tracks(file_path)
            self.set_tags(file_path, style_tags) if style_tags else None
            self.set_chapters(file_path)


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