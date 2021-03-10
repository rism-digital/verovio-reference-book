import argparse
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

    #print(options)



    for grp_id in options['groups']:

        # Open the file for the option group
        f = open(options_output + grp_id + ".md", 'w')
        # Table header in MD
        f.write("| Name and parameter | Description | See also |\n")
        f.write("|---|---|---|\n")

        grp = options['groups'][grp_id]
        
        for option_id in grp['options']:
            option = grp['options'][option_id]

            # Use regex to transform JSON option names into Cmd-line option names
            # E.g, transform adjustPageHeight into --adjust-page-height
            cmd_option = option_id
            cmd_option = regex.sub(r"(.)([A-Z][a-z]+)", r"\1-\2", cmd_option)
            cmd_option = regex.sub(r"([a-z0-9])([A-Z])", r"\1-\2", cmd_option)
            cmd_option = "--{}".format(cmd_option.lower())

            # Add the parameter type
            # <f> / <i> / <s> / * <s>
            opt_type_str = ""
            opt_type = option.get('type')
            if opt_type == 'double':
                opt_type_str = " &lt;f&gt;"
            elif opt_type == 'int':
                opt_type_str = " &lt;i&gt;"
            elif opt_type == 'std::string':
                opt_type_str = " &lt;s&gt;"
            elif opt_type == 'array':
                opt_type_str = "* &lt;s&gt;"
            elif opt_type != 'bool':
                opt_type_str = " &lt;s&gt;"

            # Add the default values when appropriate
            default_str = ""
            if opt_type == 'double':
                default_str =  "<br/>(default: " + str(option['default'])
                default_str +=  "; min: " + str(option['min'])
                default_str +=  "; max: " + str(option['max']) + ")"
            elif opt_type == 'int':
                default_str =  "<br/>(default: " + str(option['default'])
                default_str +=  "; min: " + str(option['min'])
                default_str +=  "; max: " + str(option['max']) + ")"
            elif opt_type == 'std::string':
                default_str =  "<br/>(default: \"" + option['default'] + "\")"
            elif opt_type == 'std::string-list':
                default_str =  "<br/>(default: \"" + option['default']
                default_str += "\"; other values: " + str(option['values']) + ")"

            description = option['description']
            description = "{}{}".format(description, default_str)
            
            see_also = "[Link](link-to)"

            # Add the table line with span.lang1 / span.lang2 for toggling JSON and Cmd-line
            f.write("| <span class=\"lang1\">{}</span><span class=\"lang2\">{}</span>{} ".format(option_id, cmd_option, opt_type_str))
            f.write("| {} | {} |\n".format(description, see_also))

        f.write("{: .table .table-condensed}\n")
        f.close()

    log.debug("Finished processing")

    sys.exit()
