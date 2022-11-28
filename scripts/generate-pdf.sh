# [experimental]
# If the config.yml generate-full-chapters flag is on and the site is served locally, this script will
# generate a PDF of the book

wkhtmltopdf -s A4 --javascript-delay 500 --page-size A4 --no-background  --print-media-type --outline --outline-depth 3  \
-B 15 -R 15 -L 15 -T 15 \
--minimum-font-size 19  \
--footer-center "– [page] –"  --footer-font-size 8 \
--enable-local-file-access \
http://127.0.0.1:4000/pdf/index.html \
toc --xsl-style-sheet ./scripts/toc.xsl \
scripts/verovio-reference-book.pdf

