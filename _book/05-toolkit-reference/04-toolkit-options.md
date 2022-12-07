---
title: "Toolkit options"

# If an option is documented in a section, add the link here
# The script scripts/generate-options.py needs to be run for the links to be updated
see-also:
    font:
      - "/advanced-topics/smufl.html"
    inputFrom:
      - "/toolkit-reference/input-formats.html"
    logLevel:
      - "/toolkit-reference/environment-functions.html"
    mensuralToMeasure:
      - "/advanced-topics/mensural-notation.html#ligatures"
      - "/advanced-topics/mensural-notation.html#layout"
    outputTo:
      - "/toolkit-reference/output-formats.html"
    transpose:
      - "/advanced-topics/transposition.html"
    pageHeight:
      - "/advanced-topics/controlling-the-svg-output.html"
    pageWidth:
      - "/advanced-topics/controlling-the-svg-output.html"
    resourcePath:
      - "/toolkit-reference/toolkit-methods.html#setresourcepath"
      - "/toolkit-reference/environment-functions.html"
      - "/installing-or-building-from-sources/python.html#resources-for-versions-built-locally"
    scale:
      - "/advanced-topics/controlling-the-svg-output.html#scaling"
    scaleToPageSize:
      - "/advanced-topics/controlling-the-svg-output.html#scaling"
    smuflTextFont:
      - "/advanced-topics/smufl.html#music-symbols-in-text"
    unit:
      - "/advanced-topics/controlling-the-svg-output.html#units-and-page-dimensions"   
      - "/advanced-topics/controlling-the-svg-output.html#scaling"   
---

<div class="hidden-print radio-inline">
  <label><input type="radio" name="lang" checked>Command-line parameters</label>
</div>
<div class="hidden-print radio-inline">
  <label><input type="radio" name="lang">JavaScript/Python options</label>
</div>

For the Python toolkit, options have to be passed as [stringified JSON objects](/installing-or-building-from-sources/python.html#basic-usage-of-the-toolkit). For the JavaScript toolkit, they have to be passed as [JSON objects](/first-steps/layout-options.html#passing-options-to-verovio) directly.

### Base short options

All of the base options are short options in the command-line version of the toolkit. Most of them are command-line only and are not used in the JavaScript or Python toolkits.

{% include options/0-base.md %}

### Input and page layout options

{% include options/1-general.md %}

### General layout options

{% include options/2-generalLayout.md %}

### Element selectors and processing

{% include options/3-selectors.md %}

### Element margins

{% include options/4-elementMargins.md %}

<script type="text/javascript">
$('input:radio[name="lang"]').click(function() {
    $("span").toggleClass("lang1 lang2");
});
</script>
