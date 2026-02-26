---
title: "SMuFL fonts"

examples:
    - name: ex-01
      test-suite: dynam/dynam-003.mei
      options:
        xmlIdSeed: 1
    - name: ex-02
      test-suite: dynam/dynam-003.mei
      options:
        xmlIdSeed: 1
        font: "Bravura"
    - name: ex-03
      test-suite: dynam/dynam-003.mei
      options:
        xmlIdSeed: 1
        font: "Gootville"
    - name: ex-04
      test-suite: dynam/dynam-003.mei
      options:
        xmlIdSeed: 1
        font: "Leland"

    - name: ex-05
      test-suite: artic/artic-001.mei
      options:
        xmlIdSeed: 1
        scale: 60
    - name: ex-06
      test-suite: artic/artic-001.mei
      options:
        xmlIdSeed: 1
        scale: 60
        font: "Bravura"

    - name: lyric-01
      test-suite: lyric/lyric-007.mei
      options:
        xmlIdSeed: 1  
      xpath:
        - ".//mei:note[1]/mei:verse"

    - name: tempo-01
      options:
        xmlIdSeed: 1
      test-suite: tempo/tempo-001.mei
      xpath:
        - ".//mei:tempo"

    - name: dynam-01
      options:
        xmlIdSeed: 1
      test-suite: dynam/dynam-006.mei
      xpath:
        - ".//mei:dynam"

    - name: turn-01
      options:
        xmlIdSeed: 1
      test-suite: turn/turn-003.mei
      xpath:
        - ".//mei:turn"

    - name: keySig-01
      options:
        xmlIdSeed: 1
      test-suite: keysig/keysig-005.mei
      xpath:
        - ".//mei:keySig"

    - name: custom-01
      options:
        xmlIdSeed: 1
        fontAddCustom:
          - 'scripts/GoldenAge.zip'
      test-suite: font/font-002.mei
      xpath:
        - ".//mei:clef[@fontname='Petaluma']"
---

Most music notation software applications use music fonts for rendering music symbols or parts of music symbols. These may include clefs, note heads, time signatures or articulation signs. However, these fonts often have incompatible code points – the internal location within the font that points to a symbol. They are most of the time developed with no common agreement on which code point represents which character. The code point for the G clef symbol in one font may be the code point used for a quarter rest in another, or may be simply undefined. Furthermore, they usually have their own metric and positioning system for specifying what the size of the glyph is and where its baseline is. Because of this, music fonts are difficult to use interchangeably.

