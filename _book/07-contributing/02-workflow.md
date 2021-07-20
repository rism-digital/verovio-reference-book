---
title: "Contributing workflow"
---

When contributing to Verovio there are a few steps you can take to help make your contribution easy to understand and evaluate. Verovio uses the GitHub issue tracker and pull requests mechanism to organize these contributions.

These steps are:

1. Provide an short example MEI encoding that demonstrates a bug or a new feature that can be included in our test suite. You can use the [Verovio Editor](https://editor.verovio.org) to create your example. This is described in more detail below.
2. Open an [issue](https://github.com/rism-digital/verovio) describing the problem or the new feature, and attach your short example. This provides our developer community with an opportunity to provide feedback on the problem, and determine the appropriate course of action.
3. If you can also provide the solution to the problem by modifying the Verovio source code, then that will speed up the process of getting your issue fixed! If you are a first-time contributor, then please make sure you have read the [contributing guidelines](/contributing/guidelines.html). When you are ready, open a [Pull Request](https://github.com/rism-digital/verovio/pulls), making sure to reference the open issue that it solves.

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
<extMeta><![CDATA[{ "font": "Bravura" }]]></extMeta>
```

{% aside .warning %}
The additional options set in the MEI header are taken into account in both the test-suite page and the test-suite evaluation performed by the GitHub Actions. However, they currently remain ignored in the Verovio Editor.
{% endaside %}

### What to expect with an open issue

When opening an issue, you should be prepared to help shepherd it through the process of getting fixed. If it is a problem with the software itself and you do not know how to fix it, you can still help with testing any potential fixes. You can also help by improving documentation about the new feature by contributing to the Verovio book, as appropriate. **Please do not open an issue unless you are willing to help, in some way, solve it.**

If you open an issue and someone provides a fix that requires no further changes, please respond! A "thank-you" and a note to say that it fixed the problem is always appreciated. You can also close the issue so that we know it has been addressed.

Sometimes an issue may be open for several years. These issues may be particularly complex, or may have been partially but not fully fixed. They usually have a discussion attached with sample encodings. Sometimes these issues have actually been fixed later, but as part of a separate issue. If you open an issue that happens to be fixed later, you can help us by leaving a note on your issue and closing it yourself.

If you are a software developer and can provide a solution, you should mention this in your issue. **For new contributors it is useful to open issues prior to opening pull requests.** Sometimes a change cannot be accepted, so opening an issue first gives an opportunity for the more experienced members of the community to provide feedback before you invest a lot of time in it. The quickest and easiest way to get help is to reach out on the #verovio channel in the [MEI Community’s Slack chat](https://music-encoding.slack.com/). If you are not already a member, [you can join](https://join.slack.com/t/music-encoding/shared_invite/zt-4zgx6zbq-2jEjDiUT7ym3dygTaY8C0g).

**Issues that have a code contribution attached, and which have active participation from the reporter, are typically addressed first and fixed sooner.** This is largely due to the community-driven nature of the project, recognizing that the more experienced developers have their own set of priorities.  If you can provide a fix, even if it is not 100% correct, then it is easier to review your contribution and provide feedback than it is for someone else to code something from the ground up.

{% aside .info %}
If Verovio is a critically important part of your project, and you need dedicated help to make changes and contributions, the Verovio project accepts some sponsorship arrangements. Please [get in touch](mailto:info@rism.digital) to find out more about this.
{% endaside %}
