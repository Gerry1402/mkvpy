from __future__ import annotations

import os
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Iterable


def check_executable_path(executable_path: str | Path) -> Path | None:
    executable_path = Path(executable_path)

    return executable_path if executable_path.is_file() and executable_path.exists() else None


def check_file_path(file_path: str | Path) -> Path:
    file_path = Path(file_path)
    if file_path.is_file() and file_path.exists():
        return file_path

    raise FileNotFoundError(f"File '{file_path}' does not exist or is not a file.")


def unique_path(base_path: str | Path) -> Path:
    base = Path(base_path)
    if not base.exists():
        return base

    counter = 1
    while True:
        new_path = base.with_name(f"{base.stem} ({counter}){base.suffix}")
        if not new_path.exists():
            return new_path
        counter += 1


def default_or_new_path(default_path: str | Path, new_path: str | Path | None, overwrite: bool) -> Path:
    final_path = Path(new_path or default_path)

    if not overwrite and final_path.exists():
        final_path = unique_path(final_path)

    return final_path


def human_join(iterable: Iterable[str]) -> str:
    """Join an iterable of strings into a human-readable string."""

    sorted_list = sorted(iterable, key=str)

    add_firsts = ", ".join(str(item) for item in sorted_list[:-1])
    add_and = " and " if len(sorted_list) > 1 else ""
    add_last = str(sorted_list[-1]) if len(sorted_list) > 1 else ""

    return f"{add_firsts}{add_and}{add_last}"


@contextmanager
def temp_file(suffix, content: str = "", encoding="utf-8"):
    fd, path = tempfile.mkstemp(suffix=suffix)
    temp_path = Path(path)
    os.close(fd)
    try:
        if content:
            temp_path.write_text(content, encoding=encoding)
        yield temp_path
    finally:
        temp_path.unlink(missing_ok=True)
