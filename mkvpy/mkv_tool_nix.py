from __future__ import annotations

import json
import subprocess as sp
import warnings
from pathlib import Path
from typing import Literal

from mkvpy.utils import check_executable_path, check_file_path


class MKVToolNix:
    _paths: dict[str, Path | None] = {"merge": None, "extract": None, "info": None, "propedit": None}

    _defaults: dict[str, str] = {"merge": "mkvmerge", "extract": "mkvextract", "info": "mkvinfo", "propedit": "mkvpropedit"}
    _links: dict[str, str] = {
        "merge": "https://www.bunkus.org/videotools/mkvtoolnix/doc/mkvmerge.html",
        "extract": "https://www.bunkus.org/videotools/mkvtoolnix/doc/mkvextract.html",
        "info": "https://www.bunkus.org/videotools/mkvtoolnix/doc/mkvinfo.html",
        "propedit": "https://www.bunkus.org/videotools/mkvtoolnix/doc/mkvpropedit.html",
    }

    @classmethod
    def get_path(cls, tool: Literal["merge", "extract", "info", "propedit"]) -> Path | str:
        return cls._paths[tool] or cls._defaults[tool]

    @classmethod
    def set_path(cls, tool: Literal["merge", "extract", "info", "propedit"], path: Path | str | None) -> None:
        cls._paths[tool] = check_executable_path(path) if path else None

    @classmethod
    def reset_paths(cls) -> None:
        for tool in cls._paths:
            cls._paths[tool] = None

    @classmethod
    def execute_command(cls, tool: Literal["merge", "extract", "info", "propedit"], *args: str | Path) -> str:
        cmds = [cls.get_path(tool)] + [str(arg) for arg in args]
        result = sp.run(cmds, capture_output=True, text=True, encoding="utf-8")

        if result.returncode == 1:
            warnings.warn(
                f"{cls._defaults[tool]} It is strongly advisable to check the waning and the final file. stderr: '{result.stderr}', stdout: '{result.stdout}'"
            )
        elif result.returncode == 2:
            raise RuntimeError(
                f"{cls._defaults[tool]} failed. stderr: '{result.stderr}', stdout: '{result.stdout}'"
            )
        return result.stdout.strip()

    @classmethod
    def get_file_info(cls, file_path: str | Path) -> dict:
        path = check_file_path(file_path)
        return json.loads(cls.execute_command("merge", "-J", path))
