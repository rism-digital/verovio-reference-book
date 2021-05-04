---
title: "SMuFL fonts"

examples:
    - name: ex-01
      test-suite: dynam/dynam-003.mei
    - name: ex-02
      test-suite: dynam/dynam-003.mei
      options:
        font: "Bravura"
    - name: ex-03
      test-suite: dynam/dynam-003.mei
      options:
        font: "Gootville"
    - name: ex-04
      test-suite: dynam/dynam-003.mei
      options:
        font: "Leland"

    - name: ex-05
      test-suite: artic/artic-001.mei
      options:
        scale: 60
    - name: ex-06
      test-suite: artic/artic-001.mei
      options:
        scale: 60
        font: "Bravura"

    - name: lyric-01
      test-suite: lyric/lyric-007.mei
      xpath:
        - ".//mei:note[1]/mei:verse"

    - name: tempo-01
      test-suite: tempo/tempo-001.mei
      xpath:
        - ".//mei:tempo"

    - name: dynam-01
      test-suite: dynam/dynam-006.mei
      xpath:
        - ".//mei:dynam"
---

Most music notation software applications use music fonts for rendering music symbols or parts of music symbols. These may include clefs, note heads, time signatures or articulation signs. However, these fonts often have incompatible code points – the internal location within the font that points to a symbol. They are most of the time developed with no common agreement on which code point represents which character. The code point for the G clef symbol in one font may be the code point used for a quarter rest in another, or may be simply undefined. Furthermore, they usually have their own metric and positioning system for specifying what the size of the glyph is and where its baseline is. Because of this, music fonts are difficult to use interchangeably. 

To address this, the Standard Music Font Layout ([SMuFL](https://www.smufl.org/)) specification has been developed to attempt to harmonize code points across music fonts by specifying code points and symbol sizes for music fonts. SMuFL gives users the ability to reference specific Unicode code points with the understanding that it would represent the same, or similar, symbol across fonts. This presents new opportunities for exploring visual representations of music within a music encoding system without necessarily tying them to a particular font. While previous music encoding systems could not reference font code points without becoming tied to that font for representation, the introduction of SMuFL to music encoding can provide a reference to a particular graphical symbol that should be used to render a given encoding.

Verovio follows the SMuFL specification, which means that it is easily possible to change the music font used in Verovio and to have a personalised output. Verovio includes the [Leipzig](https://github.com/rism-digital/leipzig) font, its own SMuFL-compliant music font. Leipzig was initially developed by Etienne Darbellay and Jean-François Marti as part of the Wolfgang music notation software. It is SMuFL compliant since version 5.0 and distributed under the [SIL Open Font License](https://github.com/rism-digital/leipzig/blob/main/LICENSE.txt).

Verovio also supports and includes the [Bravura](https://github.com/steinbergmedia/bravura) font designed by Daniel Spreadbury, the [Gootville](https://github.com/musescore/MuseScore/tree/master/fonts/gootville) and the [Leland](https://github.com/MuseScoreFonts/Leland) fonts designed by MuseScore community.

Fonts included can be selected by setting the `--font` option. For example, the Bravura font can be selected with the `--font Bravura` option in the command-line tool or by adding `{ font: "Bravura" }` in the JavaScript toolkit options.

#### Examples

{% row %}
{% col %}

*Leipzig*
{% include music-notation-only example="ex-01" %}

{% endcol %}
{% col %}

*Bravura*
{% include music-notation-only example="ex-02" %}

{% endcol %}
{% endrow %}

{% row %}
{% col %}

*Gootville*
{% include music-notation-only example="ex-03" %}

{% endcol %}
{% col %}

*Leland*
{% include music-notation-only example="ex-04" %}

{% endcol %}
{% endrow %}

*Leipzig*

{% include music-notation-only example="ex-05" %}

*Bravura*

{% include music-notation-only example="ex-06" %}

### Music symbols in text

For cases when music symbols have to displayed within text, Verovio uses the [VerovioText](https://github.com/rism-digital/verovio/blob/develop/fonts/VerovioText-1.0.ttf) font. This font is a based on Leipzig and include only a very limited set of [symbols](https://torinak.com/font/lsfont.html#https://raw.githubusercontent.com/rism-digital/verovio/develop/fonts/VerovioText-1.0.ttf?raw=true). They include:
* Note symbols for tempo indications
* Lyric elision symbols
* Figured bass symbols
* Dynamic symbols

#### Examples

{% include music-notation example="lyric-01" %}

{% include music-notation example="tempo-01" %}

Characters in tempo indications can be encoded as Unicode characters or as entities (e.g., `&#xE1D3;`). See the section on MEI in [Output formats](/toolkit-reference/output-formats.html#MEI) for more information on how to control them.

#### Dynamics

For dynamics, the font is used only in cases where text and dynamic symbols are mixed together. Verovio automatically detects dynamic symbols within text and display them appropriately. In such cases, however, the music font will always be VerovioText and the font specified with the `--font` option will not be used.

{% include music-notation example="dynam-01" %}

In some cases, it might be desirable to disable the automatic detection of dynamic symbols and the use of the music font. This can be achieved by setting explicitly a text font as illustrated with the `<rend fontfam="Times">` in the second dynamic in the example above.