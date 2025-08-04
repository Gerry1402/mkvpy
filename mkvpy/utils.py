import os
import tempfile
from collections.abc import KeysView
from contextlib import contextmanager
from pathlib import Path
from typing import Any


def check_executable_path(executable_path: str | Path) -> Path | None:

    executable_path = (
        Path(executable_path)
        if not isinstance(executable_path, Path)
        else executable_path
    )

    if executable_path.exists() and executable_path.is_file():
        return Path(executable_path)

    return None


def check_file_path(file_path: str | Path) -> Path:
    file_path = Path(file_path) if not isinstance(file_path, Path) else file_path

    if file_path.exists() and file_path.is_file():
        return Path(file_path)

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


def human_join(iterable: KeysView[Any] | list[Any] | tuple[Any] | set[Any]) -> str:
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


def string_to_number(s: str):
    for action in [int, float, str]:
        try:
            action(s.strip())
        except ValueError:
            continue
        else:
            return action(s.strip())


def number_to_string(number: int | float | str | None) -> str | None:
    """Convert a number to a string, preserving its type."""
    return str(number) if isinstance(number, (int, float)) else number
