---
title: "Layout options"

examples:
    - name: spacing-default
      url: https://kern.humdrum.org/cgi-bin/ksdata?l=users/craig/classical/bach/371chorales&file=chor010.krn&f=kern
      options:
        breaks: 'auto'
        pageHeight: 300
        adjustPageHeight: True

    - name: spacing-adjusted-01
      url: https://kern.humdrum.org/cgi-bin/ksdata?l=users/craig/classical/bach/371chorales&file=chor010.krn&f=kern
      options:
        breaks: 'auto'
        pageHeight: 300
        spacingLinear: 0.03
        spacingNonLinear: 1.0
        adjustPageHeight: True

    - name: spacing-adjusted-02
      url: https://kern.humdrum.org/cgi-bin/ksdata?l=users/craig/classical/bach/371chorales&file=chor010.krn&f=kern
      options:
        breaks: 'auto'
        pageHeight: 300
        spacingLinear: 1.0
        spacingNonLinear: 0.35
        adjustPageHeight: True

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

    - name: incipit
      test-suite: score/score-004.mei
      options:
        adjustPageHeight: True
        breaks: 'auto'
        footer: 'none'
        header: 'none'
        spacingStaff: 10
        pageHeight: 100
        pageWidth: 1500

---

### Output layout

By default, Verovio generates an output where the content is organized in pages, which size can be changed with the `--page-height` and `--page-width` options. The content of the music will laid out on one or more pages. It is possible to adjust the option `--breaks` to control how the layout is organized, namely where system and page breaks occur.

By setting the option `--breaks` to `none`, no system and page breaks will occur, and Verovio will output a single system with the entire music content. With this option, the page width will be adjusted (e.g., increased) automatically to ensure that it can contain the entire content. Be aware that this can produce very large files, regarding both the dimension of the SVG image and the actual file size.

### Content spacing

The spacing of the rhythmic values (notes and rests) is adjusted based on their durations, each value taking a bit more space than the next shorter value. This is the default output: 

{% include music-notation-only example="spacing-default" class="centered" %}

The spacing can be controlled with `--spacing-linear` and `--spacing-non-linear` options. In general, if one of them is increased, the other should be decrease not to have an exaggeratedly expanded - or the other way around. The default values are `0.25` for `--spacing-linear` and `0.6` for `--spacing-non-linear`. If you want all measures to have the same width, which means making no spacing difference according to the duration of the notes and rests, the `--spacing-non-linear` value needs to be set to `1.0`. This is what Verovio will produce together with `--spacing-linear` set to `0.03`: 

{% include music-notation-only example="spacing-adjusted-01" class="centered" %}

Alternatively, if `--spacing-non-linear` is reduced to `0.35` and `--spacing-linear` increased to `1.0`, there will be less difference in spacing between notes of different durations: 

{% include music-notation-only example="spacing-adjusted-02" class="centered" %}

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

### Generating single-system incipits

Generating single-system incipits can be done with the options `--page-height 100` and `--adjust-page-height` enabled. This way, the first page will contain only the first system of music. Its width can be set as desired with `--page-width`, here with `1500`:

{% include music-notation-only example="incipit" %}
