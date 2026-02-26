import argparse
import logging
import os
import re
import shutil
import sys
import typing

import git
from lxml import etree

endings = [
    "auth",
    "anl",
    "base",
    "cmn",
    "ges",
    "log",
    "names",
    "pitched",
    "quality",
    "ratio",
    "vis",
]

attribute_classes_exceptions = {"att.time.base": "att.timeBase"}

element_exceptions = [
    "accidFloatingObject",
    "annot",
    "barLineAttr",
    "divLineAttr",
    "doc",
    "dots",
    "editorTreeObject",
    "flag",
    "genericLayerElement",
    "object",
    "page",
    "pageMilestoneEnd",
    "pages",
    "pitchInflection",
    "stem",
    "system",
    "systemMilestoneEnd",
    "text",
    "textElement",
    "timestampAttr",
    "tupletBracket",
    "tupletNum",
]

element_mapped = {
    "staff": ["vrv::OStaff"]
}

class_to_mei = {"annotScore": "annot"}

doxygen_repo_url = "https://github.com/rism-digital/verovio-doxygen"
tmp_dir = "scripts/tmp/doxygen"
mei_support_output_page = "./_book/05-toolkit-reference/05-mei-support.md"

mei_attribute_base_url = "https://music-encoding.org/guidelines/v5/attribute-classes/"
mei_element_base_url = "https://music-encoding.org/guidelines/v5/elements/"


def format_attribute(vrv_attribute: str) -> str:
    """
    Transform a Verovio attribute class into an MEI one.
    Uses a list of endings and a list of exceptions
    """

    # Split CamelCased strings
    # E.g., AttStaffLocPitched into Att Staff Loc Pitched
    patt = re.compile(r"[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))")
    parts = patt.findall(vrv_attribute)
    # If we have more than three parts, we need to check if the ending is of type .log, or .vis
    # See the endings list
    if len(parts) > 2:
        # If yes, then merge only what is between the att. and the ending
        # E.g., Att Staff Loc Pitched into Att StaffLoc Pitched
        if parts[-1].lower() in endings:
            parts[1:-1] = ["".join(parts[1:-1])]
        # Otherwise merge everything that is after the att.
        # E.g., Att Placement Rel Staff into Att PlacementRelStaff
        else:
            parts[1:] = ["".join(parts[1:])]
    # change case for the first letter of each part and join with a .
    # E.g., Att StaffLoc Pitched into att.staffLoc.Pitched
    base_att = ".".join(v[0].lower() + v[1:] for v in parts)

    # handle exceptions
    if base_att in attribute_classes_exceptions:
        base_att = attribute_classes_exceptions[base_att]

    return f"[{base_att}]({mei_attribute_base_url}{base_att}.html)"


def write_element(
    element: str, attributes: list[str], rows_by_vrv_name: dict[str, str]
) -> None:
    """
    Print the MD content for an element and its attributes.
    """
    # Avoid mutating the argument.
    elname: str = element
    # Doxygen element names are prefixed with vrv::

    if element.startswith("vrv::"):
        elname = element[5:]
    # Change first letter to lower case (StaffGrp into staffGrp)
    elname = elname[0].lower() + elname[1:]

    # Skip exceptions
    if elname in element_exceptions:
        return None

    # Handle name exceptions
    if elname in class_to_mei:
        elname = class_to_mei[elname]

    # Element column
    row_output = "{% row %}\n"
    row_output += (
        f"{{% col 2 %}}\n[\\<{elname}\\>]({mei_element_base_url}{elname}.html)\n{{% endcol %}}\n"
    )
    # Add the description and the links
    row_output += "{% col 10 %}\n"

    # Attribute column
    fmt_att: list[str] = [format_attribute(a) for a in attributes]
    row_output += ", ".join(fmt_att)
    row_output += "\n{% endcol %}\n{% endrow %}\n\n"
    rows_by_vrv_name[element] = row_output

    if (elname in element_mapped):
        for mapped_el in element_mapped[elname]:
            write_element(mapped_el, attributes, rows_by_vrv_name)

    return None


