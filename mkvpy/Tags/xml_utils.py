from __future__ import annotations

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


def get_text_element(elem: ET.Element, tag: str) -> str | None:
    found_elem = (elem.findtext(tag) or "").strip()
    return " ".join(found_elem.split()) if found_elem else None


def parse_single_tag(
    element: ET.Element,
) -> tuple[tuple | str | None, tuple | str | int | float | None]:
    """
    Parse a single tag element and return its name and value.
    If the tag has nested Simple elements, return a dictionary of name-value pairs.
    """

    name_1 = get_text_element(element, "Name")
    value_1 = get_text_element(element, "String")

    if not name_1 or not value_1:
        return None, None

    if element.find("Simple") is not None:
        pairs = [
            (name, value)
            for simple in element.findall("Simple")
            if (name := get_text_element(simple, "Name"))
            and (value := get_text_element(simple, "String"))
        ]
        name_x, value_x = zip(*pairs) if pairs else ([], [])
        return ((name_1, *name_x), (value_1, *value_x))

    return name_1, value_1


def get_or_create_target(
    root: Element, target_type_value: int, target_type: str
) -> Element:

    for tag in root.findall("Tag"):
        ttv = tag.findtext("Targets/TargetType")
        if ttv == target_type:
            return tag

    new_tag = ET.SubElement(root, "Tag")
    target_elem = ET.SubElement(new_tag, "Targets")
    ET.SubElement(target_elem, "TargetTypeValue").text = str(target_type_value)
    ET.SubElement(target_elem, "TargetType").text = target_type

    return new_tag


def simple_tag(tag_name: str, tag_value: str | int | float) -> Element:
    element = ET.Element("Simple")
    ET.SubElement(element, "Name").text = tag_name
    ET.SubElement(element, "String").text = str(tag_value)
    return element


def complex_tag(names: tuple[str], values: tuple[str]) -> Element:
    name_1, name_x = names[0], names[1:]
    value_1, value_x = values[0], values[1:]
    primary_element = simple_tag(name_1, value_1)
    for name, value in zip(name_x, value_x):
        primary_element.append(simple_tag(name, value))
    return primary_element
