[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

# Reference book for Verovio

This is the repository for the Reference book for the Verovio engraving library. Contributions to this book are very welcome. These can be minor corrections, additions to a section or more. Contributions should be submitted as pull-requests to the `master` (default) branch of this repository.

## Structure and syntax

The book is a Jekyll site written in Markdown. The text content of the book is in the [_book](./_book) folder of this repository.

Each chapter of the book is composed of a Markdown file and a corresponding directory with its sections. The chapter file can have not text but has to exist. The name of the content directory of a chapter is exactly the name of the chapter file (without the `.md` extension). This needs to be maintained.

The content of a chapter is a list of files, one per section. Chapter and section file names have to be prefixed with a `dd-` numbering that determines their order in the book.

Subsections in a section are `h3` headings (`###` in Markdown) in the text. Text paragraphs should not have hard wraps to help cut down on the size of the diffs that appear when changes are made, making changes easier to review.

## Build the book locally

You can build the site locally following a standard Jekyll installation procedure. This is recommended if you want to submit more significant changes than a small correction or addition to an existing text.

## Adding a subsection or a section

The table of content (i.e., the navigation sidebar) is built from the content. Adding a subsection only requires a `###` heading to be added in the section text at the right place.

Adding a section requires a section file to be added following the file structure described above. If the section needs to be inserted in-between exsisting sections, then the files of following sections needs to be renumbered accordingly.

## Adding a music notation examples

Music notation examples included in the book are imported from the [Verovio test suite](https://www.verovio.org/test-suite.xhmtl). They are pre-generated and included as SVG together with a snippet of the MEI code. Examples used in a page a listed in its front matter in `examples`. To include a new example, you need to proceed as follow.

### Add the example in the front matter

In the front matter of the page where you want to include the example, add it in `examples`. For example:
```yaml
examples:
    - name: accid-003
      url: https://raw.githubusercontent.com/rism-digital/verovio.org/gh-pages/_tests/accid/accid-003.mei
      xpath:
        - ".//mei:section/mei:measure[1]//mei:note[1]"
        - "[...]"
        - ".//mei:section/mei:measure[1]//mei:note[last()-1]"
```
The example entry has three values:
1. `name` is the value you will refer to when including the example within the content of the page
2. `url` is the address of the MEI example in the Verovio test suite that needs to be included
3. `xpath` is an array of xpath queries to execute in order to extract the MEI snippet to be displayed with the example

For example, if you want to show in the MEI snippet the second and the third measure of the example, use:
```yaml
xpath:
  - ".//mei:section/mei:measure[2]"
  - ".//mei:section/mei:measure[3]"
```

The `xpath` array can contains the `[...]` value, which will not be executed but simply be replaced by `<!-- ... --->` in the code displayed. It can be used when the MEI snippet includes parts of the code that are not adjacent.

### Add the example in the text

In the text of the page, the example can then be included with the templates `music-notation`. It takes a `example` parameter referring to its `name`. For the example above, it will look like:
```md
{% include music-notation example="accid-003" %}
```

### Generate the examples

For the example to properly display, You need to:
1. Generate the Jekyll site - this will update the `scripts/examples.yml` file that contains all the examples in the book
2. Run the script `scripts/generate-examples.py`

The Python script will generate the SVG and extract the MEI snippet for each example. The following packages are required and can all be install with `pip`:
* verovio
* wget
* ...
* ...

The script has to be run from the site root directory with the command
```bash
python scripts/generate-examples.py
```

## License

The content of the repo is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