To address this, the Standard Music Font Layout ([SMuFL](https://www.smufl.org/)) specification has been developed to attempt to harmonize code points across music fonts by specifying code points and symbol sizes for music fonts. SMuFL gives users the ability to reference specific Unicode code points with the understanding that it would represent the same, or similar, symbol across fonts. This presents new opportunities for exploring visual representations of music within a music encoding system without necessarily tying them to a particular font. While previous music encoding systems could not reference font code points without becoming tied to that font for representation, the introduction of SMuFL to music encoding can provide a reference to a particular graphical symbol that should be used to render a given encoding.

Verovio follows the SMuFL specification. It means that it is possible to easily change the music font used in Verovio for personalised output. Verovio includes the [Leipzig](https://github.com/rism-digital/leipzig) font, its own SMuFL-compliant music font. Leipzig was initially developed by Etienne Darbellay and Jean-François Marti as part of the Wolfgang music notation software. It is SMuFL compliant since version 5.0 and distributed under the [SIL Open Font License](https://github.com/rism-digital/leipzig/blob/main/LICENSE.txt).

Verovio also supports and includes the [Bravura](https://github.com/steinbergmedia/bravura) font designed by Daniel Spreadbury, and the [Gootville](https://github.com/musescore/MuseScore/tree/master/fonts/gootville) and [Leland](https://github.com/MuseScoreFonts/Leland) fonts designed by the MuseScore community.

Fonts included can be selected by setting the `--font` option. For example, the Bravura font can be selected with the `--font Bravura` option on the command-line tool or by adding `{ font: "Bravura" }` in the JavaScript toolkit options.

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

For cases when music symbols are displayed within text, Verovio uses a text [WOFF2](https://www.w3.org/TR/WOFF2/) version of the selected music font. The font is included in the SVG as CSS.

The `--smufl-text-font` allows to change how the font is included. By default, it is simply embedded as a base64 string. This means that the SVG is fully self-contained and does not require network access for the font glyphs to be displayed. The include of the font can also be ignored with `none`, which can be useful when the font is included seperately in the environment.

With `linked`, the text font will be included in the SVG but with the following CSS import:
```xml
<style type="text/css">
    @import url("https://www.verovio.org/javascript/3.13.0/data/Leipzig.css");
</style>
```
The version of the font path is based on the Verovio version release number, or is `develop` for the develop version of the toolkit.

When a music glyph is displayed within text and the music font selected is not Leipzig or Bravura, Verovio will also check if the music glyph exists in the selected music font. If not, it will fallback to the Leipzig font. If other text elements include music glyphs that do exist in the selected font, then both Leipzig and the selected font will be included. In other words, the fallback to Leipzig will be enabled only for the text elements displaying a missing music glyphs but not for the others.

#### Examples

{% include music-notation example="lyric-01" %}

{% include music-notation example="tempo-01" %}

Characters in tempo indications can be encoded as Unicode characters or as entities (e.g., `&#xE1D3;`). See the section on MEI in [Output formats](/toolkit-reference/output-formats.html#MEI) for more information on how to control them.

#### Dynamics

For dynamics, Verovio automatically detects dynamic symbols within text and displays them appropriately. In some cases, it might be desirable to disable the automatic detection of dynamic symbols and the use of the music font. This can be achieved by setting a text font explicitly, as illustrated with the `<rend fontfam="Times">` in the second dynamic in this example:

{% include music-notation example="dynam-01" %}

### Use alternate SMuFL glyphs

For some elements, Verovio support the use of alternate SMuFL glyphs through the `@glyph.auth` and `@glyph.name` or `@glyph.num` attributes. The `@glyph.auth` is expected to the value `smufl`. When both `@glyph.auth` and `@glyph.num` are provided, then the priority is given to `@glyph.num`.

{% include music-notation example="turn-01" %}

{% include music-notation example="keySig-01" %}

### Custom fonts

#### Load all fonts

The `--font-load-all` boolean option makes Verovio loads all the music fonts available in the resource directory. That way, a specific font other than the default font `Leipzig` or the font set with the `--font` option can be used by specifying a `@fontname` value. At this stage, this is supporting only on `clef` and `meterSig`.

#### Set a specific fall back

Only Bravura and Leipzig have a complete coverage of the glyphs used in Verovio. The `--font-fallback` parameter option allows to choose between `Leipzig` (default) or `Bravura` as the fallback font to be used when the font chosen is missing a glyph.

#### Loading custom fonts

The `--font-add-custom` parameter option allows to load and use an external font not available in the resource directory. The option is repeatable, which means that more than one external font can be loaded. For bindings that use JSON options, the value(s) must be passed in an array.

The custom font must be archived in a ZIP file containing the files produced by the font script Verovio provides in `./fonts` for extracting relevant information from an SVG font file and the corresponding SMuFL metadata file. See the [README](https://github.com/rism-digital/verovio/tree/develop/fonts#readme) for more information about the script and how to run it. The files needed are:
* The XML file with bounding boxes of the included glyphs.
* The XML snippets for each glyph
* The CSS file of the font for text

The ZIP filename must correspond to the name of the font. For the JavaScript binding, the ZIP file must be encoded in Base64 and passed as a URL or as a based64 string.

Example rendered with `--font-fallback Bravura` and `--font-add-custom GoldenAge.zip` (available [here](https://github.com/rism-digital/verovio.org/tree/gh-pages/examples/fonts/custom)) and all fonts loaded with `--font-load-all`. The elements in olive have a `@fontame="Petaluma"`. The clef in orange is a `Bravura` fallback.

{% include music-notation example="custom-01" %}
