---
title: "Internal structure"
---

Verovio provides a self-contained typesetting engine that is directly capable of rendering MEI to a graphical representation in high quality. Its main goal is to develop a library with an internal structure identical to MEI as far as possible. 

For practical reasons, however, the Verovio library uses a page-based customization of MEI internally. Since the modifications introduced by the customization are very limited, the Verovio library can also be used to render un-customized MEI files. With the page-based customization, the content of the music is encoded in `<page>` elements that are themselves contained in a `<pages>` element within `<mdiv>`.

A `<page>` element contains `<system>` elements. From there, the encoding is identical to standard MEI. That is, a `<system>` element will contain `<measure>` elements or `<staff>` elements that are both un-customized, depending on whether the music is measured or un-measured. 

### Layout and positioning

The idea of a page-based customization is also to make it possible to encode the positioning of elements directly in the content tree. This can be useful where the encoding represents one single source with one image per page. This is typically the case with optical music recognition applications. Verovio supports both positioned elements and automatic layout, which is the default when un-customized MEI files are rendered.

The page-based organization is modeled by a MEI customization that defines the structure described above. The ODD file of the customization and the corresponding RNG schema are available from the [MEI Incubator](https://github.com/music-encoding/mei-incubator/tree/master/page-based). This is still work-in-progress. 

### SVG structure

One advantage of SVG rendering over other formats (e.g., images or PDF) is that SVG is rendered natively in all modern web-browsers. Because it is in XML, it also has the advantage that it is well suited to interaction in the browser, since every graphic is an XML element that is easy addressable in the DOM. With Verovio, we also have the advantage that the SVG is organized in such a way that the MEI structure is preserved as much as possible. 

To give an example, a `<note>` element with an `xml:id` attribute in the MEI file will have a corresponding `<g>` element in the SVG with and `class` attribute with a value of `"note"` and an `id` attribute corresponding to the `xml:id`. This makes interaction with the SVG using JavaScript very easy. The hierarchy of the element is also preserved as shown below. 

```xml
<tuplet xml:id="t1" num="3" numbase="2">
  <beam xml:id="b1">
    <note xml:id="n1" pname="d" oct="5" dur="8" />
    <note xml:id="n2" pname="e" oct="5" dur="16" dots="1"/>
    <note xml:id="n3" pname="d" oct="5" dur="32" />
    <note xml:id="n4" pname="c" oct="5" dur="8" accid="s"/>
  </beam>
</tuplet>
<beam xml:id="b2">
  <tuplet xml:id="t2" num="3" numbase="2">
    <note xml:id="n5" pname="d" oct="5" dur="8" />
    <note xml:id="n6" pname="e" oct="5" dur="16" dots="1"/>
    <note xml:id="n7" pname="f" oct="5" dur="32" accid="s"/>
    <note xml:id="n8" pname="e" oct="5" dur="8"/>
  </tuplet>
</beam>
```
{% row %}
{% col 5 %}
![tuplet-and-beams](/images/advanced-topics/internal-structure/tuplet-beam.png){:.img-responsive}
{% endcol %}
{% col 7 %}

```xml
<g class="tuplet" id="t1">
  <g class="beam" id="b1">
    <g class="note" id="n1"></g>
    <g class="note" id="n2"></g>
    <g class="note" id="n3"></g>
    <g class="note" id="n4"></g>
  </g>
</g>
<g class="beam" id="b2">
  <g class="tuplet" id="t2">
    <g class="note" id="n5"></g>
    <g class="note" id="n6"></g>
    <g class="note" id="n7"></g>
    <g class="note" id="n8"></g>
  </g>
</g>
```
{% endcol %}
{% endrow %}