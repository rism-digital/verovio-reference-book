---
title: "Adding SMuFL glyphs"
---

All SMuFL glyphs used by Verovio have to be available in the [Leipzig](https://github.com/rism-digital/leipzig) font. For adding support for a new SMuFL glyph, the steps are:

1. Add the glyph to the Leipzig font file
2. Generate the Leipzig in various format and the metadata with the script available in [Leipzig](https://github.com/rism-digital/leipzig) repository
3. Add the glyph to the list of supported glyph in the XML list and re-generate the fonts.

Make sure you always add glyphs **only** in the [Leipzig](https://github.com/rism-digital/leipzig) font. Because conflict solving is quickly very when adding a glyph (in particular with the binary font files), make sure you always pull the latest version of the font file branch before starting your work and do not wait too long before making a PR. If changes have been made in between, you will need to add your glyphs again.

When making a PR, always add an image (e.g., screenshot of FontForge) showing the glyphs.

#### Adding the glyph to the Leipzig font file

The file to modify is `./Leipzig.sfd` and should be edited with [FontForge](https://fontforge.org/). Very often it is possible to copy another existing glyph as basis for the new glyph. Leipzig is visually lighter and thinner than Bravura and new glyphs have to follow this design choice. **Do not simply copy glyphs from Bravura.** Make sure the font is valid by running "Element => "Find Problems...".

Once the new glyph(s) has/have been added, you also need to change the version number in the font info (menu "Element" => "Font Info" and then tab "PS Names" in fields "Version" and "Copyright" and tab "FONTLOG" where you also need to add a comment together with the version number. The file can be saved.

#### Generate other font formats and the metadata

Once the `./Leipzig.sfd` has been modify and saved, you have to run the `./generate_font.py` script that will generate different font formats and the metadata. You are now ready to make a PR to the [Leipzig](https://github.com/rism-digital/leipzig) repository.

#### Add the glyph to the list of supported glyph in the XML list and re-generate the fonts

Once the PR to the [Leipzig](https://github.com/rism-digital/leipzig) repository has been approved and merged, the new glyphs have to be added to the Verovio codebase. The first thing to do is to add them to the list of glyphs supported by Verovio.

Open the file `./fonts/supported.xml` and uncomment the glyph(s) you added to Leipzig. The XML file is then used to extract the glyphs supported by Verovio.

To do so, you need to copy to `./fonts/Leipzig` the new Leipzig files:
* `Leipzig.woff2`
* `Leipzig.ttf`
* `Leipzig.svg`
* `leipzig_metadata.json`

The glyphs will be extracted from the SVG font by running the script `./fonts/generate_all.sh` (from `./fonts/`). This will extract all the glyphs from the SVG font file and calculate the their bounding boxes. When this is done you will see your glyphs in `./data/` and in `./include/vrv/smufl.h`. The CSS font files will also be updated.

When using a custom FontForge binary (e.g. latest [AppImage](https://fontforge.org/en-US/downloads/gnulinux-dl/)) the specific location needs to be provided to `generate.py` via the `--fontforge <path-to-fontforge-binary>` command line argument. When using `generate_all.sh`, all command line arguments are passed on to the python scripts.

Example: `./generate_all.sh --fontforge /mnt/linux-data/henry/Apps/FontForge-2023-01-01-a1dad3e-x86_64.AppImage`
