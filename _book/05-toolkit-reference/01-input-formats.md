---
title: "Input formats"

examples:
    - name: humdrum-01
      options:
        breaks: auto
        header: auto
      inline: |-
        !!!COM: Mozart, Wolfgang Amadeus
        !!!OTL: Piano Sonata No. 2 in F major
        !!!OMV: 1
        !!!SCT1: K1 280
        !!!SCT2: K6 189e
        !!!OMD: Allegro assai
        **kern	**kern	**dynam
        *staff2	*staff1	*staff1/2
        *clefF4	*clefG2	*
        *k[b-]	*k[b-]	*
        *F:	*F:	*
        *M3/4	*M3/4	*
        *MM152	*MM152	*
        =1-	=1-	=1-
        4FF 4F	4c: 4f: 4a: 4cc:	f
        4C	4a/ 4cc/	.
        4AA	4a/ 4cc/	.
        =2	=2	=2
        4FF	4.a/ 4.cc/	.
        4FFF	.	.
        .	(16ddLL	.
        .	16ccJJ	.
        4r	16b-LL	.
        .	16a	.
        .	16g	.
        .	16fJJ	.
        =3	=3	=3
        8F 8AL	4ff	.
        8F 8A	.	.
        8F 8G 8B-	4ee	.
        8F 8G 8B-	.	.
        8F 8A 8c	4ee-)	.
        8F 8A 8cJ	.	.
        =4	=4	=4
        8F 8B- 8dL	4dd	.
        8F 8B- 8d	.	.
        8F 8B- 8d	4r	.
        8F 8B- 8d	.	.
        8F 8B- 8d	4r	.
        8F 8B- 8dJ	.	.
        =5	=5	=5
        8F 8G 8eL	(8ccL	p
        8F 8G 8e	8b-J)	.
        8F 8G 8e	4b-'	.
        8F 8G 8e	.	.
        8F 8G 8e	4r	.
        8F 8G 8eJ	.	.
        =6	=6	=6
        *-	*-	*-
    - name: humdrum-02
      options:
        breaks: auto
        header: auto
      inline: |-
        !!!OTL@@DE: Liebes-A-B-C
        !!!COM: Pohlenz, August
        !!!CDT: 1790/07/03/-1843/03/09/
        !!!ODT: 1827
        !!!OMD: Allegretto
        !!!LYR: Gerhard, Wilhelm
        !!!LDT: 1826
        !!!OCL: Erk, Ludwig
        !!!GCO: Deutscher Liederschatz, Band 1
        **kern	**kern	**kern	**text	**text	**text	**text	**text	**text	**text
        *staff3	*staff2	*staff1	*staff1	*staff1	*staff1	*staff1	*staff1	*staff1	*staff1
        *Ipiano	*Ipiano	*Ivox	*	*	*	*	*	*	*
        *clefF4	*clefG2	*clefG2	*	*	*	*	*	*	*
        *k[b-]	*k[b-]	*k[b-]	*	*	*	*	*	*	*
        *F:	*F:	*F:	*	*	*	*	*	*	*
        *M3/8	*M3/8	*M3/8	*	*	*	*	*	*	*
        *MM100	*MM100	*MM100	*	*	*	*	*	*	*
        =1-	=1-	=1-	=1-	=1-	=1-	=1-	=1-	=1-	=1-
        *^	*^	*	*	*	*	*	*	*	*
        8AL	4F	8fL	4c	8f	A	E	I	M	Q	U	Yp-
        8G	.	8e	.	8e	B	F	K	N	R	V	-si-
        8AJ	8F	8fJ	8c	8f	C	G	und	O	S	W	-lon
        *v	*v	*	*	*	*	*	*	*	*	*	*
        *	*v	*v	*	*	*	*	*	*	*	*
        =2	=2	=2	=2	=2	=2	=2	=2	=2	=2
        4C 4c	4e 4g	4g	D,	H,	L,	P,	T,	X,	Z,
        8r	8r	8r	.	.	.	.	.	.	.
        =3	=3	=3	=3	=3	=3	=3	=3	=3	=3
        4C 4c	8e 8gL	8g	wenn	wärst	Aeug-	gleich	Schei-	mach'	nun
        .	8d 8f	8f	ich	du	-lein	ei-	-den	ei-	geh'
        8C 8c	8e 8gJ	8g	dich	doch	so	-ner	thut	-nen	zu
        =4	=4	=4	=4	=4	=4	=4	=4	=4	=4
        4F 4c	4f 4a	4a	seh',	da!	hell	Fee	weh.	Knix,	Bett!
        8r	8r	8r	.	.	.	.	.	.	.
        =5	=5	=5	=5	=5	=5	=5	=5	=5	=5
        4DD 4D	8r	8a	dich,	Drück-	glänz-	fes-	Hal-	drückt	Bricht
        .	8c 8d 8f#L	8a	mei-	-te	-ten	-selst	-te	dir	doch
        8r	8c 8d 8f#J	8dd	-ne	mein	in	du	mit	ein	die
        =6	=6	=6	=6	=6	=6	=6	=6	=6	=6
        4GG	8r	8.cc	sü-	treu-	Lie-	Herz	Herz	jun-	Nacht
        .	8B- 8d 8gL	.	.	.	.	.	.	.	.
        .	.	16b-	-sse	-er	-bes-	und	und	-ger	schon
        8r	8B- 8d 8gJ	8b-	Lust,	Arm,	-pracht	Sinn,	Mund	Fant	ein,
        =7	=7	=7	=7	=7	=7	=7	=7	=7	=7
        4CC 4C	8r	8g	klopft	Hol-	mir	Grüb-	treu	zärt-	kann
        .	8B- 8c 8eL	8g	die	-de,	aus	-chen	an	-lich	ja
        8r	8B- 8c 8eJ	8cc	em-	dich	der	in	dem	die	nicht
        =8	=8	=8	=8	=8	=8	=8	=8	=8	=8
        4FF	8r	8.b-	-pör-	lie-	Wim-	Wang'	Lie-	Schwa-	bei
        .	8A 8c 8fL	.	.	.	.	.	.	.	.
        .	.	16a	-te	-be-	-pern	und	-bes-	-nen-	dir
        8r	8A 8c 8fJ	8a	Brust,	warm!	Nacht,	Kinn,	-bund,	-hand,	sein,
        =9	=9	=9	=9	=9	=9	=9	=9	=9	=9
        8FFL	8A 8fL	8f	wird	Schätz-	tra-	Ro-	sa-	a-	wenn
        8GG	8B- 8e	8e	mir	-chen,	-fen	-sen-	-ge	-ber	ich
        8AAJ	8c 8fJ	8f	so	ach	wie	-glut,	mir	nur	auch
        =10	=10	=10	=10	=10	=10	=10	=10	=10	=10
        4BB-	8r	8.ee	wohl	wärst	bli-	Li-	nie	ern-	Flü-
        .	8B- 8d 8gL	.	.	.	.	.	.	.	.
        .	.	16dd	und	du	-tzes-	-lien-	A-	-sten	-gel
        8r	8B- 8d 8gJ	8dd	weh,	da!	-schnell,	schnee,	de!	Blicks	hätt'!
        =11	=11	=11	=11	=11	=11	=11	=11	=11	=11
        4C	8r	8cc	wenn	wärst	Aeug-	rei-	Schei-	mach'	Geh'
        .	8B- 8c 8eL	8g	ich	du	-lein	-zen-	-den	ihm	nur
        8r	8B- 8c 8eJ	8a	dich	mir	so	-de	thut	den	zu
        =12	=12	=12	=12	=12	=12	=12	=12	=12	=12
        4FF 4F	4A 4c 4f	4f	seh'!	nah'!	hell.	Fee!	weh.	Knix!	Bett!
        8r	8r	8r	.	.	.	.	.	.	.
        ==	==	==	==	==	==	==	==	==	==
        *-	*-	*-	*-	*-	*-	*-	*-	*-	*-
        !!!SMS: Deutscher Liederschatz, Band 1, Ludwig Erk, ed.
        !!!ENC: Craig Stuart Sapp
        !!!END: 2004/05/16/
        !!!EED: 2011/02/05/
        !!!EFL: 001/651
        !!muse2ps: s^(.){(..)}^z21jv200,114,144
        !!CharacterEncoding: UTF-8

    - name: pae-01
      url: https://raw.githubusercontent.com/rism-digital/verovio/develop/doc/tests/pae/6_mixed/beams_and_tuplets.pae
    - name: pae-02
      url: https://raw.githubusercontent.com/rism-digital/verovio/develop/doc/tests/pae/6_mixed/measure_rest_and_keysig_change.pae
    - name: pae-03
      url: https://raw.githubusercontent.com/rism-digital/verovio/develop/doc/tests/pae/6_mixed/clef_changes.pae
    - name: pae-04
      url: https://raw.githubusercontent.com/rism-digital/verovio/develop/doc/tests/pae/6_mixed/trills_and_fermata.pae
    - name: pae-05
      url: https://raw.githubusercontent.com/rism-digital/verovio/develop/doc/tests/pae/6_mixed/ties.pae
    - name: pae-06
      url: https://raw.githubusercontent.com/rism-digital/verovio/develop/doc/tests/pae/6_mixed/grace_notes_accaciature.pae
    - name: pae-07
      url: https://raw.githubusercontent.com/rism-digital/verovio/develop/doc/tests/pae/6_mixed/grace_notes_appogiature.pae
    - name: pae-08
      url: https://raw.githubusercontent.com/rism-digital/verovio/develop/doc/tests/pae/6_mixed/rhythmic_patterns.pae
    - name: pae-09
      url: https://raw.githubusercontent.com/rism-digital/verovio/develop/doc/tests/pae/6_mixed/abbreviated_writing.pae

    - name: abc-01
      options:
        breaks: auto
        header: auto
      inline: |-
        X: 99
        T:Short tune
        C:K. Rettinghaus
        M:4/4
        L:1/4
        K:G
        D|G>ABG|A>BAD|G>ABA|G3|]
    - name: abc-03
      options:
        breaks: auto
        header: auto
      inline: |-
        X: 99
        T:Short tune
        C:K. Rettinghaus
        M:4/4
        L:1/4
        Q:"Andante"
        K:G
        "D"!mf!D|"G"G>A "Em"B {/A/}G|"Am"A>B "D7"A{/E/}D|"G"G>A "C"B "D"A|"G"G3|]
    - name: abc-04
      options:
        breaks: encoded
        header: auto
      inline: |-
        X:1
        T:Dusty Miller, The
        T:Binny's Jig
        C:Trad.
        R:DH
        M:3/4
        K:G
        B>cd BAG|FA Ac BA|B>cd BAG|DG GB AG:|
        Bdd gfg|aA Ac BA|Bdd gfa|gG GB AG:|
        BG G/2G/2G BG|FA Ac BA|BG G/2G/2G BG|DG GB AG:|
    - name: abc-05
      options:
        breaks: auto
        header: auto
      inline: |-
        X:2
        T:Old Sir Simon the King
        C:Trad.
        S:Offord MSS          % from Offord manuscript
        N:see also Playford   % reference note
        M:9/8
        R:SJ                  % slip jig
        N:originally in C     % transcription note
        K:G
        D|GFG GAG G2D|GFG GAG F2D|EFE EFE EFG|A2G F2E D2:|
        D|GAG GAB d2D|GAG GAB c2D|[1 EFE EFE EFG|A2G F2E D2:|\\\ % no line-break in score
        M:12/8                % change of meter
        [2 E2E EFE E2E EFG|\\\  % no line-break in score
        M:9/8                 % change of meter
        A2G F2E D2|]
    - name: abc-06
      inline: |-
        X:1
        T:Broken rhythm markers
        M:C
        K:C
        A>A A2>A2 A>>A A2>>>A2|]
    - name: abc-07
      inline: |-
        X:1
        T:Ties and Slurs
        M:C
        K:C
        (AA) (A(A)A) ((AA)A) (A|A) A-A A-A-A A2-|A4|]
    - name: abc-08
      inline: |-
        X:1
        T:Accidentals
        M:C
        K:C
        __A _A =A ^A ^^A|]
    - name: abc-09
      inline: |-
        X:1
        T:Chords
        M:2/4
        K:C
        [CEGc] [C2G2] [CE][DF]|[D2F2][EG][FA] [A4d4]|]

  
