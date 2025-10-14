---
title: "Repetition expansion"

examples:
  - name: expansion-001
    test-suite: expansion/expansion-001.mei
    xpath:
  #      - ".//mei:score/mei:section[not(*)]"
  #       - ".//score/section/expansion"
  #      - ".//mei:section[not(.//*[not(self::expansion or self::section or self::ending or self::rdg or self::lem)])]"

  - name: expansion-001-default
    test-suite: expansion/expansion-001.mei
    options:
      expand: "expansion-default"

  - name: expansion-001-minimal
    test-suite: expansion/expansion-001.mei
    options:
      expand: "expansion-minimal"

  - name: expansion-001-maximal
    test-suite: expansion/expansion-001.mei
    options:
      expand: "expansion-maximal"

  - name: expansion-002
    test-suite: expansion/expansion-002.mei

  - name: expansion-002-default
    test-suite: expansion/expansion-002.mei
    options:
      expand: "default"
---

Scores may contain repetitions, endings, or directives to repeat a section from a certain location in the score, such as dal segno or similar. Such instructions allow performers to make informed decisions about the repetition structure during performance. The MEI schema provides the [`<expansion>` element](https://music-encoding.org/guidelines/v5/elements/expansion) to encode specific versions of a scores' repetition structure. Verovio supports this MEI element with the `--expand` toolkit option, which generates an unfolded version of the score in the requested output format. This realises the encoded repetitions by copying and/or deleting score elements to match the specified repetition structure.

The `expansion` element is expected to be the first element in a `section` or `ending` and must contain descendant `expansion`, `ending`, or `rdg` elements (see [guidelines for section](https://music-encoding.org/guidelines/v5/elements/section)). Its `@plist` attribute may point to its descendant `section`, `ending`, `rdg`, or `lem` elements to indicate a particular expanded version of that excerpt of the score. See the [MEI guidelines for a simple expansion example](https://music-encoding.org/guidelines/v5/content/shared.html#sharedMdivContent).

### Minuet example

A typical MEI example (from the [Verovio test suite](https://www.verovio.org/test-suite.xhtml?cat=expansion#example-expansion-001)) is given below containing a straight-forward repetition structure in which the Minuet and the Trio are each repeated once with different endings. As indicated by "Menuett da capo", the performer is requested to repeat the Minuet after the Trio, but then without repetition, going directly to `A2` to terminate the performance.

{% include music-notation-only example="expansion-001" %}

```xml
<section xml:id="all">
  <expansion xml:id="expansion-default" plist="#A #A1 #A #A2 #B #B1 #B #B2 #A #A2"/>
  <expansion xml:id="expansion-minimal" plist="#A #A2 #B #B2 #A #A2"/>
  <expansion xml:id="expansion-maximal" plist="#A #A1 #A #A2 #B #B1 #B #B2 #A #A1 #A #A2"/>
  <section xml:id="A"/>
  <ending xml:id="A1" n="1."/>
  <ending xml:id="A2" n="2."/>
  <section xml:id="B"/>
  <ending xml:id="B1" n="1."/>
  <ending xml:id="B2" n="2."/>
</section>
```

An expansion is engraved by Verovio by passing the `xml:id` of its expansion element as an option to the toolkit, e.g. `--expand expansion-default` for the command-line or `expand: 'expansion-default'` for Javascript/Python options, which looks like this:

{% include music-notation-only example="expansion-001-default" %}

This example also encodes a "minimal" expansion that omits sections A1 and B1, but still repeats the Minuet:

```xml
<expansion xml:id="expansion-minimal" plist="#A #A2 #B #B2 #A #A2"/>
```

{% include music-notation-only example="expansion-001-minimal" %}

This example also encodes a "maximal" expansion that realises all repeats, including in the repeated Minuet:

```xml
<expansion xml:id="expansion-maximal" plist="#A #A1 #A #A2 #B #B1 #B #B2 #A #A1 #A #A2"/>
```

{% include music-notation-only example="expansion-001-maximal" %}

You may also encode the expansion structure of the above Minuet example in a hierarchical way (see [Verovio test suite](https://www.verovio.org/test-suite.xhtml?cat=expansion#example-expansion-001-hierarchical)), with sections for Minuet and Trio, each having their own expansion elements embedded:

```xml
<section xml:id="all">
  <expansion xml:id="exp-default" plist="#exp-menuett-default #exp-trio-default #exp-menuett-minimal"/>
  <expansion xml:id="exp-minimal" plist="#exp-menuett-minimal #exp-trio-minimal #exp-menuett-minimal"/>
  <expansion xml:id="exp-maximal" plist="#exp-menuett-default #exp-trio-default #exp-menuett-default"/>
  <section xml:id="Menuett">
    <expansion xml:id="exp-menuett-default" plist="#A #A1 #A #A2"/>
    <expansion xml:id="exp-menuett-minimal" plist="#A #A2"/>
    <section xml:id="A"/>
    <ending xml:id="A1" n="1."/>
    <ending xml:id="A2" n="2."/>
  </section>
  <section xml:id="Trio">
    <expansion xml:id="exp-trio-default" plist="#B #B1 #B #B2"/>
    <expansion xml:id="exp-trio-minimal" plist="#B #B2"/>
    <section xml:id="B"/>
    <ending xml:id="B1" n="1."/>
    <ending xml:id="B2" n="2."/>
  </section>
</section>
```

#### Exporting an expansionmap

For sections that get cloned, Verovio generates predictable `xml:id`s for all containing elements, appending a `-rendX` to the existing `xml:id`, where `X` is a number starting from 2 for the first repetition of a given element. Thus, `xml:id="A-rend3"` would refer to the third occurence (or the second repetition) of section `"A"`. To track the relationship between the original score and a unfolded repeats, Verovio provides access to the expansionmap. This JSON object contains key-value pairs with unique keys for each `xml:id` in the encoding (both the original and the unfolded elements) and values containing a list of related (original and unfolded) elements, e.g. `["A", "A-rend2", "A-rend3"]`.

For more information on the expansionmap, see [Output formats](/toolkit-reference/output-formats.html#expansionmap).

### Example with re-ordered sections

The following example has a slightly more complex default expansion structure that requires section A to be rendered three times, each time choosing a different ending.

{% include music-notation-only example="expansion-002" %}

The following expansion represents a sensible default:

```xml
<expansion xml:id="default" plist="#Upbeat #A #A1 #A #A2 #B #A #A-Fine"/>
````

Verovio accommodates this complexity automatically by re-ordering the section structure so that it looks like this:

{% include music-notation-only example="expansion-002-default" %}

### Hierarchical expansion structure

The elements referred to in the `expansion@plist` may themselves be expansion elements situated in descendent section elements. A complex but typical example is the Waltz structure of [An der schönen blauen Donau by Johann Strauss II](https://mei-friend.mdw.ac.at/?file=https://raw.githubusercontent.com/Signature-Sound-Vienna/Johann-Strauss-Sohn_Op314_Donauwalzer_Breitkopf/main/Donauwalzer-Breitkopf.mei&scale=33&breaks=line&select=Shorter_Version_Boskovsky&page=1&speed=true&notationOrientation=left&notationProportion=0.44){:target="\_blank"}. (To open a public-domain encoding in mei-friend, please click [here](https://mei-friend.mdw.ac.at/?file=https://raw.githubusercontent.com/Signature-Sound-Vienna/Johann-Strauss-Sohn_Op314_Donauwalzer_Breitkopf/main/Donauwalzer-Breitkopf.mei&scale=33&breaks=line&select=Shorter_Version_Boskovsky&page=1&speed=true&notationOrientation=left&notationProportion=0.44){:target="\_blank"}.)

![Donauwalzer-Sections](/images/advanced-topics/expansions/BlueDanube-section-structure.png){:.img-responsive .example-80}

In turn, each waltz contains a set of expansion elements, each defining a repetition structure performed within the history of the Vienna New Year's Concert series. The higher-level expansion element then refers to these waltz-level expansions.

The beginning of the section structure of the first two waltzes including the respective expansion structure looks like this:

```xml
<section xml:id="Donauwalzer">
        <expansion xml:id="Longest_Version_Krauss" plist="#Introduktion #Walzer-1-withRep-woDalSegno #Walzer-2-withRep-withDalSegno ..." />
        <expansion xml:id="Shorter_Version_Boskovsky" plist="#Introduktion #Walzer-1-woRep-woDalSegno #Walzer-2-woRep-withDalSegno ..."/>
        <section xml:id="Introduktion">
                <section xml:id="Andantino"/>
                <section xml:id="Tempo-di-Valse"/>
        </section>
        <section xml:id="Walzer-1">
                <expansion xml:id="Walzer-1-withRep-woDalSegno" plist="#Walzer-1-A #Walzer-1-B-Upbeat #Walzer-1-B #Walzer-1-B-ending1 #Walzer-1-B #Walzer-1-B-Fine"/>
                <expansion xml:id="Walzer-1-woRep-woDalSegno" plist="#Walzer-1-A #Walzer-1-B-Upbeat #Walzer-1-B #Walzer-1-B-Fine"/>
                <section xml:id="Walzer-1-A"/>
                <section xml:id="Walzer-1-B-Upbeat"/>
                <section xml:id="Walzer-1-B"/>
                <ending xml:id="Walzer-1-B-ending1" n="1."/>
                <ending xml:id="Walzer-1-B-dalSegno" n="2."/>
                <ending xml:id="Walzer-1-B-Fine" n="Fine"/>
        </section>
        <section xml:id="Walzer-2">
                <expansion xml:id="Walzer-2-withRep-withDalSegno" plist="#Walzer-2-A-Upbeat #Walzer-2-A #Walzer-2-A-ending1 #Walzer-2-A #Walzer-2-A-ending2 #Walzer-2-B #Walzer-2-A #Walzer-2-A-Fine"/>
                <expansion xml:id="Walzer-2-woRep-withDalSegno" plist="#Walzer-2-A-Upbeat #Walzer-2-A #Walzer-2-A-ending2 #Walzer-2-B #Walzer-2-A #Walzer-2-A-Fine"/>
                <section xml:id="Walzer-2-A-Upbeat"/>
                <section xml:id="Walzer-2-A"/>
                <ending xml:id="Walzer-2-A-ending1" n="1."/>
                <ending xml:id="Walzer-2-A-ending2" n="2."/>
                <ending xml:id="Walzer-2-A-Fine" n="Fine"/>
        </section>
...
```

The following expansion element refers to the longest and most typical realisation of this piece in the history of the Vienna New Year's Concert series, as first conducted by Clemens Krauss:

```xml
<expansion xml:id="Longest_Version_Krauss" plist="#Introduktion #Walzer-1-withRep-woDalSegno #Walzer-2-withRep-withDalSegno #Walzer-3-withRep1-withRep2-woDalSegno #Walzer-4-withRep1-withRep2-woDalSegno #Walzer-5-withRep-woDalSegno #Coda"/>
```
