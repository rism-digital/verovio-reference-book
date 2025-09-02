import argparse
import logging
import os
import sys

import requests
import yaml
from lxml import etree

header_url = "https://raw.githubusercontent.com/rism-digital/verovio-doxygen/{}/xml/classvrv_1_1_toolkit.xml"
header_tmp_dir = "scripts/tmp"
header_tmp_name = "classvrv_1_1_toolkit.xml"
methods_output_page = "./_book/05-toolkit-reference/03-toolkit-methods.md"


def extract_nojs_name(xml_node):
    """
    Extract the name of nojs method from a Doxygen XML node
    """
    return xml_node.findtext("name")


def extract_method(xml_node) -> dict:
    """
    Extract the method relevant part from a Doxygen XML node
    Put everything into a dictionary
    """

    m: dict = {
        "id": xml_node.get("id"),
        "name": xml_node.findtext("name"),
        "type": xml_node.findtext("type"),
        "definition": xml_node.findtext("definition"),
        "argsstring": xml_node.findtext("argsstring"),
    }

    doc_id = m["name"].lower()
    xml_desc = xml_node.xpath(".//detaileddescription/para/simplesect[@kind='return']")
    # look for the description of return
    if xml_desc:
        texts = xml_desc[0].xpath("./descendant::*/text()")
        m["return-simplesect"] = "".join(texts).strip()

    params = []
    # look for all parameters
    xml_params = xml_node.findall("param")
    for xml_param in xml_params:
        declname = xml_param.findtext("declname")
        doc_id += f"-{declname.lower()}"
        param: dict = {
            "declname": declname,
            "type": xml_param.findtext("type"),
            "defval": xml_param.findtext("defval"),
        }

        # look for the description of a parameter
        xml_desc = xml_node.xpath(
            f".//parameteritem[parameternamelist/parametername/text()='{declname}']"
        )
        if xml_desc:
            texts = xml_desc[0].xpath("./parameterdescription/descendant::*/text()")
            param["parameterdescription"] = "".join(texts).strip()

        params.append(param)

    m["params"] = params
    m["doc_id"] = doc_id

    texts = xml_node.xpath("./briefdescription/descendant::*/text()")
    m["briefdescription"] = "".join(texts).strip()

    texts = xml_node.xpath(
        "./detaileddescription/descendant::*[not(ancestor::parameterlist) and not(ancestor::simplesect)]/text()"
    )
    m["detaileddescription"] = "".join(texts).strip()

    return m


def format_python_example(mthd: dict) -> str:
    """
    Format a Python example call
    """
    name = mthd["name"]
    name = name[0].lower() + name[1:]

    res_pfx: str = ""
    if mthd.get("type") != "void":
        res_pfx = "result = "

    params = ", ".join([p["declname"] for p in mthd["params"]])

    return f"{res_pfx}toolkit.{name}({params})"


def write_method(mthd: dict, fptr) -> None:
    """
    Print the MD content for a method.
    """

    # header, short and long description
    fptr.write(f"### {mthd['name']}\n\n")
    if mthd.get("briefdescription"):
        fptr.write(f"{mthd['briefdescription']}\n\n")
    if mthd.get("detaileddescription"):
        fptr.write(f"{mthd['detaileddescription']}\n\n")

    if mthd.get("nojs"):
        fptr.write(
            f"{{% aside .warning %}}{'This method is not available in the JavaScript distributed version of the toolkit'}{{% endaside %}}\n\n"
        )

    # return
    if mthd.get("type"):
        fptr.write(f"**Returns**\n\n`{mthd['type']}`")
        if mthd.get("return-simplesect"):
            fptr.write(f" – {mthd['return-simplesect']}")
        fptr.write("\n\n")

    # parameter table
    if mthd.get("params"):
        fptr.write(
            "**Parameters**\n\n|---|---|---|\n| Name | Type | Default | Description |\n"
        )
        for param in mthd["params"]:
            fptr.write(f"| `{param['declname'] if param.get('declname') else ''}` ")
            fptr.write(f"| `{param['type'] if param.get('type') else ''}` ")
            defval = (
                f"`{param['defval']}`"
                if param.get("defval") and param["defval"] != "null"
                else "∅"
            )
            fptr.write(f"| {defval} ")
            fptr.write(
                f"| {param['parameterdescription'] if param.get('parameterdescription') else ''} |\n"
            )
        fptr.write("{: .table .table-condensed .table-sm .text-xsmall}\n\n")

    # C++ original header
    if mthd.get("definition") and mthd.get("argsstring"):
        fptr.write(
            f"**Original header**\n\n```cpp\n{mthd['definition']}{mthd['argsstring']}\n```\n\n"
        )

    # Python example call
    fptr.write(f"**Example call**\n\n```python\n{format_python_example(mthd)}\n```\n\n")

    # Extended documentation include
    fptr.write(f'{{% include method-doc file="{mthd["doc_id"]}" %}}\n')