---

When data is loaded into Verovio with no input format specifies, it tries to detect it based on the initial content of the data. MEI is assume to be the default format if auto detection fails. In such cases, the format can be given explicitly with the option `--input-from` (or `-f`).

### MEI

The native input format for Verovio is MEI. Verovio supports MEI as input format from MEI 2013 onwards. From Verovio 2.x.x, the plan is to have even version numbers for Verovio releases using a stable version of MEI, and odd version numbers for releases using a development version of MEI. It means that once MEI 5.0 will be released, Verovio will move to version 4.x.x. Older versions of MEI are still supported by newer versions of Verovio.

When loading MEI data into Verovio and outputting MEI, elements that are not supported by Verovio will be ignored. This means that they are not loaded into memory and will not be preserved in the MEI output. This includes the element themselves, but also any descendant they might have. A warning will be given in the console. For example:
```bash
[Warning] Unsupported '<ossia>' within <measure>
```

#### Support for previous version of MEI

When an MEI file in loaded into Verovio and is not of the latest version for that version of Verovio, it performs upgrade steps for the features that were supported by Verovio for that older version of MEI.

**MEI 2013 files**

Various attributes in `<page>` and `<measure>` for the page-based version of MEI are upgraded (experimental work).

**MEI 3.0 files**

The following elements / attributes are upgraded:
* `turn@form`
* `staffDef@barthru`
* `staffDef@label`
* `staffDef@label.abbr`
* `staffGrp@label`
* `staffGrp@label.abbr`
* `fTrem@slash`
* `@dur.ges`
* `beatRpt`

