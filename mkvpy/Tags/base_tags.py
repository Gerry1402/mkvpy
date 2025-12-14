from __future__ import annotations

from abc import abstractmethod
from pathlib import Path
from typing import Any, Generator, Literal
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from defusedxml import ElementTree as DefusedET

from mkvpy import MKVToolNix
from mkvpy.Tags.info_tags import info_tags, info_targets, movie_tags_by_target, order_tags, series_tags_by_target
from mkvpy.Tags.xml_utils import complex_tag, get_or_create_target, parse_single_tag, simple_tag
from mkvpy.utils import check_file_path, temp_file, unique_path


class BaseTags(MKVToolNix):

    def __init__(
        self, file_path: Path | str | None = None, language: str | None = None, style_tags: Literal["movie", "series"] = "movie"
    ) -> None:

        self.style_tags: Literal["movie", "series"] = style_tags
        self._file_path: Path | None = check_file_path(file_path) if file_path else None
        self._info_file = self.extract_tags_as_dict(self._file_path) if self._file_path else {}
        self.language: str = language or "und"

    def load_tags_to_attributes(self, values: dict[str, Any]) -> None:
        """Load extracted tags into instance attributes."""
        if not values:
            return
        [setattr(self, attr_name, tag_value) for attr_name, tag_value in values.items() if hasattr(self, attr_name)]

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}{f' source=\"{self._file_path.name}\"' if self._file_path else ''} lang=\"{self.language}\" tags={len(self)}>"

    def __iter__(self) -> Generator[tuple[str, Any]]:
        for tag in order_tags:
            if hasattr(self, tag):
                yield tag, getattr(self, tag)

    def __len__(self) -> int:
        return sum(bool(value) for tag, value in self)

    def __bool__(self) -> bool:
        return bool(len(self))

    def __contains__(self, item: str) -> bool:
        return item in self.__dict__ and bool(self.__dict__[item]) if item not in ["style_tags", "_file_path", "_info_file", "language"] else False

    def __add__(self, other) -> None:
        if not isinstance(other, BaseTags):
            raise TypeError("Can only add BaseTags instances.")

        if type(self) != type(other) or type(self) is BaseTags:
            raise TypeError("Can only add instances of the same subclass of BaseTags.")

        combined_info = self.__dict__.copy()
        for tag_name, tag_value in other.__dict__.items():
            combined_info[tag_name].setdefault(tag_name, tag_value)

        self.load_tags_to_attributes(combined_info)

    @abstractmethod
    def _info_targets(self) -> dict[int, str]:
        pass

    def extract_tags_file(self, output_path: str | Path | None = None, overwrite: bool = False) -> None:
        # sourcery skip: class-extract-method
        if not self._file_path:
            raise ValueError("File path is not set. Cannot extract tags.")
        output_file = output_path or self._file_path.with_name(f"{self._file_path.stem}_tags.xml")
        output_file = unique_path(output_file) if overwrite else output_file
        self.execute_command("extract", self._file_path, "tags", output_file)

    def extract_tags_as_string(self, file_path: str | Path) -> str:
        return self.execute_command("extract", file_path, "tags", "-")

    def extract_tags_as_dict(self, file_path: str | Path) -> dict[str, Any]:
        xml_content = self.extract_tags_as_string(file_path)
        root = DefusedET.fromstring(xml_content)
        parsed_tags: dict[str, Any] = {}
        tags_by_target = series_tags_by_target if self.style_tags == "series" else movie_tags_by_target

        for tag_element in root.findall("Tag"):
            target_value = 50
            if v := tag_element.findtext("./Targets/TargetTypeValue"):
                if v.isdigit():
                    target_value = int(v) if int(v) in info_targets.values() else 50
            elif t := tag_element.findtext("./Targets/TargetType"):
                target_value = info_targets.get(t, 50)

            for simple in tag_element.findall("Simple"):
                key, tag = parse_single_tag(simple)
                if key is None or tag is None:
                    continue
                name = tags_by_target.get(target_value, {}).get(key, {}).get("name", "")
                class_tag = type(getattr(self, name)) if hasattr(self, name) else None
                if tags_by_target.get(target_value, {}).get(key, {}).get("unique", False):
                    tag = class_tag(tag) if class_tag else tag
                    parsed_tags[name] = tag
                else:
                    parsed_tags.setdefault(name, []).append(tag)

        if not parsed_tags:
            print("No tags found in the MKV file. Make sure to follow the official MKV tagging guidelines.")
        return parsed_tags

    def _mount_xml(self) -> Element:
        root = Element("Tags")
        for tag_name, tag_value in self:
            info_tag = info_tags[tag_name]
            target_int = info_tag.get("target", 50)
            if not isinstance(target_int, int):
                target_int = 50
            info_target = self._info_targets().get(target_int, "MOVIE")
            target = get_or_create_target(root, target_int, info_target)
            if not isinstance(tag_value, list):
                tag_value = [tag_value]
            for value in tag_value:
                if isinstance(tag_name, tuple):
                    target.append(complex_tag(tag_name, value))
                elif isinstance(tag_name, str):
                    target.append(simple_tag(tag_name, value))
        return root

    def create_tags_as_string(self) -> str:
        return ElementTree.tostring(self._mount_xml(), encoding="utf-8").decode("utf-8")

    def create_file_tags(self, output_path: str | Path | None = None, overwrite: bool = False) -> None:
        if not self._file_path:
            raise ValueError("File path is not set. Cannot create tags file.")
        output_file = output_path or self._file_path.with_name(f"{self._file_path.stem}_tags.xml")
        output_file = unique_path(output_file) if overwrite else output_file
        ElementTree.ElementTree(self._mount_xml()).write(str(output_file), encoding="utf-8", xml_declaration=True)

    def delete_tags(self) -> None:
        if not self._file_path:
            raise ValueError("File path is not set. Cannot delete tags.")
        self.execute_command("propedit", self._file_path, "--tags", "all:")

    def add_tags(self) -> None:
        if not self._file_path:
            raise ValueError("File path is not set. Cannot add tags.")
        with temp_file(".xml", self.create_tags_as_string()) as temp_path:
            self.execute_command("propedit", self._file_path, "--tags", f"global:{temp_path}")

    def apply_tags(self) -> None:
        self.delete_tags()
        self.add_tags()
