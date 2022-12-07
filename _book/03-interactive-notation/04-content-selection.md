---
title: "Score content selection"
---

Verovio can extract segments of a score and display only these segments. This can be useful if you have a larger score and want to display a segment in a webpage to highlight a particular segment or portion. This can also be combined with the techniques from the previous tutorials, so you can also highlight or even play back these segments using MIDI. 

### Selecting parts of a score

Verovio has a `select` method available on the toolkit. This method takes a JSON object where you can specify a range of measures in the format "[first]-[last]". The selection syntax is based on a subset of the `measureRange` syntax from the [Enhancing Music Notation Addressability API](https://github.com/music-addressability/ema/blob/master/docs/api.md). The difference is that Verovio only supports a single measure range. For example:

```js
tk.select({measureRange: "1-10"});
```

Once the measures have been selected, calls to render the score to SVG will render only that selected portion. Importantly, it will also reduce the number of "pages" that are available to only the number that are needed to represent the selection.

You can clear a selection by passing in an empty JSON Object:

```js
tk.select({});
```

You can also select the entire score by using `start` and `end`:

```js
tk.select({measureRange: "start-end"});
```

### Full example

Open [this example](/tutorials/content-selection.html){:target="_blank"} in a new window.

```html
{% include tutorials/content-selection.html %}
```