{% row %}{% col %}
*Original data*
```xml
<turn form="inv"/>
<turn form="norm"/>
```
{% endcol %}{% col %}
*Upgraded data*
```xml
<turn form="lower"/>
<turn form="upper"/>
```
{% endcol %}{% endrow %}

{% row %}{% col %}
*Original data*
```xml
<staff barthru="true"/>
```
{% endcol %}{% col %}
*Upgraded data*
```xml
<staff bar.thru="true"/>
```
{% endcol %}{% endrow %}

{% row %}{% col %}
*Original data*
```xml
<staffDef label="violin I" label.abbr="vl I"/>
```
{% endcol %}{% col %}
*Upgraded data*
```xml
<staffDef>
   <label>Violin I<label>
   <labelAbbr>Vl I<labelAbbr>
</staffDef>
```
{% endcol %}{% endrow %}

{% row %}{% col %}
*Original data*
```xml
<fTrem slash="2"/>
```
{% endcol %}{% col %}
*Upgraded data*
```xml
<fTrem beams="2"/>
```
{% endcol %}{% endrow %}

{% row %}{% col %}
*Original data*
```xml
<note dur.ges="8p"/>
<note dur.ges="32r"/>
<note dur.ges="32s"/>
```
{% endcol %}{% col %}
*Upgraded data*
```xml
<note dur.ppq="8"/>
<note dur.recip="32"/>
<note dur.real="32"/>
```
{% endcol %}{% endrow %}

