from pathlib import Path

from mkvpy import MKVToolNix
from mkvpy.utils import check_file_path


class Chapters(MKVToolNix):
    """
    Class to handle chapters in MKV files.
    """

    def __init__(self, file_path: Path | str | None = None):
        self.timestamps = []
        self.names = []

        if file_path:
            self._file_path = check_file_path(file_path)
            self._get_chapters_info()
        else:
            self._file_path = None

    def _get_chapters_info(self) -> None:
        """Extract chapter information as a list of tuples."""

        string_chapters: str = self.execute_command("extract", str(self._file_path), "chapters", "--simple")
        lines: list[str] = string_chapters.splitlines()
        num_decimals: int = len(str(len(lines)//2))

        for i, (timestamp_line, name_line) in enumerate(zip(lines[::2], lines[1::2]), start=1):

            chapter_name: str = name_line.split("=", 1)[1] if "=" in name_line else f"Chapter {str(i).zfill(num_decimals)}"
            self.names.append(chapter_name)

            time_str: str = timestamp_line.split("=", 1)[1]
            parts: list[str] = time_str.split(":")
            seconds: float = sum(float(part) * (60**i) for i, part in enumerate(reversed(parts)))
            self.timestamps.append(seconds)
    
    def build_str_content(self):
        """Build a string representation of the chapter information."""
        if len(self.names) != len(self.timestamps):
            raise ValueError("Chapter names and timestamps lists have different lengths.")
        
        lines = []
        num_decimals: int = len(str(len(self.names)))

        for i, (name, timestamp) in enumerate(zip(self.names, self.timestamps), start=1):
            minutes, seconds = divmod(timestamp, 60)
            hours, minutes = divmod(minutes, 60)
            lines.append(
                f"CHAPTER{str(i).zfill(num_decimals)}={hours:02.0f}:{minutes:02.0f}:{(seconds):06.3f}\n"
                f"CHAPTER{str(i).zfill(num_decimals)}NAME={name}"
            )
        return "\n".join(lines)
