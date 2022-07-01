---
title: "Usage with npm"
---

The latest stable version is available in the *npm* registry. The version distributed via *npm* is the WebAssembly build. It can be installed with: 

```bash
npm install verovio
```

## Basic usage

```javascript
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


## Usage with ESM

Since version 3.11.0 there is an ESM compatible version of the *npm* package with a modularized build of the Verovio module, that needs a slightly different setup to wait for the asynchronous Emscripten module to be ready for usage which is now [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) based instead of using the `onRuntimeInitialized` callback function.

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


## Usage with CommonJS

Alternatively this package also exports a version compatible with CommonJS

```js
const createVerovioModule = require('verovio/wasm');
const { VerovioToolkit } = require('verovio/esm');
```


# Humdrum support

Since version 3.11.0 the *npm* package provides an additional module with Humdrum support:

```js
import createVerovioModule from 'verovio/wasm-hum';
```