{% row %}{% col %}
*Original data*
```xml
<beatRpt rend="4"/>
<beatRpt rend="8"/>
<beatRpt rend="16"/>
<beatRpt form="4"/>
```
{% endcol %}{% col %}
*Upgraded data*
```xml
<beatRpt slash="1"/>
<beatRpt slash="1"/>
<beatRpt slash="2"/>
<beatRpt slash="1"/>
```
{% endcol %}{% endrow %}


**MEI 4.0 files**

The following elements / attributes are upgraded:
* `mensur@tempus`
* `mensur@prolatio`

{% row %}{% col %}
*Original data*
```xml
<mensur tempus="3"/>
<mensur tempus="2"/>
```
{% endcol %}{% col %}
*Upgraded data*
```xml
<mensur tempus="3" sign="0"/>
<mensur tempus="2" sign="C"/>
```
{% endcol %}{% endrow %}

{% row %}{% col %}
*Original data*
```xml
<mensur prolatio="3"/>
<mensur prolatio="2"/>
```
{% endcol %}{% col %}
*Upgraded data*
```xml
<mensur prolatio="3" dot="true"/>
<mensur prolatio="2" dot="false"/>
```
{% endcol %}{% endrow %}

#### Page-based MEI

{% aside .warning %}
The MEI page-based model is not part of MEI. It was put in place for the development of Verovio and can still change in the future. It will be documented as input format once it is stabilized.
{% endaside %}

