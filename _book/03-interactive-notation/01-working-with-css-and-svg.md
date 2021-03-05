---
title: "Working with CSS and SVG"

examples:
    - name: accid-001
      url: https://raw.githubusercontent.com/rism-digital/verovio.org/gh-pages/_tests/accid/accid-001.mei
      xpath:
        - ".//mei:section/mei:measure[1]//mei:note[1]"
    - name: accid-003
      url: https://raw.githubusercontent.com/rism-digital/verovio.org/gh-pages/_tests/accid/accid-003.mei
      xpath:
        - ".//mei:section/mei:measure[1]//mei:note[1]"
        - "[...]"
        - ".//mei:section/mei:measure[1]//mei:note[last()-1]"
---

Here is one example - show first note

{% include mei example="accid-001" %}

Here is another one - show first and last note

{% include mei example="accid-003" %}