def write_frontmatter(fptr) -> None:
    """
    Print the front matter of the method MD file.
    """
    fptr.write('---\ntitle: "Toolkit methods"\nno-edit: true\n')
    fptr.write("# This file is auto-generated - do not edit\n---\n\n")

    # Extended documentation include
    fptr.write('{% include method-doc file="introduction" %}\n\n')


if __name__ == "__main__":
    description = """
        Generates documentation for the options available in the Verovio toolkit.
        Creates one file per option category
    """
    parser = argparse.ArgumentParser(description=description)
    verbose_group = parser.add_mutually_exclusive_group()
    verbose_group.add_argument("--verbose", "-v", action="store_true")
    verbose_group.add_argument("--debug", "-d", action="store_true")

    parser.add_argument("mode", help="Mode (release or develop)")

    args = parser.parse_args()
    if args.debug:
        level_msg: str = "Debug"
        level = logging.DEBUG
    elif args.verbose:
        level_msg: str = "Info"
        level = logging.INFO
    else:
        level_msg: str = "Error"
        level = logging.ERROR

    logging.basicConfig(
        format="[%(asctime)s] [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)",
        level=level,
    )
    log = logging.getLogger(__name__)
    log.info("Running at logging level %s", level_msg)

    # Download the header_file file from the given url
    url = header_url.format(args.mode)
    log.debug("Downloading %s", url)
    header_file = requests.get(url, timeout=10)

    if 200 <= header_file.status_code < 400:
        log.info("%s successfully downloaded", url)
    else:
        log.error("Problem downloading %s. Skipping this example", url)
        sys.exit()

        # create the output directory if necessary
    if not os.path.isdir(header_tmp_dir):
        os.mkdir(header_tmp_dir)

    header_tmp_file = os.path.join(header_tmp_dir, header_tmp_name)
    # Save the file locally for parsing
    with open(header_tmp_file, "w") as f:
        f.write(header_file.text)

    index_xml = etree.parse(header_tmp_file)

    # get the toolkit class
    toolkit = index_xml.xpath('//compoundname[text()="vrv::Toolkit"]')[0]

    # get all the methods not supported in the JS toolkit mark with a @remark nojs
    doxygen_nojss = toolkit.xpath(
        '//memberdef[@kind="function" and @prot="public" and ./detaileddescription/para/simplesect[@kind="remark"]/para/text()="nojs"]'
    )

    # extract their content into an array of dictionaries
    nojs_methods = []
    for doxygen_nojs in doxygen_nojss:
        nojs_methods.append(extract_nojs_name(doxygen_nojs))

    # get all the public methods
    doxygen_methods = toolkit.xpath(
        '//memberdef[@kind="function" and @prot="public" and not(starts-with(@id, "group__nodoc_"))]'
    )

    # extract their content into an array of dictionaries
    methods = [
        extract_method(d) for d in doxygen_methods if d.findtext("name") != "~Toolkit"
    ]

    # sort them by method name
    methods.sort(key=lambda n: n.get("name"))

    with open(methods_output_page, "w") as methods_out:
        write_frontmatter(methods_out)

        for method in methods:
            if method.get("name") in nojs_methods:
                print(method["name"])
                method["nojs"] = True
            write_method(method, methods_out)

    # Save file for documentation
    if not (os.path.isdir("_data")):
        os.mkdir("_data")

    with open("_data/methods.yml", "w") as yml_file:
        yaml.dump(methods, yml_file)

    sys.exit()
