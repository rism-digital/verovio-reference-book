---
title: "Interacting with editorial markup"
---

MEI has a feature that lets us encode variant "readings" of a musical text. These readings may come from different sources of the same piece. A common type of alternate reading is a "contrafactum", or alternate text. Typically this might occur between a Latin sacred text and a secular text in a vernacular, such as English, both set to the same music.

Verovio supports the selection of variant readings encoded with MEI `<app>`, containing `<lem>` and `<rdg>` elements. Only one variant can be displayed at a time, and this is selected when the file is loaded. By default, Verovio selects the `<lem>` (or the first `<rdg>` if no `<lem>` is provided).

In this example we are going to create a basic interface to switch between variants by applying XPath queries for selecting specific readings, and then highlight the editorial markup in different colours. The MEI file we will use for this purpose comes from the Marenzio edition:

```
https://raw.githubusercontent.com/marenzio/marenzio.github.io/master/mei/M-04-6/M_04_6_02_Di_nettare_amoroso_ebro_la_mente.mei
```

### Selection with an xpath query

The first thing we need is a variable to store the XPath queries. This must be an array, but we can start with an empty one, which applies the default behaviour:

```js
let appXPath = [];
```

Since Verovio selects the elements to be displayed when loading the file, we need to define a `loadFile()` function that applies the options, loads the file into Verovio, and renders it:

```js
// A function that loads a file
function loadFile() {
  fetch("https://raw.githubusercontent.com/marenzio/marenzio.github.io/master/mei/M-04-6/M_04_6_02_Di_nettare_amoroso_ebro_la_mente.mei")
    .then((response) => response.text())
    .then((meiXML) => {
      tk.setOptions({
        pageWidth: document.body.clientWidth,
        pageHeight: document.body.clientHeight,
        scale: 50,
        scaleToPageSize: true,
        appXPathQuery: appXPath
      });
      tk.loadData(meiXML);
      notationElement.innerHTML = tk.renderToSVG(currentPage);
    });
}
```

To load, or reload, the file we can now call the function:

```js
loadFile();
```

In the CSS file we also have defined two rules:

```css
g.lem {
  fill: darkcyan;
}
g.rdg {
  fill: crimson;
}
```

At this stage, because we have a `editorial-markup.css` with some rule highlighting for `lem` and `rdg` classes, the default `<lem>` should appear highlighted.

### Switching between readings

To switch between the original and a reading (an English contrafactum text, in this case), we add two buttons, with two handlers that bind to the button event listeners:

```html
<button id="original">Original</button>
<button id="contrafactum">Contrafactum</button>
```

```js
const originalHandler = function () {
  // Do something to render the original
}

const contrafactumHandler = function () {
 // Do something to render the contrafactum
}

document.getElementById("original").addEventListener("click", originalHandler);
document.getElementById("contrafactum").addEventListener("click", contrafactumHandler);
```

The file example we are using has some readings encoded as follows:

```xml
<app>
  <lem source="Italian">
    <verse>
      <syl>Di</syl>
    </verse>
  </lem>
  <rdg source="English">
    <verse>
      <syl>When</syl>
    </verse>
  </rdg>
</app>
```

To select the "English" reading (i.e., in the `contrafactumHandler`), we can write an xPath query selecting `<rdg>` elements with the corresponding `@source` value, in this case "English", and then reload the file:

```js
appXPath = ["./rdg[@source='English']"];
loadFile();
```

For the original, we can reset Verovio by passing in an empty `appXPath` array:

```js
appXPath = [];
loadFile();
```

When switching between the views you will notice that the colour of the text differs between the original `<lem>` and the English `<rdg>`. 

### Full example

Open [this example](/tutorials/editorial-markup.html){:target="_blank"} in a new window.

```html
{% include tutorials/editorial-markup.html %}
```
