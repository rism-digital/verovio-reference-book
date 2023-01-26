---
title: "Output formats"

examples:
    - name: t-01
      test-suite: tempo/tempo-001.mei
      xpath:
        - ".//mei:measure"

    - name: t-02
      test-suite: tuplet/tuplet-003.mei

    - name: pae-01
      url: https://raw.githubusercontent.com/rism-digital/verovio/develop/doc/tests/pae/6_mixed/abbreviated_writing.pae
---

### SVG

For more information about the SVG output in Verovio, see the [Internal structure](/advanced-topics/internal-structure.html) and the [Controlling the SVG output](/advanced-topics/controlling-the-svg-output.html) sections in the previous chapter.

#### Font limitation

Firefox on Linux (Ubuntu), uses "DejaVu Serif" as default font, which can cause some text layout problems when displaying the SVG files generated with Verovio.

### MEI

With its MEI output, Verovio can serve as a converter to MEI. This can be useful for converting data from another input format supported by Verovio (e.g., MusicXML, ABC) to MEI. It can also be used to upgrade files encoded in an older version of MEI to the one supported by the version of Verovio that being used. Another typical use-case where outputting MEI from Verovio can be desirable is for [transposing](/advanced-topics/transposition.html) content.

When converting other formats to MEI, it is important to keep in mind that the output produced by Verovio will only include the MEI features (elements and attributes) currently supported by the Verovio version being used. It is also important to remember that the MEI produced by Verovio is only one way to express things in MEI and that MEI will often offer other valid and recommendable ways to represent the same things. Choosing between them depends on the goal being pursued. It is possible that Verovio is the appropriate solution but not necessary.

