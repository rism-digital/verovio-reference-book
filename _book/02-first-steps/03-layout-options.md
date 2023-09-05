---
title: "Layout options"
---

Now that we have successfully rendered an MEI file to a web page, we can start to explore how to customize the SVG output. There are [many possible options](/toolkit-reference/toolkit-options.html), most of which you will never need.

To start, we will first try and reduce the size of the image output, to demonstrate how we can scale the music notation to fit the screen.

### Passing options to Verovio

Passing options to Verovio is as easy as creating a set of key and value pairs, and using the `setOptions` method on the toolkit. To scale the output we will use the `scale` option given as percentage of the normal (100) output. Add the following to your page, after we have instantiated the toolkit but before we render the data:

```js
tk.setOptions({
  scale: 30
});
```

When you refresh your page, you should see your score scaled to 30% of its original size. Try experimenting with other values to see their effects! (Hint: you can use sizes above 100%.)

### Defaults

All of the options have default values. You can use the `getOptions` method to view the list of all the options and their default values. We will use the browser console to explore these defaults. Add the following line:

```js
console.log("Verovio options:", tk.getOptions());
// for the default values
console.log("Verovio options:", tk.getDefaultOptions());
```

When you refresh your page and open your browser's console you should see the text "Verovio options:" followed by a small disclosure triangle. Clicking this triangle will produce a long list of options that you can pass to `setOptions`. Let's try a few more.

### Change the page orientation

You may have noticed that, by default, Verovio renders the score in "portrait" orientation; that is, the width of the score is shorter than the length. To change this, we can use the `landscape` and `adjustPageWidth` options:

```js
tk.setOptions({
  scale: 30,
  landscape: true,
  adjustPageWidth: true
});
```

When you refresh the page you should notice that your SVG has changed orientation! But wait... the score is now cut off! Where did the rest of it go?

It turns out that Verovio has the ability to split scores into "pages" automatically. When it calculates the notation cannot fit on the current page, Verovio will automatically push it to the next page. Adjusting the different options will have an effect on this calculation, so it is worth looking through the options that we printed out, and trying some on your own. You may wish to change the `pageWidth` option, for example, to a bigger or smaller value and see what the result is.

### End of Section 3

In this section we have explored Verovio's default options, and looked at how to adjust them to change the rendering output. In the next section we will look at how we can adjust these options dynamically, using on-screen controls to provide a user interface for building interactive music notation displays.

#### Full example

```html
<html>
  <head>
    <script src="https://www.verovio.org/javascript/latest/verovio-toolkit-wasm.js" defer></script>
    <script>
      document.addEventListener("DOMContentLoaded", (event) => {
          verovio.module.onRuntimeInitialized = async _ => {
            let tk = new verovio.toolkit();
            console.log("Verovio has loaded!");
            tk.setOptions({
              scale: 30,
              landscape: true,
              adjustPageWidth: true
            });
            console.log("Verovio options:", tk.getOptions());

            fetch("https://www.verovio.org/examples/downloads/Schubert_Lindenbaum.mei")
              .then( (response) => response.text() )
              .then( (meiXML) => {
                let svg = tk.renderData(meiXML, {});
                document.getElementById("notation").innerHTML = svg;
              });
          }
      });
    </script>
  </head>
  <body>
    <h1>Hello Verovio!</h1>
    <div id="notation"></div>
  </body>
</html>
```
