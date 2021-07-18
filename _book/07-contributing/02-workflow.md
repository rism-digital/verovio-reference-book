---
title: "Contributing workflow"
---

### Adding examples to the test-suite

When adding examples to the test-suite, you should keep in mind the following points:
* The example should be as minimal as possible, ideally one or two measures and without un-related MEI / notation features
* The example has to be valid MEI (4.0 or 5.0-dev)
* The header should follow the test-suite style
* The XML should be indented with 3-spaces
* It is not mandatory to have an @xml:id on all MEI elements
* The file name should follow the test-suite style

#### Example header

Example MEI header for a test-suite example:
```xml
<meiHead>
    <fileDesc>
        <titleStmt>
        <title>Slur position with cross-staff</title>
        <respStmt>
            <persName role="editor">Laurent Pugin</persName>
            <persName role="encoder">Craig Sapp</persName>
        </respStmt>
        </titleStmt>
        <pubStmt>
        <date isodate="2021-01-06">2021-01-06</date>
        <pubPlace>
            <ref target="https://github.com/rism-digital/verovio/issues/1898" />
        </pubPlace>
        </pubStmt>
        <notesStmt>
        <annot>Slurs with cross-staff should be place identically as in normal situations.</annot>
        </notesStmt>
    </fileDesc>
    <encodingDesc>
        <appInfo>
        <application version="3.1.0" label="2">
            <name>Verovio</name>
        </application>
        </appInfo>
    </encodingDesc>
</meiHead>
```

#### File names

The test suite examples are grouped by element name, with a very few exceptions. There is a corresponding folder name in the [test suite folder](https://github.com/rism-digital/verovio.org/_tests/). A test-suite example should be saved in the folder corresponding to the MEI element it targets. File names also use the element name and are numbered using the three digits (`-001.mei`) pattern.

#### Additional options

In some cases, a test suite example can require specific Verovio options to be set for it to make sense. For instance, it can require a specific layout or spacing parameter, or a specific font. The options can be set in the header of the MEI file as JSON object encoded as `CDATA` in the `<extMeta>` tag. 

For example, setting the Bravura font can be triggered by including the following tag in the header of the test suite example:

```xml
<extMeta><[CDATA[{ "font": "Bravura" }]]></extMeta>
```

{% aside .warning %}
The additional options set in the MEI header are taken into account in both the test-suite page and the test-suite evaluation performed by the GitHub Actions. However, they currently remain ignored in the Verovio Editor.
{% endaside %}
