# [experimental]
# If the config.yml generate-full-chapters flag is on and the site is served locally, this script will
# generate a PDF of the book

chromium-browser \
  --headless \
  --no-pdf-header-footer \
  --virtual-time-budget=10000 \
  --print-to-pdf="scripts/verovio-reference-book.pdf" \
http://127.0.0.1:4000/pdf/index.html 