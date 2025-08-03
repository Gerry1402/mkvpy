from mkvpy.Tracks.track import Track
from pathlib import Path

def string_to_tuple(resolution: str) -> tuple[int, int]:
    """Convert a resolution string like '1920x1080' to a tuple (1920, 1080)."""
    try:
        width, height = map(lambda x: int(x.strip()), resolution.split('x'))
        return width, height
    except ValueError:
        raise ValueError(f"Invalid resolution format: {resolution}. Expected format is 'widthxheight'.")


class Video(Track):
    def __init__(
        self,
        file_path: str | Path,
        id: int,
        name: str | None = None,
        language: str | None = None,
        default: bool | None = None,
        forced: bool | None = None,
        sync: int = 0,
        dimension_pixel: tuple[int, int] | None = None,
        dimension_display: tuple[int, int] | None = None,
    ):
        super().__init__(file_path, id, name, language, default, forced, sync)
        self.dimension_pixel: tuple[int, int] = dimension_pixel or string_to_tuple(self.info_track.get("properties", {}).get("pixel_dimensions", "0x0"))
        self.dimension_display: tuple[int, int] = dimension_display or string_to_tuple(self.info_track.get("properties", {}).get("display_dimensions", "0x0"))

    def __repr__(self):
        return f"<Video id={self.id} resolution={self.dimension_pixel} codec={self._id}>"
