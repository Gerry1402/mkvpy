from pathlib import Path

from mkvpy.Tracks.track import Track


class Video(Track):
    def __init__(
        self,
        file_path: str | Path,
        id_track: int = 0,
        name: str = "",
        default: bool = False,
        forced: bool = False,
        sync: int = 0,
        dimension_pixel: str = "0x0",
        dimension_display: str = "0x0",
    ):
        super().__init__(file_path, id_track, name, default, forced, sync)
        self.dimension_pixel: str = self.info_track.get("properties", {}).get("pixel_dimensions", "1920x1080")
        self.dimension_display: str = self.info_track.get("properties", {}).get("display_dimensions", "1920x1080")
