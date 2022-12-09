---
title: "Layout options"

examples:
    - name: default
      test-suite: score/score-014.mei
      options:
        adjustPageHeight: False
        breaks: 'auto'
        footer: 'auto'
        header: 'auto'
        scale: 20
        spacingStaff: 10
        spacingSystem: 10

    - name: justification-default
      test-suite: score/score-014.mei
      options:
        adjustPageHeight: False
        breaks: 'auto'
        footer: 'auto'
        header: 'auto'
        justifyVertically: True
        scale: 20
        spacingStaff: 10
        spacingSystem: 10

    - name: justification-brace-group-0
      test-suite: score/score-014.mei
      options:
        adjustPageHeight: False
        breaks: 'auto'
        footer: 'auto'
        header: 'auto'
        justificationBraceGroup: 0.0
        justifyVertically: True
        scale: 20
        spacingStaff: 10
        spacingSystem: 10

    - name: justification-bracket-group-0-5
      test-suite: score/score-014.mei
      options:
        adjustPageHeight: False
        breaks: 'auto'
        footer: 'auto'
        header: 'auto'
        justificationBraceGroup: 0.0
        justificationBracketGroup: 0.2
        justifyVertically: True
        scale: 20
        spacingStaff: 10
        spacingSystem: 10

---

### Staff and system spacing

Staff and system spacing in Verovio is controlled by two options, namely `--spacing-staff` and `--spacing-system`. Their value is given in MEI units and the default value is `12` units. Since a five line staff is 8 units, it means the default spacing between two staves will be one and a half staff height, and an additional equivalent system spacing between two systems.

Verovio adds half a staff space above the first staff of a system and below the last one. This is the illustrated below with the default spacing options.

![spacing 01](/images/advanced-topics/layout-options/spacing-01.png){:.img-responsive .example-80}

When removing the top and bottom page margins (`--page-margin-top 0` and  `--page-margin-bottom 0`), there will be only the half staff space above and below.

![spacing 02](/images/advanced-topics/layout-options/spacing-02.png){:.img-responsive .example-80}

To remove the spacing above and below the staff completely, the staff space has to be removed with `--spacing-staff 0`.

![spacing 03](/images/advanced-topics/layout-options/spacing-03.png){:.img-responsive .example-80}

The half staff space above and below the staff means that having music content above or below the staff line does not change vertical positioning when the content fits within that space. Because the default value for `--spacing-staff` is `12` MEI units, it means that up to 3 staff spaces (e.g., up to a D6 with a G-2 clef) will fit in that space.

![spacing 04](/images/advanced-topics/layout-options/spacing-04.png){:.img-responsive .example-80}

When the content takes more space than half a staff spacing, then space is added. On a page, it means that the position of the staff will be lowered accordingly.

![spacing 05](/images/advanced-topics/layout-options/spacing-05.png){:.img-responsive .example-80}

When there is a header or a footer, additional spacing is added between between them and the music content. By default, the spacing is `2.0` MEI units. The value can be adjusted with the options  `--bottom-margin-pg-header` or  `--top-margin-pg-footer`.

![spacing 06](/images/advanced-topics/layout-options/spacing-06.png){:.img-responsive .example-80}

### Vertical justification

When producing page-like layouts, it is often desirable to justify the content vertically in order to have the staves distributed on the page in a balance way.

By default, no vertical justification is applied, and rendering a page will place all systems at the top of the page. The spacing of the staff and the system will be simply determined by the `--spacing-staff` and `--spacing-system` values. 

{% include music-notation-only example="default" class="centered" %}

To have the content justified, the option `--justify-vertically` has to be enabled.

{% include music-notation-only example="justification-default" class="centered" %}

This option applies justification over all staff spaces in the score in a linear way. Verovio allows for a more fine-tuned justification with different spacing parameters for staves grouped by a brace or a bracket. The options to adjust are `--justification-brace-group`, `--justification-bracket-group`, `--justification-staff` and `--justification-system`. Each of these take a parameter from `0.0` to `10.0` acting as a factor on the justification applied. The default value is `1.0` for all of them.

Setting one of these options to `0.0` will result in no justification space added between the corresponding staves. For example, the same example as above rendered with `--justification-brace-group 0.0` will have a layout where the staff spacing between the staves in the brace groups remains unchanged.

{% include music-notation-only example="justification-brace-group-0" class="centered" %}

Adding `--justification-bracket-group 0.2` with reduce the space between the staves in the bracket group, even though still changing it be cause the value is not `0.0`. The spacing between the other staves and the systems is consequently increased.

{% include music-notation-only example="justification-bracket-group-0-5" class="centered" %}