from pathlib import Path

from mkvpy.mkv_tool_nix import MKVToolNix
from mkvpy.utils import check_file_path, unique_path

CODECID_EXT_TO_EXT: dict[str, str] = {

    # Vídeo
    "V_MPEG4/ISO/AVC": "h264",
    "V_MS/VFW/FOURCC": "avi",
    "V_REAL/": "rm",
    "V_THEORA": "ogv",
    "V_VP8": "ivf",
    "V_VP9": "ivf",

    # Audio
    "A_MPEG/L2": "mp2",
    "A_MPEG/L3": "mp3",
    "A_AC3": "ac3",
    "A_EAC3": "eac3",
    "A_PCM/INT/LIT": "wav",
    "A_AAC": "aac",
    "A_AAC/": "aac",
    "A_VORBIS": "ogg",
    "A_FLAC": "flac",
    "A_ALAC": "caf",
    "A_OPUS": "opus",
    "A_TTA1": "tta",
    "A_WAVPACK4": "wv",

    # Subtítulos
    "S_TEXT/UTF8": "srt",
    "S_TEXT/SSA": "ssa",
    "S_TEXT/ASS": "ass",
}


class Track(MKVToolNix):
    def __new__(
        cls,
        file_path: str | Path,
        id: int,
        name: str | None = None,
        language: str | None = None,
        default: bool | None = None,
        forced: bool | None = None,
        sync: int = 0,
    ):
        """Factory method that returns the appropriate track subclass."""

        if cls != Track:
            return super().__new__(cls)

        temp_instance = object.__new__(Track)
        temp_instance.__init__(file_path, id, name, language, default, forced, sync)

        track_type = temp_instance.type

        from .audio import Audio
        from .subtitles import Subtitle
        from .video import Video

        track_classes: dict[str, type] = {
            "video": Video,
            "audio": Audio,
            "subtitles": Subtitle,
        }

        track_class = track_classes.get(track_type, Track)

        if track_class != Track:
            new_instance = object.__new__(track_class)
            new_instance.__init__(file_path, id, name, language, default, forced, sync)
            return new_instance

        return temp_instance

    def __init__(
        self,
        file_path: str | Path,
        id: int,
        name: str | None = None,
        language: str | None = None,
        default: bool | None = None,
        forced: bool | None = None,
        sync: int = 0,
    ):
        self.file_path: Path = check_file_path(file_path)
        try:
            self.info_track = self.get_file_info(self.file_path).get("tracks", [])[id]
        except IndexError:
            raise ValueError(f"Track with id {id} does not exist in file {self.file_path}.") from None
        self._id: int = id

        self.name: str = name or self.info_track["properties"].get("name", f"{self.type} {self.id}")
        self.language: str = language or self.info_track["properties"].get("language", "und")
        self.default: bool = default or self.info_track["properties"].get("default", None)
        self.forced: bool = forced or self.info_track["properties"].get("forced", None)
        self.enabled: bool = self.info_track["properties"].get("enabled", None)
        self.sync: int = sync

    @property
    def id(self) -> int:
        return self._id

    @property
    def type(self) -> str:
        return self.info_track.get("type", "unknown")

    @property
    def codec_id(self) -> str:
        return self.info_track["properties"].get("codec_id", "unknown")

    def extract(self, output_path: str | Path | None = None, overwrite: bool = False) -> None:
        """Extract the track to a file."""
        if self.type not in CODECID_EXT_TO_EXT:
            raise ValueError(f"Unsupported track type: {self.type}. Cannot extract.")
        path = output_path or self.file_path.with_suffix(f".{CODECID_EXT_TO_EXT[self.type]}")
        if overwrite:
            path = unique_path(path)
        self.execute_command("extract", "tracks", self.file_path, f"{self.id}:{path}")

    def __repr__(self):
        return f"<Track id={self.id} type={self.type} codec_id={self.codec_id}>"
