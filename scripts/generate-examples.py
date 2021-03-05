# This script it expected to be run from ./bindings/python
import argparse
import json
import os
import re
import sys
import wget
import xml.etree.ElementTree as ET
import yaml

from io import StringIO 

# Add path for toolkit built in-place
sys.path.append('.')
import verovio

ns = {'mei': 'http://www.music-encoding.org/ns/mei'}

testOptions = {
    'adjustPageHeight': True,
    'breaks': 'none',
    'pageHeight': 2970,
    'pageWidth': 2100,
    'header': 'none',
    'footer': 'none',
    'scale': 50,
    'spacingStaff': 4,
    'svgViewBox': False
}

def indent(elem, level=0):
  i = "\n" + level*"  "
  if len(elem):
    if not elem.text or not elem.text.strip():
      elem.text = i + "  "
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
    for elem in elem:
      indent(elem, level+1)
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
  else:
    if level and (not elem.tail or not elem.tail.strip()):
      elem.tail = i

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #parser.add_option("--clean", nargs='?', default=False)
    args = parser.parse_args()

    tk = verovio.toolkit()
    # version of the toolkit
    print(tk.getVersion())

    # keep all the options to be able to reset them for each test
    defaultOptions = json.loads(tk.getOptions(True))

    with open(r'scripts/examples.yaml') as file:
        examples = yaml.load(file, Loader=yaml.FullLoader)
        for example in examples:
            #if 'svg-example-exists' in example and example['svg-example-exists']:
                #continue
            #if 'mei-example-exists' in example and example['mei-example-exists']:
                #continue

            meiFile = wget.download(example['url'], out="./scripts/tmp")
            print("\nFile successfully downloaded to .{}".format(meiFile))

            options = {**defaultOptions, **testOptions}
            # parse the MEI file
            
            tree = ET.parse(meiFile)

            root = tree.getroot()
            # try to get the extMeta tag and load the options if existing
            meta = root.findtext(".//mei:meiHead/mei:extMeta", namespaces=ns)
            if (meta != None and meta != ''):
                print(meta)
                metaOptions = json.loads(meta)
                options = {**options, **metaOptions}

            f = root.findall(".//mei:measure", namespaces=ns)
            ET.register_namespace('', 'http://www.music-encoding.org/ns/mei')

            meiSnippetStr = ""
            for i in f:
                indent(i)
                xmlStr = ET.tostring(i, method='xml').decode()
                if xmlStr:
                    #xmlStr = re.sub(xmlStr, ' xmlns="http:\/\/www.music-encoding.org\/ns\/mei"', '')
                    meiSnippetStr += xmlStr

            meiSnippetFile = os.path.join("_includes", example['mei-example-file'])
            meiSnippetDir = os.path.dirname(meiSnippetFile)
            if not(os.path.isdir(meiSnippetDir)):
                print(meiSnippetDir)
                os.mkdir(os.path.join(meiSnippetDir))

            with open(meiSnippetFile, 'w') as f:
                f.write(meiSnippetStr)

            tk.setOptions(json.dumps(options))
            tk.loadFile(meiFile)

            svgString = tk.renderToSVG(1)

            # create the output directory if necessary
            svgFile = os.path.join("images", example['svg-example-file'])
            svgDir = os.path.dirname(svgFile)
            if not(os.path.isdir(svgDir)):
                print(svgDir)
                os.mkdir(os.path.join(svgDir))

            ET.ElementTree(ET.fromstring(svgString)).write(svgFile)

            os.remove(meiFile) 
