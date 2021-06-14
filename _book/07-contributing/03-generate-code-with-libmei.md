---
title: "Generate code with libMEI"
---

Verovio uses a [forked version](https://github.com/rism-digital/libmei) of [LibMEI](https://github.com/DDMAL/libmei), a library that generates code directly from the MEI schema. It can be adapted to generate code in any language. For Verovio, it is used to generate C++ code. The code generated with LibMEI is included in the Verovio repository in the `./libmei` directory and the LibMEI repository does not need to be cloned for building Verovio.

Whenever the MEI schema is modified, this code needs to be re-generated in order to integrate these changes. However, since Verovio implements only a small subset of the MEI schema, this really needs to be done only for the changes in the schema that touch features supported by Verovio. This means that the code within the `./libmei` directory should never be edited by hand because any change will be overwritten by the LibMEI output when the code generated from the schema needs to be updated and LibMEI is run again.

### Running LibMEI

In order to update to code generated with LibMEI, you need to clone the [forked version](https://github.com/rism-digital/libmei) of LibMEI.

LibMEI takes a compiled ODD as input. You need to run, from the LibMEI directory:

```bash
python tools/parseschema2.py -l vrv -o /path/to/the/verovio/directory -i tools/includes/vrv mei/dev/mei-verovio_compiled.odd
```

You need to set to option `-o` to point to the Verovio directory where the `./libmei` files will be written.

### Customization

Verovio currently uses an MEI customization that adds or modified a few elements. It is defined in the `./mei/dev/mei-verovio.xml` file. If you want to makes changes to it, you can make them there. You will need to re-generate the `./mei/dev/mei-verovio_compiled.odd` ODD file. This can be done using the Edirom [MEI Garage](https://meigarage.edirom.de/). Alternatively, you can also use the MEI command-line script. To do so, you will need to a clone of the [MEI](https://github.com/music-encoding/music-encoding) repository, copy your customization file (e.g., `mei-verovio.xml`) into it and do:

```bash
ant init
ant -lib lib/saxon/saxon9he.jar -Dcustomization.path=mei-verovio.xml
```

The ODD file will be written to `./dist/schemata/mei-verovio_compiled.odd`, which you can use as new input file for LibMEI.
