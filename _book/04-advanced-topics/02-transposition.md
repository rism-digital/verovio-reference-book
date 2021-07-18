---
title: "Transposition"

examples:
    - name: t-01
      test-suite: chord/chord-005.mei
      xpath:
        - ".//mei:score"
    - name: t-02
      test-suite: chord/chord-005.mei
      options:
        transpose: "M2"
    - name: t-03
      test-suite: chord/chord-005.mei
      options:
        transpose: "-m2"
    - name: t-04
      test-suite: chord/chord-005.mei
      options:
        transpose: "1"
    - name: t-05
      test-suite: chord/chord-005.mei
      options:
        transpose: "m2"
    - name: t-06
      test-suite: chord/chord-005.mei
      options:
        transpose: "a1"
    - name: t-07
      test-suite: chord/chord-005.mei
      options:
        transpose: "E"
    - name: t-08
      test-suite: chord/chord-005.mei
      options:
        transpose: "F#"
    - name: t-09
      test-suite: chord/chord-005.mei
      options:
        transpose: "Gb"
    - name: t-10
      test-suite: chord/chord-005.mei
      options:
        transpose: "+Gb"
    - name: t-11
      test-suite: chord/chord-005.mei
      options:
        transpose: "++Gb"
---


Transposition in Verovio uses the base-40 system that allows for an arbitrary maximum sharp/flat count (where base-40 can handle up to double sharps/flats). The option `--transpose` can be given two types of data: (1) a chromatic interval, or (2) a tonic pitch in the new key with optional direction and octave of transposition added.

### Transposition by chromatic interval

For transposition by chromatic intervals, the format is an optional sign, followed by a chromatic quality followed by a diatonic number of steps.  Examples: `+M2` = up major second, `-d5` = down diminished fifth

The direction of the interval, with `-` indicating down and no sign or a `+` means up.  A special cases is `P1` which is a perfect unison, so `+P1` and `-P1` are equivalent since there is no movement up or down.

For the chromatic quality of the interval, `P` means perfect, `M` means major, `m` means minor, `d` means diminished, `A` means augmented, `dd` means doubly diminished (and so on), `AA` means doubly augmented (and so on).   For `[PdA]` the case of the letter does not matter so `[pDa]` should be interpreted as equivalent. `M` and `m` are case-sensitive (major and minor).

The diatonic interval is any (reasonable) positive integer.  A unison is `1`, a second is `2`, and so on.  Compound intervals an octave and above can also be represented, such as `8` for an octave, a `9` for a ninth (octave plus a second), `10` for a tenth (octave plus a third), `15` is two octaves, and `16` is two octaves plus a second.

Verovio will print an error message if the string option is not formatted correctly, and it will return an error interval which is a very large interval going down.

Example interval names:

| name | meaning |
|------|---------|
| P1 | perfect unison |
| M2 | major second up |
| +M2 | major second up |
| -M2 | major second down |
| m2 | minor second up |
| d2 | diminished second up |
| dd2 | doubly diminished second up |
| A2 | augmented second up |
| AA2 | doubly augmented second up |
| M3 | major third up |
| P4 | perfect fourth up |
| d4 | diminished fourth up |
| A4 | augmented fourth up |
| P8 | perfect octave up |
| P15 | two perfect octaves up |
| m10 | perfect octave plus minor third up |
{: .table .table-condensed .table-sm}

### Transposition by tonic pitch

For transposition by tonic pitch names, the format is made up of an optional direction, a `pname` and an `accid`.

If no direction is given, then the smallest interval will be chosen. For example if starting from C major and transposing to G major, the calculated interval will be down a perfect fourth, since the G below C is closer than the G above C.

When the direction is `+`, the next higher pitch that matches the new tonic will define the interval.  For C major to G major, this is a perfect fifth up. When the direction is `-`, the next lowest pitch that matches the new tonic will define the interval.  For C major to G major, this is a perfect fourth down.

The `+` or `-` direction can be doubled/tripled/etc. to indicate additional octave transpositions.   For example `--g` from C major means to transpose down an octave and a fourth: The fourth to the G below, and then the octave to the next lower G.  Likewise, `+++g` from C major means to transpose up two octaves and a fifth:  A fifth to the G above, then `++` means two octaves above that G.

