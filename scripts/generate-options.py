import argparse
import frontmatter
import json
import os
import sys
import pprint
import regex
from typing import Dict, List
import logging

import verovio
import yaml

options_index_page = "./_book/05-toolkit-reference/04-toolkit-options.md"
options_output = "./_includes/options/"
toc_file = "scripts/toc.yaml"

if __name__ == "__main__":
    description = """
        Generates documentation for the options available in the Verovio toolkit.
        Creates one file per option category
    """
    parser = argparse.ArgumentParser(description=description)
    verbose_group = parser.add_mutually_exclusive_group()
    verbose_group.add_argument("--verbose", "-v", action="store_true")
    verbose_group.add_argument("--debug", "-d", action="store_true")

    #parser.add_argument("examples", help="Path to examples.yaml file")

    see_also = {}
    with open(options_index_page, 'r') as file:
        options_file = frontmatter.loads(file.read())
        see_also = options_file.get('see-also', {})

    toc = {}
    with open(toc_file, 'r') as file:
        toc: Dict = yaml.full_load(file)

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

    tk = verovio.toolkit()
    # version of the toolkit
    log.info("Using Verovio %s", tk.getVersion())

    # keep all the options to be able to reset them for each example
    options: Dict = json.loads(tk.getAvailableOptions())

    for grp_id, grp in options['groups'].items():
        # Open the file for the option group
        f = open(options_output + grp_id + ".md", 'w')
        # Table header in MD
        #f.write("| Name and parameter | Description | See also |\n")
        #f.write("|---|---|---|\n")
        
        for option_id, option in grp['options'].items():

            # Use regex to transform JSON option names into Cmd-line option names
            # E.g, transform adjustPageHeight into --adjust-page-height
            cmd_option = option_id
            cmd_option = regex.sub(r"(.)([A-Z][a-z]+)", r"\1-\2", cmd_option)
            cmd_option = regex.sub(r"([a-z0-9])([A-Z])", r"\1-\2", cmd_option)
            cmd_option = "--{}".format(cmd_option.lower())

            if option.get('shortOption'):
                cmd_option = "-{}, {}".format(option['shortOption'], cmd_option)

            # Add the parameter type
            opt_type_str = ""
            opt_type = option.get('type')
            if opt_type == 'double':
                opt_type_str = " <f>"
            elif opt_type == 'int':
                opt_type_str = " <i>"
            elif opt_type == 'std::string':
                opt_type_str = " <s>"
            elif opt_type == 'array':
                opt_type_str = "* <s>"
            elif opt_type != 'bool':
                opt_type_str = " <s>"

            opt_type_json_str = opt_type_str
            if opt_type == 'bool':
                opt_type_json_str = " <br>"

            cmd_option_str = "`{} {}`".format(cmd_option, opt_type_str)
            json_option_str = "`\"{}\": {}`".format(option_id, opt_type_json_str)

            # Add the default values when appropriate
            default_str = ""
            if opt_type == 'double':
                default_str =  "<br/>(default: " + str(option['default'])
                default_str +=  "; min: " + str(option['min'])
                default_str +=  "; max: " + str(option['max']) + ")"
            elif opt_type == 'int' and (option['default'] != option['min'] != option['max']):
                default_str =  "<br/>(default: " + str(option['default'])
                default_str +=  "; min: " + str(option['min'])
                default_str +=  "; max: " + str(option['max']) + ")"
            elif opt_type == 'std::string':
                default_str =  "<br/>(default: \"" + option['default'] + "\")"
            elif opt_type == 'std::string-list':
                default_str =  "<br/>(default: \"" + option['default']
                default_str += "\"; other values: " + str(option['values']) + ")"

            # Add the description
            description = option['description']
            description = "{}{}".format(description, default_str)

            # Check if we have an extended description in _includes/options/
            extended_description = os.path.join(options_output, grp_id,option_id + ".md")
            if os.path.exists(extended_description):
                log.info("Include extended description %s", extended_description)
                description += ("\n\n{{% include {} %}}".format(os.path.join("options", grp_id, option_id + ".md")))
            
            # If we have one or more see-also entries in the option.md, add the links
            see_also_this = see_also.get(option_id)
            see_also_str = ""
            if see_also_this:
                see_also_str = "See also: "
                see_also_links = []
                for ref in see_also_this:
                    # Get the name of the link target from the scripts/toc.yaml file
                    link = "[{}]({})".format(toc.get(ref, "[missing]"), ref)
                    see_also_links.append(link)
                see_also_str += " \\| ".join(see_also_links)

            if option.get('cmdOnly'):
                json_option_str = "∅"

            # Add the table line with span.lang1 / span.lang2 for toggling JSON and Cmd-line
            #f.write("| <span class=\"lang1\">{}</span><span class=\"lang2\">{}</span> ".format(json_option_str, cmd_option_str))
            f.write("{% row %}")
            f.write("{{% col 3 %}} <span class=\"lang1\">{}</span><span class=\"lang2\">{}</span> {{% endcol %}}".format(json_option_str, cmd_option_str))
            # Add the descripion and the links
            f.write("{{% col 6 %}} {} {{% endcol %}}{{% col 3 %}} {} {{% endcol %}}\n".format(description, see_also_str))
            f.write("{% endrow %}")

        f.close()

    log.debug("Finished processing")

    sys.exit()
