from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# trunk-ignore(bandit/B405)
from xml.etree import ElementTree as ET

# trunk-ignore(bandit/B405)
from xml.etree.ElementTree import Element

from defusedxml import ElementTree as DefusedET

from mkvpy import MKVToolNix
from mkvpy.Tags.info_tags import info_tags, info_targets, order_tags, tags_by_target
from mkvpy.Tags.xml_utils import (
    complex_tag,
    get_or_create_target,
    parse_single_tag,
    simple_tag,
)
from mkvpy.utils import check_file_path, temp_file, unique_path


@dataclass(repr=False)
class BaseTags(MKVToolNix, ABC):
    file_path: Path
    language: str = "und"

    # Campos internos que no entran en el constructor ni se muestran
    _info_file: dict[int, Any] = field(init=False, repr=False, compare=False)

    def __post_init__(self):
        self.file_path: Path = check_file_path(self.file_path)
        self._info_file = self.extract_tags_as_dict(self.file_path)

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        file_name = self.file_path.name
        return f"{class_name} (file='{file_name}', language='{self.language}', num_tags={len(self)})"

    def __iter__(self):
        for tag in order_tags:
            if hasattr(self, tag) and (tag_value := getattr(self, tag)):
                info_tag = info_tags[tag]
                target_int = info_tag.get("target", 50)
                if not isinstance(target_int, int):
                    target_int = 50
                yield (target_int, tag, tag_value)

    def __len__(self) -> int:
        return sum(
            1
            for attr, value in self.__dict__.items()
            if attr in info_tags and value is not None
        )

    def __bool__(self) -> bool:
        return bool(len(self))

    def __contains__(self, item: str | int) -> bool:
        if isinstance(item, str):
            return any(item in tag for _, tag, _ in self)
        elif isinstance(item, int):
            return any(item == target for target, _, _ in self)
        return False

    @abstractmethod
    def _info_targets(self) -> dict[int, str]:
        pass

    def extract_tags_file(
        self,
        output_path: str | Path | None = None,
        overwrite: bool = False,
    ) -> None:
        output_file = output_path or self.file_path.with_name(
            f"{self.file_path.stem}_tags.xml"
        )
        output_file = unique_path(output_file) if overwrite else output_file
        self.execute_command("extract", self.file_path, "tags", output_file)

    def extract_tags_as_string(self, file_path: str | Path) -> str:
        return self.execute_command("extract", file_path, "tags", "-")

    def extract_tags_as_dict(self, file_path: str | Path) -> dict[int, Any]:
        xml_content = self.extract_tags_as_string(file_path)
        root = DefusedET.fromstring(xml_content)
        parsed_tags: dict[int, Any] = {}

        for tag_element in root.findall("Tag"):
            target_value = 50
            if v := tag_element.findtext("./Targets/TargetTypeValue"):
                target_value = (
                    int(v or 0) if v.isdigit() and v in info_targets.values() else 50
                )
            elif t := tag_element.findtext("./Targets/TargetType"):
                target_value = info_targets.get(t, 50)

            for simple in tag_element.findall("Simple"):
                key, tag = parse_single_tag(simple)
                if key is None or tag is None:
                    continue
                name = tags_by_target.get(target_value, {}).get(key, "")
                parsed_tags.setdefault(target_value, {}).setdefault(name, []).append(
                    tag
                )

        if not parsed_tags:
            print(
                "No tags found in the MKV file. Make sure to follow the official MKV tagging guidelines."
            )
        return parsed_tags

    def _mount_xml(self) -> Element:
        root = Element("Tags")
        for target_int, tag_name, tag_value in self:
            info_target = self._info_targets().get(target_int, "MOVIE")
            target = get_or_create_target(root, target_int, info_target)
            for value in tag_value:
                if isinstance(tag_name, tuple):
                    target.append(complex_tag(tag_name, value))
                elif isinstance(tag_name, str):
                    target.append(simple_tag(tag_name, value))
        return root

    def create_tags_as_string(self) -> str:
        return ET.tostring(self._mount_xml(), encoding="utf-8").decode("utf-8")

    def create_file_tags(
        self,
        output_path: str | Path | None = None,
        overwrite: bool = False,
    ) -> None:
        output_file = output_path or self.file_path.with_name(
            f"{self.file_path.stem}_tags.xml"
        )
        output_file = unique_path(output_file) if overwrite else output_file
        ET.ElementTree(self._mount_xml()).write(
            str(output_file), encoding="utf-8", xml_declaration=True
        )

    def delete_tags(self) -> None:
        self.execute_command("propedit", self.file_path, "--tags", "all:")

    def add_tags(self) -> None:
        with temp_file(
            suffix=".xml", content=self.create_tags_as_string()
        ) as temp_path:
            self.execute_command(
                "propedit", self.file_path, "--tags", f"global:{temp_path}"
            )

    def apply_tags(self) -> None:
        self.delete_tags()
        with temp_file(
            suffix=".xml", content=self.create_tags_as_string()
        ) as temp_path:
            self.execute_command(
                "propedit", self.file_path, "--tags", f"global:{temp_path}"
            )
