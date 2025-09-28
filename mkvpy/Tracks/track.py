from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from mkvpy.mkv_tool_nix import MKVToolNix
from mkvpy.utils import check_file_path, default_or_new_path

if TYPE_CHECKING:
    from .audio import Audio
    from .subtitle import Subtitle
    from .video import Video

codecid_to_ext: dict[str, str] = {
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

    def __new__(cls, file_path: str | Path, id_track: int = 0, **kwargs) -> Track | Video | Audio | Subtitle:

        if cls is not Track:
            return super().__new__(cls)

        file_path = check_file_path(file_path)
        try:
            track_info = cls.get_file_info(file_path).get("tracks", [])[id_track]
        except IndexError:
            raise ValueError(f"Track with id {id_track} does not exist in file {file_path}.") from None
        track_type = track_info.get("type", "unknown").lower()

        if track_type == "video":
            from .video import Video

            return Video(file_path, id_track, **kwargs)

        elif track_type == "audio":
            from .audio import Audio

            return Audio(file_path, id_track, **kwargs)

        elif track_type == "subtitles":
            from .subtitle import Subtitle

            return Subtitle(file_path, id_track, **kwargs)

        else:
            raise ValueError(f"Unknown track type: {track_type}")

    def __init__(
        self,
        file_path: str | Path,
        id_track: int = 0,
        name: str = "",
        default: bool  = False,
        forced: bool = False,
        sync: int = 0,
    ) -> None:
        self.file_path: Path = check_file_path(file_path)
        try:
            self.info_track: dict = self.get_file_info(self.file_path).get("tracks", [])[id_track]
        except IndexError:
            raise ValueError(f"Track with id {id_track} does not exist in file {self.file_path}.") from None
        self._id: int = id_track

        self.name: str = name or self.info_track["properties"].get("track_name", f"{self.type} {self.id}")
        self.default: bool = default or self.info_track["properties"].get("default_track", False)
        self.forced: bool = forced or self.info_track["properties"].get("forced_track", False)
        self.enabled: bool = self.info_track["properties"].get("enabled_track", False)
        self.sync: int = sync

    @property
    def id(self) -> int:
        return self._id

    @property
    def type(self) -> str:
        return self.info_track.get("type", "unknown").lower()

    @property
    def codec_id(self) -> str:
        return self.info_track["properties"].get("codec_id", "unknown")

    def extract(self, output_path: str | Path | None = None, overwrite: bool = False) -> None:
        """Extract the track to a file."""
        if self.type not in codecid_to_ext:
            raise TypeError(f"Unsupported track type: {self.type}. Cannot extract.")
        path = default_or_new_path(self.file_path.with_suffix(f".{codecid_to_ext[self.type]}"), output_path, overwrite)
        self.execute_command("extract", "tracks", self.file_path, f"{self.id}:{path}")

    def __repr__(self) -> str:
        info = [
            ("file_path", "source"),
            ("id", "id"),
            ("codec_id", "codec"),
            ("type", "type"),
            ("name", "name"),
            ("language", "lang"),
            ("dimension_pixel", "resolution"),
            ("dimension_display", "display_resolution"),
            ("channels", "channels"),
            ("frequency", "sampling_frequency"),
        ]
        class_name = self.__class__.__name__
        attrs = {name: getattr(self, key, "N/A") for key, name in info if hasattr(self, key)}
        attr_str = " ".join([f"{key}={value}" for key, value in attrs.items()])
        return f"<{class_name} {attr_str}>"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Track):
            return self.id == other.id and self.file_path == other.file_path
        return False

    def __hash__(self) -> int:
        return hash((self.id, self.file_path))


if __name__ == "__main__":
    file = r"C:\Users\gerar\Desktop\The Martian.mkv"
    for i in range(7):
        track = Track(file, i)
        print(track, end="\n\n")
