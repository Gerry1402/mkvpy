from pathlib import Path

from mkvpy import MKVToolNix
from mkvpy.utils import check_file_path


class Chapters(MKVToolNix):
    """
    Class to handle chapters in MKV files.
    """

    def __init__(self, file_path: Path | str):
        self._file_path = check_file_path(file_path)
        self._default_chapters = self._get_chapters_info()
        self.timestamps = [chapter[1] for chapter in self._default_chapters]
        self.names = [chapter[0] for chapter in self._default_chapters]

    def _get_chapters_info(self) -> list[tuple[str, float]]:
        """Extract chapter information as a list of tuples."""

        string_chapters: str = self.execute_command("extract", str(self._file_path), "chapters", "--simple")
        chapters_info: list[tuple[str, float]] = []
        lines: list[str] = string_chapters.splitlines()
        timestamp_lines: list[str] = lines[::2]
        name_lines: list[str] = lines[1::2]

        num_decimals: int = len(str(len(timestamp_lines)))

        for i, (timestamp_line, name_line) in enumerate(zip(timestamp_lines, name_lines), start=1):

            chapter_name: str = name_line.split("=", 1)[1] if "=" in name_line else f"Chapter {str(i).zfill(num_decimals)}"

            time_str: str = timestamp_line.split("=", 1)[1]
            parts: list[str] = time_str.split(":")
            seconds: float = sum(float(part) * (60**i) for i, part in enumerate(reversed(parts)))

            chapters_info.append((chapter_name, seconds))

        return chapters_info
