---
title: "Tutorial 2: Interactive notation"

examples:
    - name: accid-001
      url: https://raw.githubusercontent.com/rism-digital/verovio.org/gh-pages/_tests/accid/accid-001.mei
      xpath:
        - ".//mei:section/mei:measure[1]"
        - "[...]"
        - ".//mei:section/mei:measure[3]"
    - name: accid-002
      url: https://raw.githubusercontent.com/rism-digital/verovio.org/gh-pages/_tests/accid/accid-002.mei
      xpath:
        - ".//mei:section/mei:measure[1]"
        - ".//mei:section/mei:measure[2]"
---

Here is one example - we show measure 1 and 3 with a separator

{% include music-notation example="accid-001" %}

Here is another one - we show measure 1 and 2 without separator

{% include music-notation example="accid-002" %}