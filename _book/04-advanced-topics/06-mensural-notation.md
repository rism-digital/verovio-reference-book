---
title: "Mensural notation"

examples:
    - name: alignment-01
      test-suite: mensural/mensural-024.mei
      xpath:
        - ".//mei:measure[1]"
      options:
        spacingStaff: "8"
    - name: alignment-02
      test-suite: mensural/mensural-025.mei
      xpath:
        - ".//mei:measure[1]"
      options:
        spacingStaff: "8"
---

[in preparation]

### Duration alignment

### Layout

### Ligatures

### Alignment with CMN

Mensural notation in *tempus imperfectum* and *prolatio minor* aligns automatically (i.e., aligning whole notes with semibrevis and so on for durations up and down). Of course, this requires the mensural notation to be put in measures, and Verovio only takes care about the alignment of the duration themselves.

{% include music-notation example="alignment-01" %}

With *tempus perfectum* and or *prolatio maior*, then duration shorter than a breve in CMN need to be put into tuplets with the appropriate adjustments. See here `num="3"` and `numbase="2"` for the whole notes and `num="9"` and `numbase="4"` for the half notes and shorter.

{% include music-notation example="alignment-02" %}