def write_frontmatter(fptr: typing.IO) -> None:
    """
    Print the front matter of the method MD file.
    """
    fptr.write('---\ntitle: "MEI supported elements"\nno-edit: true\n')
    fptr.write("# This file is auto-generated - do not edit\n---\n\n")
    fptr.write(
        "{% aside .warning %} Note that, for the MEI attribute classes listed here, some attributes may not be implemented and that not all possible attribute values are supported. {% endaside %}\n\n"
    )


def remove_tmp_dir() -> None:
    if os.path.isdir(tmp_dir):
        log.debug(f"Deleting '{tmp_dir}'")
        shutil.rmtree(tmp_dir)


if __name__ == "__main__":
    description = """
        Generates documentation for the options available in the Verovio toolkit.
        Creates one file per option category
    """
    parser = argparse.ArgumentParser(description=description)
    verbose_group = parser.add_mutually_exclusive_group()
    verbose_group.add_argument("--verbose", "-v", action="store_true")
    verbose_group.add_argument("--debug", "-d", action="store_true")

    parser.add_argument(
        "--clean", "-c", action="store_true", help="Delete and re-clone."
    )
    parser.add_argument("mode", help="Mode (release or develop)")

    args = parser.parse_args()
    level_msg: str
    if args.debug:
        level_msg = "Debug"
        level = logging.DEBUG
    elif args.verbose:
        level_msg = "Info"
        level = logging.INFO
    else:
        level_msg = "Error"
        level = logging.ERROR

    logging.basicConfig(
        format="[%(asctime)s] [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)",
        level=level,
    )
    log = logging.getLogger(__name__)
    log.info("Running at logging level %s", level_msg)

    clone = True
    if args.clean:
        log.info("Cleaning...")
        remove_tmp_dir()
    elif os.path.isdir(tmp_dir):
        log.info("Directory '%s' already exits.", tmp_dir)
        resp = input(
            "Would you like to remove and clone the doxygen documentation again? (y/N) "
        )

        if resp.strip().lower() in {"y", "yes"}:
            remove_tmp_dir()
        else:
            # The only case where we don't clone is when the directory exists, but we don't want to delete it.
            clone = False

    if clone:
        log.info("Cloning...")
        git.Repo.clone_from(doxygen_repo_url, tmp_dir, branch=args.mode, depth=1)

    with open(mei_support_output_page, "w") as fptr:
        write_frontmatter(fptr)
        rows_by_vrv_name: dict[str, str] = {}

        dir1 = sorted(os.listdir(os.path.join(tmp_dir, "xml")))
        for item1 in dir1:
            # Skip hidden files
            if not item1.endswith(".xml"):
                continue

            if item1 == "index.xml" or item1 == "Doxyfile.xml":
                continue

            xml_file = os.path.join("./", tmp_dir, "xml", item1)
            # print(xml_file)
            xml = etree.parse(xml_file)
            # Find the element (class) name
            vrv_name = xml.xpath("//compoundname[1]/text()[1]")[0]
            vrv_class = xml.xpath("//compoundname[1]")[0]
            # Only MEI classes have the GetClassName method
            mei_element_xml = vrv_class.xpath('//memberdef/name[text()="GetClassName"]')

            if not mei_element_xml:
                continue

            log.debug(vrv_name)
            # Find all parents in the inheritance element
            parents = vrv_class.xpath("//inheritancegraph/node")
            attribute_classes = []
            for parent in parents:
                label = parent.xpath("./label/text()")[0]
                # Attribute classes start with 'Att'
                if not label.startswith("Att"):
                    continue
                log.debug(f"\t{label}")
                attribute_classes.append(label)

            attribute_classes.sort()

            write_element(vrv_name, attribute_classes, rows_by_vrv_name)

        for vrv_name in sorted(rows_by_vrv_name):
            fptr.write(rows_by_vrv_name[vrv_name])

    sys.exit()
