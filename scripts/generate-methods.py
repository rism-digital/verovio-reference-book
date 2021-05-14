import argparse
import frontmatter
import json
import logging
from lxml import etree
import os
import pprint
import regex
import requests
import sys
from typing import Dict, List
import yaml

header_url = "https://raw.githubusercontent.com/rism-digital/verovio-doxygen/{}/xml/classvrv_1_1_toolkit.xml"
header_tmp_dir = "scripts/tmp"
header_tmp_name = "classvrv_1_1_toolkit.xml"
methods_ouptut_page = "./_book/05-toolkit-reference/03-toolkit-methods.md"

def get_text_for_nodes(xml_nodes):
    text = ""
    for node_text in xml_nodes:
        text += node_text
    return text.strip()
    
def extract_method(xml_node):
    description = """
        Extract the method relevant part from a Doxygen XML node
        Put everything into a dictionary
    """

    method = {}
    method['id'] = xml_node.get("id")
    method['name'] = xml_node.findtext('name')
    doc_id = method['name'].lower()
    method['type'] = xml_node.findtext('type')
    xml_desc = xml_node.xpath(".//detaileddescription/para/simplesect[@kind='return']")
    # look for the description of return
    if xml_desc:
        texts = xml_desc[0].xpath('./descendant::*/text()')
        method['return-simplesect'] = get_text_for_nodes(texts)

    method['definition'] = xml_node.findtext('definition')
    method['argsstring'] = xml_node.findtext('argsstring')
    params = []
    # look for all parameters
    xml_params = xml_node.findall('param')
    for xml_param in xml_params:
        param = {}
        declname = xml_param.findtext('declname') 
        param['declname'] = declname 
        doc_id += "-{}".format(declname.lower())
        param['type'] = xml_param.findtext('type') 
        param['defval'] = xml_param.findtext('defval')    
        # loolk for the description of a parameter
        xml_desc = xml_node.xpath(".//parameteritem[parameternamelist/parametername/text()='{}']".format(declname))
        if xml_desc:
            texts = xml_desc[0].xpath('./parameterdescription/descendant::*/text()')
            param['parameterdescription'] =  get_text_for_nodes(texts)
        params.append(param) 

    method['params'] = params
    method['doc_id'] = doc_id
 
    briefdescription = ""
    texts = xml_node.xpath('./briefdescription/descendant::*/text()')
    method['briefdescription'] = get_text_for_nodes(texts)

    detaileddescription = ""
    texts = xml_node.xpath('./detaileddescription/descendant::*[not(ancestor::parameterlist) and not(ancestor::simplesect)]/text()')
    method['detaileddescription'] = get_text_for_nodes(texts)
    
    return method

def format_python_example(method):
    description = """
        Format a Python example call
    """
    example = ""
    name = method['name']
    name = name[0].lower() + name[1:]
    if method.get('type') != "void":
        example = "result = "
    example += "toolkit." + name + "("
    params = []
    for param in method['params']:
        params.append(param['declname'])
    example += ", ".join(params)
    example += ")"
    return example

def print_method(method, file):
    description = """
        Print the MD content for a method.
    """

    # header, short and long descrtiption
    file.write("### {}\n\n".format(method['name']))
    if method.get('briefdescription'):
        file.write("{}\n\n".format(method['briefdescription']))
    if method.get('detaileddescription'):
        file.write("{}\n\n".format(method['detaileddescription']))

    # return
    if method.get('type'):
        file.write("**Returns**\n\n`{}`".format(method['type']))
        if method.get('return-simplesect'):
            file.write(" – {}".format(method['return-simplesect']))
        file.write("\n\n")

    # paramter table
    if method.get('params'):
        file.write("**Parameters**\n\n|---|---|---|\n| Name | Type | Default | Description |\n")
        for param in method['params']:
            file.write("| `{}` ".format(param['declname'] if param.get('declname') else ''))
            file.write("| `{}` ".format(param['type'] if param.get('type') else ''))
            defval = "`{}`".format(param['defval']) if param.get('defval') and param['defval'] != 'null' else '∅'
            file.write("| {} ".format(defval))
            file.write("| {} |\n".format(param['parameterdescription'] if param.get('parameterdescription') else ''))
        file.write("{: .table .table-condensed .table-sm .text-xsmall}\n\n")

    # C++ original header
    if method.get('definition') and method.get('argsstring'):
        file.write("**Original header**\n\n```cpp\n{}{}\n```\n\n".format(method['definition'], method['argsstring']))

    # Python example call
    file.write("**Example call**\n\n```python\n{}\n```\n\n".format(format_python_example(method)))

    # Extended documentation include
    file.write("{{% include method-doc file=\"{}\" %}}\n".format(method['doc_id']))

def print_frontmatter(file):
    description = """
        Print the front matter of the method MD file.
    """
    file.write('---\ntitle: "Toolkit methods"\nno-edit: true\n')
    file.write('# This file is auto-generated - do not edit\n---\n\n')

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

    # Download the header_file file from the given url
    url = header_url.format(args.mode)
    log.debug("Downloading %s", url)
    header_file = requests.get(url)

    if 200 <= header_file.status_code < 400:
        log.info("%s successfully downloaded", url)
    else:
        log.error("Problem downloading %s. Skipping this example", url)
        sys.exit()

            # create the output directory if necessary
    if not(os.path.isdir(header_tmp_dir)):
        os.mkdir(header_tmp_dir)

    header_tmp_file = os.path.join(header_tmp_dir, header_tmp_name)
    # Save the file locally for parsing
    with open(header_tmp_file, 'w') as f:
        f.write(header_file.text)

    index_xml = etree.parse(header_tmp_file)

    # get the toolkit class
    toolkit = index_xml.xpath('//compoundname[text()="vrv::Toolkit"]')[0]

    # get all the public methods
    doxygen_methods = toolkit.xpath('//memberdef[@kind="function" and @prot="public" and not(starts-with(@id, "group__nodoc_"))]')

    # extract their content into an array of dictionaries
    methods = []
    for doxygen_method in doxygen_methods:
        # Skip the destructor
        if doxygen_method.findtext('name') == "~Toolkit":
            continue
        methods.append(extract_method(doxygen_method))

    # sort them by method name
    def sortName(elem):
        return elem.get('name')

    methods.sort(key=sortName)

    file = open(methods_ouptut_page, 'w')
    print_frontmatter(file)

    for method in methods:
        print_method(method, file)

    file.close()

    # Save file for documentation
    with open("_data/methods.yml", 'w') as yml_file:
        yaml.dump(methods, yml_file)

    sys.exit()
