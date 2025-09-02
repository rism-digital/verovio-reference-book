#!/usr/bin/env bash

jekyll build --baseurl=""

python3 scripts/generate-examples.py ./scripts/examples.yaml
python3 scripts/generate-options.py
python3 scripts/generate-methods.py release
python3 scripts/generate-mei-support.py release


