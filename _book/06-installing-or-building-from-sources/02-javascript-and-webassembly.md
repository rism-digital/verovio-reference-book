---
title: "JavaScript and WebAssembly"
---

### Pre-build versions

The verovio.org [GitHub repository](https://github.com/rism-digital/verovio.org) provides compiled versions of the JavaScript toolkit. The toolkit is available in three options. The recommended version is one built as [WebAssembly](https://webassembly.org/) because it is the fastest and supported by [all recent browsers](https://caniuse.com/wasm). To use it, the file you need to include is:

**`verovio-toolkit-wasm.js`**

If you need Humdrum support, the file to include is:

**`verovio-toolkit-hum.js`**

If you need to have support for old browsers, there is an `asm.js` version available. This version is obsolete and is not recommended for new projects. The file to include is:

**`verovio-toolkit.js`**

A build for the development version of the `verovio-toolkit-wasm.js` is available through CI, as well as for each [release](https://github.com/rism-digital/verovio/releases) for the Humdrum and the legacy `asm.js` version.

The latest release is always available from:
```
https://www.verovio.org/javascript/latest/verovio-toolkit-wasm.js
```

The latest development version is available from:

```
https://www.verovio.org/javascript/develop/verovio-toolkit-wasm.js
```

Previous releases are available from their corresponding directory, e.g.:

```
https://www.verovio.org/javascript/2.7.1/verovio-toolkit-wasm.js
```

For instructions on a basic usage of the JavaScript version of the toolkit, see the [Getting started](/first-steps/getting-started.html) section of the [Tutorial 1: First steps](/first-steps/) chapter.

### NPM

{% comment %}
***********************************************************************************
This section has to be kept in sync with
https://github.com/rism-digital/verovio/blob/develop/emscripten/npm/README.md
***********************************************************************************
{% endcomment %}

The latest stable version is available via [NPM](https://www.npmjs.com/package/verovio) registry. The version distributed via NPM it the WebAssembly build. It can be installed with:

```bash
npm install verovio
```

The homepage of the Verovio package includes [documentation](https://www.npmjs.com/package/verovio#usage) on how to use it.

#### Basic usage with NPM

```js
const verovio = require('verovio');
const fs = require('fs');

/* Wait for verovio to load */
verovio.module.onRuntimeInitialized = function ()
{
    // create the toolkit instance
    const vrvToolkit = new verovio.toolkit();
    // read the MEI file
    mei = fs.readFileSync('hello.mei');
    // load the MEI data as string into the toolkit
    vrvToolkit.loadData(mei.toString());
    // render the fist page as SVG
    svg = vrvToolkit.renderToSVG(1, {});
    // save the SVG into a file
    fs.writeFileSync('hello.svg', svg);
}
```


#### Usage with ESM

Since version 3.11.0 there is an ESM compatible version of the *npm* package with a modularized build of the Verovio module. This is because we need to wait for the asynchronous module to be ready for usage, and this is now [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) based instead of using the `onRuntimeInitialized` callback function.

 Use `.mjs` as file extension when using this directly in Node.js or set `"type": "module"` in your `package.json`.

```js
import createVerovioModule from 'verovio/wasm';
import { VerovioToolkit } from 'verovio/esm';
import fs from 'node:fs';

createVerovioModule().then(VerovioModule => {
   const verovioToolkit = new VerovioToolkit(VerovioModule);
   const score = fs.readFileSync('hello.mei').toString();
   verovioToolkit.loadData(score);
   const data = verovioToolkit.renderToSVG(1, {});
   console.log(data);
});
```

This is the recommended way to use Verovio when creating a website or web app with bundlers like webpack or Vite or when using JavaScript frameworks like React or Vue.js.

#### Usage with CommonJS

Alternatively this package also exports a version compatible with CommonJS

```js
const createVerovioModule = require('verovio/wasm');
const { VerovioToolkit } = require('verovio/esm');
```

#### Humdrum support

Since version 3.11.0 the NPM package provides an additional module with Humdrum support:

```js
import createVerovioModule from 'verovio/wasm-hum';
```

### Building the toolkit

To build the JavaScript toolkit you need to have the <a href="http://www.emscripten.org" target="_blank">Emscripten</a> compiler installed on your machine. You also need [CMake](https://cmake.org). You need to run:

```bash
cd emscripten
./buildToolkit -H
```

The toolkit will be written to:

```bash
./emscripten/build/verovio-toolkit.js
```

Building without `-H` will include the Humdrum support, which increases the size of the toolkit by about one third. In that case, the output will be written to `verovio-toolkit-hum.js`.

If you are building with another option set than previously, or if you want to regenerate the makefiles, add the option `-M`.
