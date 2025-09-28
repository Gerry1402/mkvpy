from __future__ import annotations

from abc import abstractmethod
from pathlib import Path
from typing import Any, Generator
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from defusedxml import ElementTree as DefusedET

from mkvpy import MKVToolNix
from mkvpy.Tags.info_tags import info_tags, info_targets, order_tags, movie_tags_by_target, series_tags_by_target
from mkvpy.Tags.xml_utils import complex_tag, get_or_create_target, parse_single_tag, simple_tag
from mkvpy.utils import check_file_path, temp_file, unique_path
from typing import Literal


class BaseTags(MKVToolNix):

    def __init__(
        self, file_path: Path | str, language: str | None = None, style_tags: Literal["movie", "series"] = "movie"
    ) -> None:
        self.file_path: Path = check_file_path(file_path)
        self.language: str = language or "und"
        self.style_tags: Literal["movie", "series"] = style_tags
        self._info_file = self.extract_tags_as_dict(self.file_path)

    def load_tags_to_attributes(self) -> None:
        """Load extracted tags into instance attributes."""
        if not self._info_file:
            return

        for tags_dict in self._info_file.values():
            for attr_name, tag_value in tags_dict.items():
                if hasattr(self, attr_name):
                    setattr(self, attr_name, tag_value)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} file={self.file_path.name} lang={self.language} num_tags={len(self)}>"

    def __iter__(self) -> Generator[tuple[bool | int, str, Any], Any, None]:
        for tag in order_tags:
            if hasattr(self, tag) and (tag_value := getattr(self, tag)):
                info_tag = info_tags[tag]
                target_int = info_tag.get("target", 50)
                if not isinstance(target_int, int):
                    target_int = 50
                yield target_int, tag, tag_value

    def __len__(self) -> int:
        return sum(bool(value) for value in self.__dict__.values())

    def __bool__(self) -> bool:
        return bool(len(self))

    def __contains__(self, item: str | int) -> bool:
        return item in self.__dict__ and bool(self.__dict__[item])

    @abstractmethod
    def _info_targets(self) -> dict[int, str]:
        pass

    def extract_tags_file(self, output_path: str | Path | None = None, overwrite: bool = False) -> None:
        output_file = output_path or self.file_path.with_name(f"{self.file_path.stem}_tags.xml")
        output_file = unique_path(output_file) if overwrite else output_file
        self.execute_command("extract", self.file_path, "tags", output_file)

    def extract_tags_as_string(self, file_path: str | Path) -> str:
        return self.execute_command("extract", file_path, "tags", "-")

    def extract_tags_as_dict(self, file_path: str | Path) -> dict[int, Any]:
        xml_content = self.extract_tags_as_string(file_path)
        root = DefusedET.fromstring(xml_content)
        parsed_tags: dict[int, Any] = {}
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
                    parsed_tags.setdefault(target_value, {})[name] = tag
                else:
                    parsed_tags.setdefault(target_value, {}).setdefault(name, []).append(tag)

        if not parsed_tags:
            print("No tags found in the MKV file. Make sure to follow the official MKV tagging guidelines.")
        return parsed_tags

    def _mount_xml(self) -> Element:
        root = Element("Tags")
        for target_int, tag_name, tag_value in self:
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
        output_file = output_path or self.file_path.with_name(f"{self.file_path.stem}_tags.xml")
        output_file = unique_path(output_file) if overwrite else output_file
        ElementTree.ElementTree(self._mount_xml()).write(str(output_file), encoding="utf-8", xml_declaration=True)

    def delete_tags(self) -> None:
        self.execute_command("propedit", self.file_path, "--tags", "all:")

    def add_tags(self) -> None:
        with temp_file(".xml", self.create_tags_as_string()) as temp_path:
            self.execute_command("propedit", self.file_path, "--tags", f"global:{temp_path}")

    def apply_tags(self) -> None:
        self.delete_tags()
        self.add_tags()
