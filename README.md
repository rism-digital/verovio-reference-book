[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

# Reference book for Verovio

This is the repository for the [Reference book](https://book.verovio.org) for the Verovio engraving library. Contributions to this book are very welcome. These can be minor corrections, additions to a section or more. Contributions should be submitted as pull-requests to the `master` (default) branch of this repository.

## Structure and syntax

The book is a Jekyll site written in Markdown. The text content of the book is in the [_book](./_book) folder of this repository.

Each chapter of the book is composed of directory. The chapter directory contains at least a chapter file in Markdown `00-index.md`. This file needs to exist. Its front matter must include the title of the chapter and (optionally) of its first section:
```yaml
---
chapter-title: "Introduction"
title: "About Verovio"
---
```
When there is no need to have an introduction text for the chapter, the title of the first section in the frontmatter can be ommitted and replaced by `redirect_to_section: true`. The link to the chapter in the table of content will redirect directly to its first section.

The content of a chapter is a list of files, one per section. Chapter and section file names have to be prefixed with a `dd-` numbering that determines their order in the book.

Subsections in a section are `h3` headings (`###` in Markdown) in the text. Text paragraphs should not have hard wraps to help cut down on the size of the diffs that appear when changes are made, making changes easier to review.

### Branches

This repository has three main branches:
* master, that holds the content for the latest release of Verovio
* develop, that holds all changes currently documenting features that are not available in the current version of Verovio
* gh-pages, that contains a build of master

PR for changes should be made to the master branch for edits applying to the latest release of Verovio and to develop (only) for edits applying striclty to new features or changes to the develop version of Verovio. The develop branch is merge to master for each release (major or minor one) of Verovio.

## Build the book locally

You can build the site locally following a [standard Jekyll installation procedure](https://jekyllrb.com/docs/step-by-step/01-setup/#build). This is recommended if you want to submit more significant changes than a small correction or addition to an existing text.

## Adding a subsection or a section

The table of content (i.e., the navigation sidebar) is built from the content. Adding a subsection only requires a `###` heading to be added in the section text at the right place.

Adding a section requires a section file to be added following the file structure described above. If the section needs to be inserted in-between exsisting sections, then the files of following sections needs to be renumbered accordingly.

## Music notation examples

Music notation examples included in the book are imported from the [Verovio test suite](https://www.verovio.org/test-suite.xhmtl). They are pre-generated and included as SVG together with a snippet of the MEI code. Examples used in a page a listed in its front matter in `examples`. To include a new example, you need to proceed as follow.

### Add examples

Examples need to be listed in the front matter of the page where they need to be included. The list should be given in the `examples` entry in the frontmatter. For example:
```yaml
examples:
    - name: accid-003
      test-suite: accid/accid-003.mei
      xpath:
        - ".//mei:section/mei:measure[1]//mei:note[1]"
        - "[...]"
        - ".//mei:section/mei:measure[1]//mei:note[last()-1]"
```
The example entry has three values:
1. `name` is the value you will refer to when including the example within the content of the page
3. `test-suite` is MEI example in the Verovio test suite that needs to be included
4. `xpath` is an array of xpath queries to execute in order to extract the MEI snippet to be displayed with the example

For example, if you want to show in the MEI snippet the second and the third measure of the example, use:
```yaml
xpath:
  - ".//mei:section/mei:measure[2]"
  - ".//mei:section/mei:measure[3]"
```

The `xpath` array can contains the `[...]` value, which will not be executed but simply be replaced by `<!-- ... -->` in the code displayed. It can be used when the MEI snippet includes parts of the code that are not adjacent.

For including an example not in the test suite (which should be the exception), replace the example `test-suite` entry with `url` with the address where the example lives. Another possibility is to include the examples directly in the front matter with `inline`.

```yaml
examples:
    - name: abc-01
      inline: |-
        X: 99
        T:Short tune
        C:K. Rettinghaus
        M:4/4
        L:1/4
        K:G
        D|G>ABG|A>BAD|G>ABA|G3|]
```

With both `url` and `inline`, an `name` entry is required.

#### Additional options

Additional options for an example can be passed to Verovio with the `options` entry as a dictionary. For example:
```yaml
options:
    transpose: "e"
```
These options will be set *after* specific options set in the header of the test-suite example and overwrite them.

### Add the example in the text

In the text of the page, the example can then be included with the templates `music-notation`. It takes a `example` parameter referring to its `name`. For the example above, it will look like:
```md
{% include music-notation example="accid-003" %}
```

For an example without showing MEI snippet, do:
```md
{% include music-notation-only example="accid-003" %}
```

### Generate the examples

For the example to properly display, You need to:
1. Generate the Jekyll site - this will update the `scripts/examples.yml` file that contains all the examples in the book
2. Run the script `scripts/generate-examples.py`

The Python script will generate the SVG and extract the MEI snippet for each example. The packages required can all be install with `pip`, including `verovio`.

The script has to be run from the site root directory with the command
```bash
python scripts/generate-examples.py
```

## Documenting methods

The method documentation is generated from the Verovio codebase through its [Doxygen documentation](https://github.com/rism-digital/verovio-doxygen).

To update the documentation, you need to run:
```bash
python scripts/generate-methods.py release
```

Note that it will generate the documentation for the latest release of Verovio. For the documentation of the develop version, run:
```bash
python scripts/generate-methods.py develop
```

### Include extended documentation for specific methods

Extended documentation for specific methods can be added in `./_includes/methods/`. The name of the file has to be the lower case method name togehter with the lower case parameter names (if any), separated with `-`. For example, `./_includes/methods/getelementattr-xmlid.md` provides extended documentation for `GetElementAttr(xmlId)`.

## Documenting options

The option documentation is generated from the Verovio codebase. To update the documentation, you need to run:
```bash
python scripts/generate-options.py
```

Note that it will generate the option documentation for the Python version currently installed on your machine.

### Include extended documentation for specific options

Extended documentation for specific options can be added in `_includes/options/` directory. They need to be listed in the directory corresponding to their group and in the filename corresponding to the JSON option name. For example, `./_includes/options/0-base/version.md` provides extended documentation for the `--version` option.

Once added, the option documentation needs to be re-generated in order for the extended documentation to appear.

### Add "See also" links to options

Links through "See also" references for options have to be added to the frontmatter of the `_book/05-toolkit-reference/04-toolkit-option.md` file. For example:
```md
see-also:
    inputFrom:
      - "/toolkit-reference/input-formats.html"
```

## Documenting MEI support

The MEI support documentation is also generated from the Verovio codebase through its [Doxygen documentation](https://github.com/rism-digital/verovio-doxygen).

To update the MEI support documentation, you need to run:
```bash
python scripts/generate-mei-support.py release
```

Note that it will generate the documentation for the latest release of Verovio. For the documentation of the develop version, run:
```bash
python scripts/generate-mei-support.py develop
```

## License

The content of the repo is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
