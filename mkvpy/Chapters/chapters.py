from mkvpy import MKVToolNix
from mkvpy.utils import check_file_path


class Chapters(MKVToolNix):
    """
    Class to handle chapters in MKV files.
    """

    def __init__(self, file_path: str):
        self._file_path = check_file_path(file_path)
        self._default_chapters = self._get_chapters_info()
        self.chapters = self._default_chapters.copy()  # Copy default chapters to allow modifications

    def _get_chapters_info(self) -> list[tuple[str, float]]:
        """Extract chapter information as a list of tuples."""

        string_chapters: str = self.execute_command("extract", str(self._file_path), "chapters", "--simple")
        chapters_info: list[tuple[str, float]] = []
        lines: list[str] = string_chapters.splitlines()

        # Group lines in pairs using zip and slicing
        timestamp_lines: list[str] = lines[::2]  # Every even line (0, 2, 4, ...)
        name_lines: list[str] = lines[1::2]  # Every odd line (1, 3, 5, ...)

        num_decimals: int = len(str(len(timestamp_lines)))

        for i, (timestamp_line, name_line) in enumerate(zip(timestamp_lines, name_lines), start=1):

            chapter_name: str = name_line.split("=", 1)[1] if "=" in name_line else f"Chapter {str(i).zfill(num_decimals)}"

            time_str: str = timestamp_line.split("=", 1)[1]
            parts: list[str] = time_str.split(":")
            seconds: float = sum(float(part) * (60**i) for i, part in enumerate(reversed(parts)))

            chapters_info.append((chapter_name, seconds))

        return chapters_info
