---
title: "Generate code with libMEI"
---

Verovio uses a forked version of [LibMEI](https://github.com/DDMAL/libmei), a library that generates code directly from the MEI schema. It can be adapted to generate code in any language. For Verovio, it is used to generate C++ code. The code generated with LibMEI is included in the Verovio repository in the `./libmei` directory and the LibMEI repository does not need to be cloned for building Verovio.

Whenever the MEI schema is modified, this code needs to be re-generated in order to integrate these changes. However, since Verovio implements only a small subset of the MEI schema, this really needs to be done only for the changes in the schema that touch features supported by Verovio. This means that the code within the `./libmei/dist` directory should never be edited by hand because any change will be overwritten by the LibMEI output when the code generated from the schema needs to be updated and LibMEI is run again.

### Generating LibMEI

You can regenerate the LibMEI code with a compiled ODD as input.

Go to the `./libmei` directory and run:

```bash
python tools/parseschema2.py -c config.yml ./mei/develop/mei-verovio_compiled.odd
```

### Customization

Verovio currently uses an MEI customization that has added or modified a few elements. It is defined in the file `./libmei/mei/develop/mei-verovio.xml`. If you want to make changes to it, you can make them there. You will need to regenerate the ODD file `./libmei/mei/develop/mei-verovio_compiled.odd`. This can be done with the Edirom [MEI Garage](https://meigarage.edirom.de/). Alternatively, you can also use the MEI command line script. To do so, you need to create a clone of the [MEI](https://github.com/music-encoding/music-encoding) repository, copy your customization file (e.g., `mei-verovio.xml`) into it and do:

```bash
ant init
ant -lib lib/saxon/saxon9he.jar -Dcustomization.path=mei-verovio.xml
```

The ODD file will be written to `./dist/schemata/mei-verovio_compiled.odd`, which you can use as new input file for LibMEI.
