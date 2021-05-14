
jekyll build --baseurl=""

python3.9 scripts/generate-examples.py ./scripts/examples.yaml
python3.9 scripts/generate-options.py   
python3.9 scripts/generate-methods.py release
python3.9 scripts/generate-mei-support.py release


