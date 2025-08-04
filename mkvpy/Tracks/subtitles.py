from pathlib import Path

from mkvpy.Tracks.track import Track


class Subtitle(Track):
    def __init__(
        self,
        file_path: str | Path,
        id: int,
        name: str = "",
        language: str = "",
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
        super().__init__(file_path, id, name, language, default, forced, sync)
        self.encoder = (
            encoder or self.info_track.get("properties", {}).get("encoding", "").lower()
        )

    def __repr__(self):
        return (
            f"<Subtitle id={self.id} language={self.language} encoder={self.encoder}>"
        )
