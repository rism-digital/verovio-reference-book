import argparse
import json
import os
import sys
import pprint
from typing import Dict, List
import logging

import requests
import verovio
import yaml
from lxml import etree


MEI_NS: Dict = {'mei': 'http://www.music-encoding.org/ns/mei'}

VRV_OPTIONS: Dict = {
    'adjustPageHeight': True,
    'breaks': 'none',
    'pageHeight': 2970,
    'pageWidth': 2100,
    'header': 'none',
    'footer': 'none',
    'scale': 50,
    'spacingStaff': 4
}


if __name__ == "__main__":
    description = """
        Fetches and renders SVG from a given set of examples. Will generate any new examples found; to 
        re-generate all examples use the '--clean' option.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--clean", action="store_true", help="Re-generate all examples.")
    verbose_group = parser.add_mutually_exclusive_group()
    verbose_group.add_argument("--verbose", "-v", action="store_true")
    verbose_group.add_argument("--debug", "-d", action="store_true")

    parser.add_argument("examples", help="Path to examples.yaml file")

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
    defaultOptions: Dict = json.loads(tk.getOptions(True))
    # Overwrite the default options with our locally-defined options
    defaultOptions.update(VRV_OPTIONS)

    # Will remove extraneous whitespace
    et_parser = etree.XMLParser(remove_blank_text=True)

    with open(args.examples, 'r') as file:
        examples: Dict = yaml.full_load(file)

        for example in examples:
            options: Dict = defaultOptions.copy()

            svg_file = os.path.join("images", example['svg-example-file'])
            svg_dir = os.path.dirname(svg_file)

            mei_snippet_file = os.path.join("_includes", example['mei-example-file'])
            mei_snippet_directory = os.path.dirname(mei_snippet_file)

            if os.path.exists(svg_file) and os.path.exists(mei_snippet_file) and not args.clean:
                log.info("This example already exists, and we're not running in cleaning mode. Skipping.")
                continue

            # Download the MEI file from the given url
            test_file = example['test-suite']
            url = f"https://raw.githubusercontent.com/rism-digital/verovio.org/gh-pages/_tests/{test_file}"

            log.debug("Downloading %s", url)
            mei_example_req = requests.get(url)

            if 200 <= mei_example_req.status_code < 400:
                log.info("%s successfully downloaded", url)
            else:
                log.error("Problem downloading %s. Skipping this example", url)
                continue

            mei_example = mei_example_req.text

            # parse the MEI file to XML
            log.debug("Parsing downloaded text to XML")
            tree = etree.fromstring(bytes(mei_example.encode("utf-8")), parser=et_parser)
            # try to get the extMeta tag and load the options if existing
            meta = tree.findtext(".//mei:meiHead/mei:extMeta", namespaces=MEI_NS)

            if meta:
                # Overwrite any pre-defined options with the options from the MEI file.
                log.info("Found some locally-defined meta options: %s", meta)
                metaOptions = json.loads(meta)
                options.update(metaOptions)

            # If the example has additional options, load them.
            example_options: str = example.get("options", "{}")
            options.update(json.loads(example_options))

            # Always returns a list, even if it's empty; won't raise an error
            # if 'xpath' doesn't exist.
            queries: List = example.get("xpath", [])
            mei_snippet: str = ""
            
            for query in queries:
                if query == "[...]":
                    log.debug("Found a comment")
                    mei_snippet += "<!-- ... -->\n"
                    continue

                results = tree.findall(query, namespaces=MEI_NS)

                for result in results:
                    mei_snippet += etree.tostring(result, pretty_print=True, encoding="unicode")

            # Since we're not really working with XML (no single root) we'll just use string regexes
            # to strip out the xmlns declaration.
            mei_snippet = mei_snippet.replace(" xmlns=\"http://www.music-encoding.org/ns/mei\"", "")

            if not os.path.exists(mei_snippet_directory):
                log.debug("Making MEI Snippet directory %s", mei_snippet_directory)
                os.mkdir(mei_snippet_directory)

            with open(mei_snippet_file, 'w') as f:
                f.write(mei_snippet)

            log.debug("Running Verovio with the following options: %s", pprint.pformat(options))
            tk.setOptions(json.dumps(options))
            tk.loadData(mei_example)

            svg: str = tk.renderToSVG(1)

            # create the output directory if necessary
            if not os.path.exists(svg_dir):
                log.debug("Making SVG output directory %s", svg_dir)
                os.mkdir(svg_dir)

            with open(svg_file, 'w') as f:
                f.write(svg)

            log.debug("Finished processing %s", test_file)

    sys.exit()
