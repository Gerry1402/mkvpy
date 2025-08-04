from pathlib import Path
from typing import Any

from mkvpy import MKVToolNix

from .utils import check_file_path


class File(MKVToolNix):

    def __init__(self, file_path: str | Path):

        self.file_path: Path = check_file_path(file_path)

        self.info_file: dict[str, Any] = self.get_file_info(self.file_path)
        self.title: str | None = self._container().get("title", None)
        self._duration: float = (
            self._container().get("duration", 0.0)
            / self._container().get("timestamp_scale", 1.0)
            / 1000
        )

    def _container(self) -> dict[str, Any]:
        return self.info_file.get("container", {}).get("properties", {})

    @property
    def duration(self) -> float:
        """Get the duration of the file in seconds."""
        return self._duration


if __name__ == "__main__":
    mkv = File(r"C:\Users\gerar\Desktop\The Martian.mkv")

    print("=== FILE INFO ===")
    # print(mkv.info_file)
    # with open(mkv.file_path.stem + ".json", "w", encoding="utf-8") as f:
    #     json.dump(mkv.info_file, f, ensure_ascii=False, indent=4)
    print(f"Title: {mkv.title}")
    print(f"Duration: {mkv.duration:.2f} seconds")

    print("\n=== TAG INFORMATION ===")
