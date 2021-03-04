# Reference book for Verovio

This is the repository for the Reference book for the Verovio engraving library. Contributions to this book are very welcome. These can be minor corrections, additions to a section or more. Contributions should be submitted as pull-requests to the `master` (default) branch of this repository.

## Structure and syntax

The book is a Jekyll site written in Markdown. The text content of the book is in the [_book](./_book) folder of this repository.

Each chapter of the book is composed of a Markdown file a corresponding directory with its content. The name of the directory of the content of a chapter has to be exactly the name of the chapter file (without the `.md` extension).

The content of a chapter is a list of files, one per section. Chapters and section file names have to be prefixed with a `dd-` numbering that determines their order in the book.

Subsections in a section are `h3` headings (`###` in Markdown) in the text. Text paragraphs have not hard wraps.

## Build the book locally

You build the site locally following a standard Jekyll installation procedure. This is recommended if you want to submit more significant changes than a small correction or addition to an existing text.

## Adding a subsection or a section

The table of content (i.e., the navigation sidebar) is built from the content. Adding a subsection only requires a `###` heading to be added in the section text at the right place.

Adding a section requires a section file to be added following the file structure described above. If the section needs to be inserted in-between exsisting sections, then the files of following sections needs to be renumbered accordingly.

## Adding a music notation example

TODO
