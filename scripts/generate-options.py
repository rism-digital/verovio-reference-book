import argparse
import html
import logging
import os
import re
import sys

import frontmatter
import verovio
import yaml

if __name__ == "__main__":
    description = """
        Generates documentation for the options available in the Verovio toolkit.
        Creates one file per option category
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--index",
        "-i",
        dest="options_index_page",
        default="_book/05-toolkit-reference/04-toolkit-options.md",
    )
    parser.add_argument(
        "--output", "-o", dest="options_output", default="_includes/options/"
    )
    parser.add_argument("--toc", "-t", dest="toc_file", default="scripts/toc.yaml")
    verbose_group = parser.add_mutually_exclusive_group()
    verbose_group.add_argument("--verbose", "-v", action="store_true")
    verbose_group.add_argument("--debug", "-d", action="store_true")
    # parser.add_argument("examples", help="Path to examples.yaml file")
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

    # some basic sanity checks.
    if not os.path.exists(args.options_index_page):
        log.error("Could not find the options index page file.")
        sys.exit(-1)

    if not os.path.exists(args.toc_file):
        log.error("Could not find the TOC file.")
        sys.exit(-1)

    if not os.path.exists(args.options_output):
        log.error("The output directory does not exist.")
        sys.exit(-1)

    with open(args.options_index_page) as file:
        options_file = frontmatter.loads(file.read())
        file_meta: dict = options_file.metadata
        see_also: dict = file_meta.get("see-also", {})

    with open(args.toc_file) as file:
        toc = yaml.full_load(file)

    tk = verovio.toolkit()
    # version of the toolkit
    log.info("Using Verovio %s", tk.getVersion())

    # keep all the options to be able to reset them for each example
    options: dict = tk.getAvailableOptions()

    for grp_id, grp in options["groups"].items():
        # Open the file for the option group
        with open(os.path.join(args.options_output, f"{grp_id}.md"), "w") as f:
            # Table header in MD
            # f.write("| Name and parameter | Description | See also |\n")
            # f.write("|---|---|---|\n")

            for option_id, option in grp["options"].items():
                # Use regex to transform JSON option names into Cmd-line option names
                # E.g, transform adjustPageHeight into --adjust-page-height
                cmd_option: str = option_id
                cmd_option = re.sub(r"(.)([A-Z][a-z]+)", r"\1-\2", cmd_option)
                cmd_option = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", cmd_option)
                cmd_option = f"--{cmd_option.lower()}"

                if so := option.get("shortOption"):
                    cmd_option = f"-{so}, {cmd_option}"

                # Add the parameter type
                opt_type_str: str = ""
                opt_type: str | None = option.get("type")

                if opt_type == "double":
                    opt_type_str = "<decimal>"
                elif opt_type == "int":
                    opt_type_str = "<integer>"
                elif opt_type == "std::string":
                    opt_type_str = "<string>"
                elif opt_type == "array":
                    opt_type_str = "<string> *"
                elif opt_type != "bool":
                    opt_type_str = "<string>"

                opt_type_json_str = opt_type_str
                if opt_type == "bool":
                    opt_type_json_str = " <boolean>"

                cmd_option_str: str = f"`{cmd_option} {opt_type_str}`"
                json_option_str: str = f'`"{option_id}": {opt_type_json_str}`'

                # Add the default values when appropriate
                default_str: str = ""
                if (
                    opt_type == "double"
                    or opt_type == "int"
                    and (option["default"] != option["min"] != option["max"])
                ):
                    default_str = f"<br/>(default: {str(option['default'])}; min: {str(option['min'])}; max: {str(option['max'])})"
                elif opt_type == "std::string":
                    default_str = f'<br/>(default: "{option["default"]}")'
                elif opt_type == "std::string-list":
                    default_str = f'<br/>(default: "{option["default"]}"; other values: {str(option["values"])})'

                # Add the description
                initial_description: str = option["description"]
                # Some descriptions have XML tags which get hidden when rendered. Escape them
                # so that they use HTML entities instead.
                escaped_description = html.escape(initial_description)
                description = f"{escaped_description}{default_str}"

                # Check if we have an extended description in _includes/options/
                extended_description = os.path.join(
                    args.options_output, grp_id, f"{option_id}.md"
                )
                if os.path.exists(extended_description):
                    log.info("Include extended description %s", extended_description)
                    description += f"\n\n{{% include {os.path.join('options', grp_id, option_id + '.md')} %}}"

                # If we have one or more see-also entries in the option.md, add the links
                see_also_this = see_also.get(option_id)
                see_also_str = ""
                if see_also_this:
                    see_also_str = "\n\nSee also: "
                    see_also_links = []
                    for ref in see_also_this:
                        # Get the name of the link target from the scripts/toc.yaml file
                        link = f"[{toc.get(ref, '[missing]')}]({ref})"
                        see_also_links.append(link)
                    see_also_str += " \\| ".join(see_also_links)
                description += see_also_str

                if option.get("cmdOnly"):
                    json_option_str = "∅"

                # Add the table line with span.lang1 / span.lang2 for toggling JSON and Cmd-line
                # f.write("| <span class=\"lang1\">{}</span><span class=\"lang2\">{}</span> ".format(json_option_str, cmd_option_str))
                f.write("{% row option_row %}")
                f.write(
                    f'{{% col 4 %}} <span class="lang1">{json_option_str}</span><span class="lang2">{cmd_option_str}</span> {{% endcol %}}'
                )
                # Add the description and the links
                f.write(f"{{% col 8 %}} {description} {{% endcol %}}\n")
                f.write("{% endrow %}")

    log.debug("Finished processing")

    sys.exit()