When converting from an older version of MEI, it is important to remember that Verovio will not perform any upgrade of the data encoded in the MEI header, with the exception of the MEI version. This means that using Verovio for upgrading MEI data is probably appropriate only for encodings that feature a very basic header and is not recommended with rich ones. It is recommended to check what has changed in MEI for the header between the versions. In any case, it is strongly recommended to check the header by validating the output files produced by Verovio. Regarding the content, Verovio will upgrade only the features that used to be supported in the previous version. See the section on MEI in the [Input formats](/toolkit-reference/input-formats.html#mei) in the previous section for more detail about what is upgraded.

#### Unsupported elements and attributes

When loading MEI data into Verovio and outputting MEI, the following is to expect regarding MEI elements and attributes that are currently not supported by Verovio. Because elements that are not supported by Verovio are ignored and are not loaded into memory, they will not be preserved in the MEI output. This includes the element themselves, but also any descendant they might have. As described in the section about the [Input formats](/toolkit-reference/input-formats.html#mei), a warning will appear in the console about these. There is one exception with the `<annot>` elements for which all the content will be preserved, including MEI element descendants that are not supported elsewhere in Verovio. Regarding attributes, Verovio will preserve in the output all attributes, including the one that are not supported or that have not relevance for the rendering.

#### Analytical markup

When loading MEI data into Verovio, some analytical markup is converted into standard markup. 

The attributes that are converted are:

* `@fermata`
* `@tie`

For example:
{% row %}{% col %}
*Original data*

```xml
<note t="i" xml:id="n1"/>
<note t="t" xml:id="n2"/>
```

{% endcol %}{% col %}
*Output data*

```xml
<tie startid="#n1" endid="#n2"/>
```

{% endcol %}{% endrow %}

{% row %}{% col %}
*Original data*

```xml
<mRest fermata="above" xml:id="mr1"/>
```

{% endcol %}{% col %}
*Output data*

```xml
<fermata startid="#mr1" place="above"/>
```

{% endcol %}{% endrow %}

By default, the analytical markup is not preserve in the MEI output. It can be with the option `--preserve-analytical-markup`.  

#### Articulations

Articulations in MEI can be encoded with multiple values within a `@artic` attribute. Verovio implementation is based on single valued `@artic` attributes. When loading MEI data, multiple valued attributes are transformed into corresponding single valued ones by duplicating the `<artic>` element. This remain as such in the MEI output. For example:

{% row %}{% col %}
*Original data*

```xml
<artic artic="marc ten" place="above"/>
```

{% endcol %}{% col %}
*Output data*

```xml
<artic artic="marc" place="above"/>
<artic artic="ten" place="above"/>
```

{% endcol %}{% endrow %}

#### Page-based MEI

{% aside .warning %}
The MEI page-based model is not part of MEI. It was put in place for the development of Verovio and can still change in the future. It will be documented as input format once it is stabilized.
{% endaside %}

### MIDI

Verovio provides a basic MIDI output feature that can be used from the command-line tool or from the JavaScript toolkit. The MIDI output can be written to a file for further processing or for building application with MIDI playback, including in online environments. However, since MIDI is not supported in web-browsers in a standard way, an additional player will be required in such cases.

When a file is loaded in the toolkit only to render a MIDI file, then setting the `--breaks` option to `none` is more efficient because it will avoid the unecessary step of calculating the page layout of the document.

#### The MIDI output takes into account:

* Tempo indication (`@midi.bpm`) provided in the first `scoreDef` and in `tempo` elements.
* The sounding accidental values provided by `@accid.ges` on `notes` and `accid`.
* The sounding octave values provided by `@oct.ges` on `note`.
* Transposing instrument information provided by `@trans.semi` on `staffDef`.
* Tie elements referring to notes with `@startid` and `@endid`.

Verovio uses the [Midifile library](https://github.com/craigsapp/midifile) for generating the MIDI output.

#### Usage

With the command-line tool, for generating a MIDI file with the default options, you need to do:

```bash
verovio -t midi -o output.midi input-file.mei
```

With the JavaScript toolkit, the MIDI output is available through the `renderToMIDI()` method. This returns a base64-coded MIDI file as string, which can be passed to a player or made available for download.

### Timemap

The timemap is an array of JSON objects, with each entry having these keys:

* tstamp: this is the time in millisecond from the start of the music to the start of the current event (real time)
* qstamp: the time in quarter notes from the start of the music to the start of the current event entry (score time)
* tempo: when the tempo changes the new tempo will be given for the current event. Also the tempo changes are only allowed to occur at the starts of measures in the current code for creating MIDI files, and this is the same limitation for the timemap file. The tempo and qstamp values can be used to re-calculate a new set of tstamp values if the tempo changes.
* on: This is an array of note ids that start at the current event time. This list will not be given if there are no note ons at the current event.
* off: This is an array of note ids that end at the current event time. This list will not be given if there are no note offs at the current event.

When a file is loaded in the toolkit only to render the timemap file, then setting the `--breaks` option to `none` is more efficient because it will avoid the unecessary step of calculating the page layout of the document.

#### Examples

{% include music-notation example="t-01" %}

```json
[
  {
    "tstamp": 0,
    "qstamp": 0,
    "tempo": 70,
    "on": [
      "m0_s2_e1"
    ]
  },
  {
    "tstamp": 428.571429,
    "qstamp": 0.5,
    "on": [
      "m0_s2_e2"
    ],
    "off": [
      "m0_s2_e1"
    ]
  },
  {
    "tstamp": 857.142857,
    "qstamp": 1,
    "on": [
      "note-0000001938389898"
    ],
    "off": [
      "m0_s2_e2"
    ]
  },
  {
    "tstamp": 2142.857143,
    "qstamp": 2.5,
    "on": [
      "note-0000001651747389"
    ],
    "off": [
      "note-0000001938389898"
    ]
  },
  {
    "tstamp": 2571.428571,
    "qstamp": 3,
    "on": [
      "note-0000001917733971"
    ],
    "off": [
      "note-0000001651747389"
    ]
  },
  {
    "tstamp": 3428.571429,
    "qstamp": 4,
    "on": [
      "m1_s2_e4"
    ],
    "off": [
      "note-0000001917733971"
    ]
  },
  {
    "tstamp": 3857.142857,
    "qstamp": 4.5,
    "on": [
      "m1_s2_e5"
    ],
    "off": [
      "m1_s2_e4"
    ]
  },
  {
    "tstamp": 4285.714286,
    "qstamp": 5,
    "off": [
      "m1_s2_e5"
    ]
  }
]
```

{% include music-notation-only example="t-02" %}

```json
[
  {
    "tstamp": 0,
    "qstamp": 0,
    "tempo": 120,
    "on": [
      "note-0000002010789077"
    ]
  },
  {
    "tstamp": 666.666667,
    "qstamp": 1.333333,
    "on": [
      "note-0000001595005340"
    ],
    "off": [
      "note-0000002010789077"
    ]
  },
  {
    "tstamp": 1333.333333,
    "qstamp": 2.666667,
    "on": [
      "note-0000000084354770"
    ],
    "off": [
      "note-0000001595005340"
    ]
  },
  {
    "tstamp": 2000,
    "qstamp": 4,
    "off": [
      "note-0000000084354770"
    ]
  }
]
```

### Plaine and Easie

The output format for the Plaine and Easie output in Verovio uses the same file structure with `key:value` lines as described in the section in the [Input formats](/toolkit-reference/input-formats.html#plaine-and-easie). See also there for the features supported.

Note that:

* duration is given explicitly for every note
* no abbreviated writing is used in the Plaine and Easie output

For example, let's consider the following example passed as input to Verovio: 

{% assign pae = page.examples | where: "name", "pae-01" | first %}

```pae
{% remote_include {{ pae.url }} %}
```

{% include music-notation-only example="pae-01" %}

Verovio will produce the following Plaine and Easie output:

```pae
@keysig:b
@timesig:3/4
@clef:G-2
@data:{6'G6G6C6C}{6G6G6C6C}{6G6C6G6C}/{6G6G6C6C}{6G6G6C6C}{6G6C6G6C}/{6G6G6C6C}{6G6G6C6C}{6G6C6G6C}/
```

### Humdrum

The Humdrum output format for Verovio is available only from MusicXML input and only if the Humdrum importer is used when loading the data into Verovio. See [this section](/toolkit-reference/input-formats.html#musicxml) for more information about the MusicXML import via Humdrum.

With this in hand, you can convert MusicXML to Humdrum from the command-line with:

```bash
verovio -f musicxml-hum -t hum file.xml
```

If the MusicXML importer via Humdrum is the default, you can simply do:

```bash
verovio -t hum file.xml
```
