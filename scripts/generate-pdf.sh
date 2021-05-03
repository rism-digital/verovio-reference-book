# [experimental]
# If the config.yml generate-full-chapters flag is on and the site is served locally, this script will
# generate a PDF of the book

wkhtmltopdf -s A4 --javascript-delay 500 --no-background  --print-media-type --outline --outline-depth 3  \
-B 20 -R 20 -L 20 -T 20 \
--minimum-font-size 19  \
--footer-center "– [page] –"  --footer-font-size 8 \
http://127.0.0.1:4000/pdf/index.html \
toc --xsl-style-sheet ./scripts/toc.xsl \
scripts/verovio-reference-book.pdf

