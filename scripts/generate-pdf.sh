# [experimental]
# If the config.yml generate-full-chapters flag is on and the site is served locally, this script will
# generate a PDF of the book

chromium-browser \
  --headless \
  --no-sandbox \
  --disable-dev-shm-usage \
  --disable-gpu \
  --no-pdf-header-footer \
  --virtual-time-budget=10000 \
  --print-to-pdf=output.pdf \
  http://localhost:4000/