### Humdrum

Humdrum data is an analytic music code for transcribing fully polyphonic textures. Humdrum syntax presents notes of the score in strict time sequence. Each data row represents all notes sounding or events occurring at the same time, and each column traces the melodic line of the individual parts. More information about the syntax is available on the [Humdrum](http://www.humdrum.org/) website.

#### Examples

The following example from Mozart's piano sonata in F major, K1 280 (K6 189e), mvmt. 1, is generated dynamically within this page using the JavaScript form of Verovio, inputting the Humdrum data that follows.

{% include music-notation-only example="humdrum-01" %}

The data consists of three separate streams of information, called spines that usually consist of one column, but sometime more due to spine splits into subspines. The first column represents music on the bottom staff, the second column represents the top staff, and the third column contains the dynamics, which in this case apply to both staves. 

{% assign humdrum = page.examples | where: "name", "humdrum-01" | first %}
```
{{ humdrum.inline }}
```

#### Verovio Humdrum Viewer

The [Verovio Humdrum Viewer](http://verovio.humdrum.org) (VHV) is a special-purpose interactive website for viewing and editing Humdrum files with the Verovio notation egraving library.  You can view the full score for the above Mozart example in VHV from this link: [verovio.humdrum.org/?file=mozart/sonatas/sonata02-1.krn](http://verovio.humdrum.org/?file=mozart/sonatas/sonata02-1.krn).

When on a VHV notation page, try pressing the key "<b>p</b>" to view the scan of the original print from which the musical data was encoded.  Also try pressing "<b>m</b>" to view the internal conversion to MEI data.  Vi users can try pressing "<b>v</b>" to toggle between the basic and vim modes for the text editor.  Use the left/right arrow keys or PageUp/PageDown to navigate to different pages.  Press shift-left/right arrows to go to the next/previous work/movement in the repertory.

Sample repertories of Humdrum data displayed in the Verovio Humdrum Viewer:

* [J.S. Bach chorales](http://verovio.humdrum.org/?file=chorales) (When viewing a chorale, type the "o" letter key to toggle view of the original historic clefs.)
* [Mozart piano sonatas](http://verovio.humdrum.org/?file=mozart/sonatas)
* [Beethoven piano sontats](http://verovio.humdrum.org/?file=beethoven/sonatas)
* [Beethoven string quartets](http://verovio.humdrum.org/?file=beethoven/quartets)
* [Chopin mazurkas](http://verovio.humdrum.org/?file=cc/chopin/mazurka)
* [Works of Scott Joplin](http://verovio.humdrum.org/?file=joplin)
* [Works of Josquin des Prez](http://verovio.humdrum.org/?file=jrp/Jos)
* [Works of Johannes Ockeghem](http://verovio.humdrum.org/?file=jrp/Ock)
* [Works of Pierre de la Rue](http://verovio.humdrum.org/?file=jrp/Rue)
* [Works of Mabrianus de Orto](http://verovio.humdrum.org/?file=jrp/Ort)
* [Deutscher Liederschatz, Band I](http://verovio.humdrum.org/?file=liederschatz1) (Edited by Ludwig Erk.)

#### Command-line interface usage

To typeset music in the Humdrum format on the command-line:

```bash
$ verovio -f humdrum input.krn -o output.svg
```

You can usually use the auto-detection feature of verovio by omitting the option.

```bash
$ verovio input.krn -o output.svg
```

The output filename will have the same basename as the input if the option is not given, so in this case the output will be called .

```bash
$ verovio file.krn
```

Standard input/output can be used with the verovio command by giving a dash for standard input and to send the output to standard output.

```bash
$ cat input.krn | verovio - -o - > output.svg
```

To convert to MEI data:

```bash
$ verovio file.krn --no-layout --all-pages -t mei
```

#### A more complicated example

Below is a song for voice and piano accompaniment. Each verse is listed in a separate spine of `**text` in addition to the three staves of music in `**kern` spines and one dynamics (`**dynam`) spine.

{% include music-notation-only example="humdrum-02" %}

{% assign humdrum = page.examples | where: "name", "humdrum-02" | first %}
```
{{ humdrum.inline }}
```

### MusicXML

Verovio has two converters for importing MusicXML data. The first one directly converts MusicXML into MEI. The second one first converts to Humdrum and then converts the Humdrum to MEI. By default, the first importer is used. It is also the one triggered when the value `xml` is passed to the `--input-from` option.

#### Importing MusicXML via Humdrum

For the JavaScript toolkit, the MusicXML import via Humdrum is available only for builds where Humdrum support has been enabled specifically. See the related [section](/installing-or-building-from-sources/javascript-and-webassembly.html) for more information about this. With builds that support Humdrum, the MusicXML import via Humdrum can be triggered by setting the `inputFrom` option to `musicxml-hum`.

With the command-line tool and the Python toolkit, Humdrum support is enabled by default. The MusicXML import via Humdrum can itself be made the default MusicXML importer with the build option `MUSICXML_DEFAULT_HUMDRUM`. See the [command-line](/installing-or-building-from-sources/command-line.html) section for more information on how to change build options. With this, MusicXML files will be loaded via the Humdrum importer. The direct importer can still be chosen with the value `xml` passed to `--input-from`.
    
### Plaine and Easie

The Plaine & Easie Code is a library standard that enables entering music incipits in modern or mensural notation. It is mostly used by the [Répertoire International des Sources Musicales](https://rism.info) (RISM) for inventorying the music incipits of the manuscripts. More information about the syntax is available on the [IAML](http://www.iaml.info/plaine-easie-code) website. 

Plaine and Easie input in Verovio is a text file (or string) with a list of the following `@key:value` lines:
* `@clef` – the initial clef
* `@keysig` – the initial key signature
* `@timesig` – the initial time signature
* `@data` – the incipit content

{% aside %}
The structure of this input format is not part of the PAE specification but only a convention put in place for Verovio
{% endaside %}

#### Examples

**Beams and tuplets**

{% assign pae_02 = page.examples | where: "name", "pae-01" | first %}
```
{% remote_include {{ pae_02.url }} %}
```
{% include music-notation-only example="pae-01" %}

**Measure rests and key and time signature changes**

{% assign pae = page.examples | where: "name", "pae-02" | first %}
```
{% remote_include {{ pae.url }} %}
```
{% include music-notation-only example="pae-02" %}

**Clef changes**

{% assign pae = page.examples | where: "name", "pae-03" | first %}
```
{% remote_include {{ pae.url }} %}
```
{% include music-notation-only example="pae-03" %}

**Trills and fermata**

{% assign pae = page.examples | where: "name", "pae-04" | first %}
```
{% remote_include {{ pae.url }} %}
```
{% include music-notation-only example="pae-04" %}

**Ties**

{% assign pae = page.examples | where: "name", "pae-05" | first %}
```
{% remote_include {{ pae.url }} %}
```
{% include music-notation-only example="pae-05" %}

**Grace notes (acciaccaturas)**

{% assign pae = page.examples | where: "name", "pae-06" | first %}
```
{% remote_include {{ pae.url }} %}
```
{% include music-notation-only example="pae-06" %}

**Grace notes (appoggiaturas)**

{% assign pae = page.examples | where: "name", "pae-07" | first %}
```
{% remote_include {{ pae.url }} %}
```
{% include music-notation-only example="pae-07" %}

**Rhythmic patterns**

{% assign pae = page.examples | where: "name", "pae-08" | first %}
```
{% remote_include {{ pae.url }} %}
```
{% include music-notation-only example="pae-08" %}

**Abbreviated writing**

{% assign pae = page.examples | where: "name", "pae-09" | first %}
```
{% remote_include {{ pae.url }} %}
```
{% include music-notation-only example="pae-09" %}


### ABC

Abc is a text-based music notation system originally designed for use with folk and traditional tunes and used throughout the web. You can find the documentation on the [ABC notation](http://abcnotation.com/wiki/abc:standard) website. 

#### Examples

Let's start with a simple little tune. 

{% assign abc = page.examples | where: "name", "abc-01" | first %}
```
{{ abc.inline }}
```
{% include music-notation-only example="abc-01" %}

Verovio takes several information fields into account, e.g. the reference number `X`, the tune title `T`, the meter `M`, the unit note length `L`, the key `K`. As you can see, Verovio prints the header as expected by default. You may suppress this behaviour with the `--header none` option.

Now let's add a literal tempo as well as some grace notes and chord symbols. Dynamics are also very important! Note that chord symbols are put above the melody. 

{% assign abc = page.examples | where: "name", "abc-03" | first %}
```
{{ abc.inline }}
```
{% include music-notation-only example="abc-03" %}

With the option `--breaks: 'encoded'` Verovio keeps the encoded layout, as you can see on this page. The default value is `'auto'`, which lets Verovio to decide where to put a line-break. 

{% assign abc = page.examples | where: "name", "abc-04" | first %}
```
{{ abc.inline }}
```
{% include music-notation-only example="abc-04" %}

Alternatively it is always possible to suppress score line-breaks. Meter changes are also supported. 

{% assign abc = page.examples | where: "name", "abc-05" | first %}
```
{{ abc.inline }}
```
{% include music-notation-only example="abc-05" %}

**Broken rhythm markers**

{% assign abc = page.examples | where: "name", "abc-06" | first %}
```
{{ abc.inline }}
```
{% include music-notation-only example="abc-06" %}

**Ties and slurs**

Verovio correctly differentiates between ties and slurs. 

{% assign abc = page.examples | where: "name", "abc-07" | first %}
```
{{ abc.inline }}
```
{% include music-notation-only example="abc-07" %}

**Accidentals**

{% assign abc = page.examples | where: "name", "abc-08" | first %}
```
{{ abc.inline }}
```
{% include music-notation-only example="abc-08" %}

**Chords**

{% assign abc = page.examples | where: "name", "abc-09" | first %}
```
{{ abc.inline }}
```
{% include music-notation-only example="abc-09" %}

#### Known limitations:
* Verovio imports only the first tune in a collection
* Tuplets are not supported
* User defined symbols are not supported
* Multi-voice music is not supported
* Lyrics are not supported yet