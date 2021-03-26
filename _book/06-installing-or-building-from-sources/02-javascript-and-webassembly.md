---
title: "JavaScript and WebAssembly"
---

### Pre-build versions

The verovio.org [GitHub repository](https://github.com/rism-digital/verovio.org) provides compiled versions of the JavaScript toolkit. The toolkit is available in three options.
1. **verovio-toolkit.js** - in JavaScript (more precisely in [asm.js](https://asmjs.org))
2. **verovio-toolkit-wasm.js** – in [WebAssembly](https://webassembly.org/)
3. **verovio-toolkit-hum.js** – in JavaScript with the Humdrum support

A build of each of these is provided by CI for the development version as well as for each [release](https://github.com/rism-digital/verovio/releases).

The latest release is always available from:
```
https://www.verovio.org/javascript/latest/verovio-toolkit.js
```

The latest development version is available from:
```
https://www.verovio.org/javascript/develop/verovio-toolkit.js
```

Previous releases are available from their corresponding directory, e.g.:
```
https://www.verovio.org/javascript/2.7.1/verovio-toolkit.js
```

#### NPM

The latest stable version is available via [NPM](https://www.npmjs.com/package/verovio) registry. The version distributed via NPM it the WebAssembly build. It can be installed with:
```bash
npm install verovio
```

The homepage of the Verovio package includes [documentation](https://www.npmjs.com/package/verovio#usage) on how to use it.

### Basic usage of the toolkit

For instructions on a basic usage of the JavaScript version of the toolkit, see the [Getting started](/first-steps/getting-started.html) section of the [Tutorial 1: First steps](/first-steps/) chapter.

### Building the toolkit

 To build the JavaScript toolkit you need to have the <a href="http://www.emscripten.org" target="_blank">Emscripten</a> compiler installed on your machine. You also need [CMake](https://cmake.org). You need to run:
```bash
cd emscripten
./buildToolkit -H
```
The toolkit will be written to:
```
./emscripten/build/verovio-toolkit.js
```

Building without `-H` will include the Humdrum support, which increases the size of the toolkit by about one third. In that case, the output will be written to `verovio-toolkit-hum.js`.

If you are building with another option set than previously, or if you want to regenerate the makefiles, add the option `-M`.

