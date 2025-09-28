from pathlib import Path

from mkvpy.Tracks.track import Track


class Subtitle(Track):
    def __init__(
        self,
        file_path: str | Path,
        id_track: int = 0,
        name: str = "",
        language: str = "und",
        default: bool = False,
        forced: bool = False,
        sync: int = 0,
        # flags
        original: bool = False,
        text_description: bool = False,
        hearing_impaired: bool = False,
        commentary: bool = False,
        # additional properties
        encoder: str = "",
    ):
        super().__init__(file_path, id_track, name, default, forced, sync)
        self.encoder = encoder or self.info_track.get("properties", {}).get("encoding", "").lower()
        self.language: str = language or self.info_track["properties"].get("language", "und")

    @property
    def index_entries(self) -> int:
        """Get the number of index entries in the subtitle track."""
        return self.info_track.get("properties", {}).get("num_index_entries", 0)
