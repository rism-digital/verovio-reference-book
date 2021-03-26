# [experimental]
# If the config.yml generate-full-chapters flag is on and the site is served locally, this script will
# generate a PDF of the book

wkhtmltopdf -g -s A4 --javascript-delay 500 --no-background  --print-media-type --outline --outline-depth 3  \
-B 20 -R 20 -L 20 -T 20 \
--minimum-font-size 18  \
http://127.0.0.1:4000/full-chapters/01-introduction.html \
http://127.0.0.1:4000/full-chapters/02-first-steps.html \
http://127.0.0.1:4000/full-chapters/03-interactive-notation.html \
http://127.0.0.1:4000/full-chapters/04-advanced-topics.html \
http://127.0.0.1:4000/full-chapters/05-toolkit-reference.html \
http://127.0.0.1:4000/full-chapters/06-installing-or-building-from-sources.html \
http://127.0.0.1:4000/full-chapters/07-contributing.html \
toc --xsl-style-sheet ./scripts/toc.xsl \
scripts/verovio-reference-book.pdf

