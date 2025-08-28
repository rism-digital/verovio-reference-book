---
title: "Repetition expansion"

examples:
    - name: expansion-001
      test-suite: expansion/expansion-001.mei
      xpath:
        - ".//mei:section"

    - name: expansion-001-default
      test-suite: expansion/expansion-001.mei
      options:
        expand: 'expansion-default'

    - name: expansion-001-minimal
      test-suite: expansion/expansion-001.mei
      options:
        expand: 'expansion-minimal'

    - name: expansion-001-maximal
      test-suite: expansion/expansion-001.mei
      options:
        expand: 'expansion-maximal'

    - name: expansion-002
      test-suite: expansion/expansion-002.mei

    - name: expansion-002-default
      test-suite: expansion/expansion-002.mei
      options:
        expand: 'default'

---

Scores may contain repetitions, endings, directives to repeat a section from a certain location in the score, such as dal segno, or similar. Such instructions advise the performer to correctly realise the repetition structure during performance. The MEI schema provides the [`<expansion>` element](https://music-encoding.org/guidelines/v5/elements/expansion) to encode specific repetition versions of a scores' repetition structure. Verovio supports this MEI element with the `--expand` toolkit option. 

The `expansion` element is expected to be the first element in a `section` or `ending` and must contain descendant `expansion`, `ending`, or `rdg` elements (see [guidelines for section](https://music-encoding.org/guidelines/v5/elements/section)). Its `@plist` attribute may point to its descendant `section`, `ending`, `rdg`, or `lem` elements to indicate a particular unfolding version of that excerpt of the score. See the [MEI guidelines for a simple expansion example](https://music-encoding.org/guidelines/v5/content/shared.html#sharedMdivContent).

### Minuet example

A typical MEI example is given below containing a straight-forward repetition structure in which the Minuet and the Trio each is repeated once with different endings. As indicated by "Menuett da capo", the performer is requested to repeat the Minuet after the Trio, but then without repetition, going directly to `A2` to terminate the performance.

{% include music-notation-only example="expansion-001" %}

```xml
<section xml:id="all">
  <expansion xml:id="expansion-default" plist="#A #A1 #A #A2 #B #B1 #B #B2 #A #A2"/>
  <expansion xml:id="expansion-minimal" plist="#A #A2 #B #B2 #A #A2"/>
  <expansion xml:id="expansion-maximal" plist="#A #A1 #A #A2 #B #B1 #B #B2 #A #A1 #A #A2"/>
  <section xml:id="A"/>
  <ending xml:id="A1" lendsym="angledown" n="1."/>
  <ending xml:id="A2" lendsym="angledown" n="2."/>
  <section xml:id="B"/>
  <ending xml:id="B1" lendsym="angledown" n="1."/>
  <ending xml:id="B2" lendsym="angledown" n="2."/>
</section>
```

The default expansion is engraved by Verovio by passing the `xml:id` of the expansion element as an option to the toolkit, e.g. `--expand expansion-default` for the command-line or `expand: 'expansion-default'` for Javascript/Python options, and it looks like this:

{% include music-notation-only example="expansion-001-default" %}

This example also contains a minimal expansion that omits sections A1 and B1, but still repeats the Minuet:
```xml
<expansion xml:id="expansion-minimal" plist="#A #A2 #B #B2 #A #A2"/>
```

{% include music-notation-only example="expansion-001-minimal" %}

This example also contains a maximal expansion that realises all repeats, also in the repeated Minuet:
```xml
<expansion xml:id="expansion-maximal" plist="#A #A1 #A #A2 #B #B1 #B #B2 #A #A1 #A #A2"/>
```

{% include music-notation-only example="expansion-001-maximal" %}


#### Exporting an expansionmap

For sections that get cloned, Verovio generates predictable xml:ids for all containing elements, adding a `-rendX` to the existing xml:id, while `X` is a number starting from 2 for the first repetition of a given element. Thus, `A-rend3` would refer to the third occurence (or the second repetition) of section A. To be able to retrieve the relationship between the original score and a unfolded repeats, Verovio provides access to the expansionmap, a JSON object that contains key-value pairs with unique keys for each xml:id in the encoding (both the original and the unfolded elements). 

More information on expansionmap at [Output formats](/toolkit-reference/output-formats.html#expansionmap).

### Example with re-ordered sections

The following example has a slightly more complex default expansion structure that requires section A to be rendered three times, each time choosing a different ending.

{% include music-notation-only example="expansion-002" %}

To be expanded with the default expansion
```xml
<expansion xml:id="default" plist="#Upbeat #A #A1 #A #A2 #B #A #A-Fine"/>
```
To accommodate this complexity, Verovio automatically re-orders the section structure so that it looks like this: 

{% include music-notation-only example="expansion-002-default" %}



### Hierarchical expansion structure

Refer to Blue Danube example with complex real-world structure.