When using a case-insensitive `@pname` for the tonic of the new key, use `([A-Ga-g])` followed by an optional `accid` for the new key tonic. This is also case-insensitive: `([Ss]*|[Ff]*)`.

Examples:  

| tonic parameter | meaning |
|----------------|----------|
| `g`   | transpose current tonic to closest G tonic note (up or down a fourth from current tonic) |
| `+g`  | transpose to the next higher G tonic |
| `-g`  | transpose down to next lower G tonic|
| `++g` | transpose to second next higher G tonic |
| `--g` | transpose to second next lower G tonic |
| `ff`  | transpose to nearest F-flat |
| `-cs` | transpose to next lower C-sharp |
|`++BF` | transpose up to second next higher B-flat |
{: .table .table-condensed .table-sm}

### Illustrated examples

Here is a test example music to transpose - note the `@key.sig` is expected for transposition to work properly:

{% include music-notation example="t-01" %}

Setting `transpose: "M2"` will transpose the music up a major second from C to D:

{% include music-notation-only example="t-02" %}

Setting `transpose: "-m2"` To go down a minor second from C to B:

{% include music-notation-only example="t-03" %}

Common intervals:  `m3` = minor third, `M3` = major 3rd, `P4` = perfect fourth, `P5` = perfect fifth, `d5` = diminished fifth, `A4` = augmented fourth.

It is also possible to give semitone steps, with 1 being one semitone, 2 being two semitones, etc.  This method is less precise, and the computer will make an automatic calculating to minimize the number of accidentals in the target key signature.  

For example `transpose: "1"` will display in D-flat major:

{% include music-notation-only example="t-04" %}

This is equivalent to going up a minor second with `transpose: "-m2"`:

{% include music-notation-only example="t-05" %}

If you need to transpose to C-sharp major, then you cannot use integers, but must use the full musical interval, which in this case is `transpose: "A1"` for an augmented unison:

{% include music-notation-only example="t-06" %}

(`a1` and `A1` are the same, but `m2` and `M2` are not equivalent).

It is also possible to give the tonic note of the new key.  For example `transpose: "E"` means to transpose to E major (or minor, since the mode will not be changed). This feature requires that the music contain key information which is not always present in MusicXML data.  It can also be incorrect, which may cause problems, so use this option with care in an automatic situation.

{% include music-notation-only example="t-07" %}

F-sharp major with `transpose: "F#"`, which is equivalent to a transposition of `A4`:

{% include music-notation-only example="t-08" %}

G-flat major with `transpose: "Gb"`, which is equivalent to `d5`:

{% include music-notation-only example="t-09" %}

Notice that this method moves to the closest tonic.  To force G-flat major above, add a `+` with `transpose: "+Gb"`:

{% include music-notation-only example="t-10" %}

To go another octave above, add two `++` with `transpose: "++Gb"`:

{% include music-notation-only example="t-11" %}

### Algorithm for transposition by tonic

The algorithm for transposition by tonic proceeds as follow:

* Find the key information at the start of the music in each part. If all parts have the same transposition (or no parts have transposition), then use the `@pname` and `@accid` as the reference pitch for which an interval will be calculated for the input transposition target tonic.

* If all parts do not have the same transposition, then choose a part that does not have a transposition from which to extract the key information. If all parts have transpositions, but the transpositions are different, then apply transposition to the key information to get it to sounding pitch for one of those instruments and use this transposed pitch as the basis for the key transposition.

* The key information may be stored in one of two main locations: `staffDef@key.pname`/`staffDef@key.accid` (the most common currently) or `keySig@pname`/`keySig@accid`.  The `staffDef@key.mode`/`keySig@mode` is not needed.  This key information must come before the first notes on the staff.  `keySig` may be found as a child of `staffDef`, or may be found outside of the `staffDef` (at the start  `layer`) or in `scoreDef` if it applies to all staves in the score (or the majority of staves in the score?).

* If there is no key information found before the first notes of the music, print an error warning and do not transpose.

* Once the original key is known, then the interval necessary for transposition can be calculated. The next step is to identify the closest new tonic's octave.  For extra `+` or `-` in the tonic string, add an octave to the interval to calculate the final interval for transposition.

At this point the key transposition process becomes equivalent to the interval transposition process.
