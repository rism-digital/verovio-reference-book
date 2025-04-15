import argparse
import frontmatter
import git
import json
import logging
from lxml import etree
import os
import pprint
import regex
import requests
import shutil
import sys
from typing import Dict, List
import yaml

endings = ["auth", "anl", "base", "cmn", "ges", "log", "names", "pitched", "quality", "ratio", "vis"] 

attribute_classes_exceptions = {
    "att.time.base": "att.timeBase"
}

element_exceptions = ["barLineAttr", "dots", "flag", "page", "pageElementEnd", "pages", "object", "stem", "system", "systemElementEnd", "text", "textElement", "timestampAttr", "tupletBracket", "tupletNum"]

doxygen_repo_url = "https://github.com/rism-digital/verovio-doxygen"
tmp_dir = "scripts/tmp/doxygen"
mei_support_output_page = "./_book/05-toolkit-reference/05-mei-support.md"

mei_attribute_base_url = "https://music-encoding.org/guidelines/v5/attribute-classes/"
mei_element_base_url = "https://music-encoding.org/guidelines/v5/elements/"

def format_attribute(vrv_attribute):
    description = """
        Transform a Verovio attribute class into an MEI one.
        Uses a list of endings and a list of exceptions
    """

    # Split CamelCased strings
    # E.g., AttStaffLocPitched into Att Staff Loc Pitched
    patt = regex.compile(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))')
    parts = patt.findall(vrv_attribute)
    # If we have more than three parts, we need to check if the ending is of type .log, or .vis
    # See the endings list
    if len(parts) > 2:
        # If yes, then merge only what is between the att. and the ending
        # E.g., Att Staff Loc Pitched into Att StaffLoc Pitched
        if parts[-1].lower() in endings:
            parts[1:-1]=["".join(parts[1:-1])]
        # Otherwise merge everything that is after the att.
        # E.g., Att Placement Rel Staff into Att PlacementRelStaff 
        else:
            parts[1:]=["".join(parts[1:])]
    # change case for the first letter of each part and join with a .
    # E.g., Att StaffLoc Pitched into att.staffLoc.Pitched
    attribute = ".".join(v[0].lower() + v[1:] for v in parts)
    
    # handle exceptions
    if attribute_classes_exceptions.get(attribute):
        attribute = attribute_classes_exceptions.get(attribute)
    return attribute

def print_element(element, attributes, file):
    description = """
        Print the MD content for an element and its attributes.
    """

    # Doxygen element names are prefixed with vrv::
    if element.startswith("vrv::"):
        element = element[len("vrv::"):]
    # Change first letter to lower case (StaffGrp into staffGrp)
    element = element[0].lower() + element[1:]

    # Skip exceptions
    if element in element_exceptions:
        return

    # Element column
    file.write("{% row %}\n")
    file.write("{{% col 2 %}}\n[\<{}\>]({}{}.html)\n{{% endcol %}}\n".format(element, mei_element_base_url, element))
    # Add the descripion and the links
    file.write("{% col 10 %}\n")

    # Attribute column
    first = True
    for attribute in attributes:
        if not first:
            file.write(", ")
        first = False
        attribute = format_attribute(attribute)
        #print(attribute)
        file.write("[{}]({}{}.html)".format(attribute, mei_attribute_base_url, attribute))

    file.write("\n{% endcol %}\n{% endrow %}\n\n")

def print_frontmatter(file):
    description = """
        Print the front matter of the method MD file.
    """
    file.write('---\ntitle: "MEI supported elements"\nno-edit: true\n')
    file.write('# This file is auto-generated - do not edit\n---\n\n')
    file.write('{% aside .warning %} Note that, for the MEI attribute classes listed here, some attributes may not be implemented and that not all possible attribute values are supported. {% endaside %}\n\n')

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

    logging.basicConfig(format="[%(asctime)s] [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)",
                        level=level)
    log = logging.getLogger(__name__)
    log.info("Running at logging level %s", level_msg)

    clone = False
    if os.path.isdir(tmp_dir):
        log.info("Directory '{}' already exits.".format(tmp_dir)) 
        delete_files = input('Would you like to remove and clone the doxygen documentation again? (y/N)')
        if delete_files in ['Y', 'y', 'Yes', 'yes', 'YES']:
            log.debug("Deleting '{}'".format(tmp_dir)) 
            shutil.rmtree(tmp_dir)
            clone = True
    else:
        clone = True

    if clone:  
        log.info("Cloning...")      
        git.Repo.clone_from(doxygen_repo_url, tmp_dir, branch=args.mode, depth=1)

    file = open(mei_support_output_page, 'w')
    print_frontmatter(file)

    dir1 = sorted(os.listdir(os.path.join(tmp_dir, 'xml')))
    for item1 in dir1:
            # Skip hidden files
            if not item1.endswith('.xml'):
                continue
            if item1 == 'index.xml' or item1 == 'Doxyfile.xml':
                continue 

            xml_file = os.path.join('./', tmp_dir, 'xml', item1)
            #print(xml_file)
            xml = etree.parse(xml_file)
            # Find the element (class) name
            vrv_name = xml.xpath('//compoundname[1]/text()[1]')[0]
            vrv_class = xml.xpath('//compoundname[1]')[0]
            # Only MEI classes have the GetClassName method
            mei_element_xml = vrv_class.xpath('//memberdef/name[text()="GetClassName"]')
            if not mei_element_xml:
                continue

            log.debug(vrv_name)
            # Find all parents in the inheritance element
            parents = vrv_class.xpath('//inheritancegraph/node')
            attribute_classes = []
            for parent in parents:
                label = parent.xpath('./label/text()')[0]
                # Attribute classes start with 'Att'
                if not label.startswith('Att'):
                    continue
                log.debug("\t{}".format(label))
                attribute_classes.append(label)

            if attribute_classes:
                attribute_classes.sort()
            print_element(vrv_name, attribute_classes, file)

    file.close()

    sys.exit()
