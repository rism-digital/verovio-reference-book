---
title: "Working with CSS and SVG"

examples:
    - name: accid-001
      test-suite: accid/accid-001.mei
      xpath:
        - ".//mei:section/mei:measure[1]//mei:note[1]"
    - name: accid-003
      test-suite: accid/accid-003.mei
      xpath:
        - ".//mei:section/mei:measure[1]//mei:note[1]"
        - "[...]"
        - ".//mei:section/mei:measure[1]//mei:note[last()-1]"
---

Here is one example - show first note

{% include music-notation example="accid-001" %}

Here is another one - show first and last note

{% include music-notation example="accid-003" %}