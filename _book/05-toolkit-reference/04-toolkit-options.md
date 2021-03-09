---
title: "Toolkit options"
---

<div class="radio-inline">
  <label><input type="radio" name="lang" checked>Command-line</label>
</div>
<div class="radio-inline">
  <label><input type="radio" name="lang">JSON</label>
</div>

### Input and page layout options

{% include options/1-general.md %}

### General layout options

{% include options/2-generalLayout.md %}

### Element selectors and processing

{% include options/3-selectors.md %}

### Element margins

{% include options/4-elementMargins.md %}

### Deprecated options

{% include options/Deprecated.md %}

<script type="text/javascript">
$('input:radio[name="lang"]').click(function() {
    $("span").toggleClass("lang1 lang2");
});
</script>

