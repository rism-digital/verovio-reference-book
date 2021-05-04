---
title: "Adding SMuFL glyphs"
---

All SMuFL glyphs used by Verovio have to be available in the [Leipzig](https://github.com/rism-digital/leipzig) font. For adding support for a new SMuFL glyph, the steps are:

1. Add the glyph to the Leipzig font file
2. Generate the Leipzig font as SVG font
3. Add the glyph to the list of supported glyph in the XSL list

Make sure you always add glyphs **only** in the develop-leipzig branch because conflict solving is problematic with the process of adding a glyph, in particular for the Leipzig font file. For this reason, make sure you always pull the latest version from the develop-leipzig branch before starting your work and do not wait too long before making a PR. If changes have been made in between, you will need to add your glyphs again.

When making a PR, always add an image (e.g., screenshot of FontForge) showing the glyphs.

#### Adding the glyph to the Leipzig font file

The file is `./fonts/Leipzig-5.2.sfd` and should be edited with [FontForge](https://fontforge.org/). Very often it is possible to copy another existing glyph as basis for the new glyph. Leipzig is visually lighter and thinner than Bravura and new glyphs have to follow this design choice. Do not copy glyphs from Bravura. Make sure the font is valid by running "Element => "Find Problems...".

Once the new glyph(s) has/have been added, you also need to change the version number in the font info (menu "Element" => "Font Info" and then tab "PS Names" in fields "Version" and "Copyright" and tab "Comment" where you also need to add a comment together with the version number. The file can be saved.

#### Generate the Leipzig font as SVG font

From FontForge, export the with menu "File" => "Generate Fonts..." and select "SVG font" (option "validate before saving" can be turned off). The file needs to be written to `./fonts/Leipzig.svg`.

#### Add the glyph to the list of supported glyph in the XSL list

Open the file `./fonts/supported.xsl` and uncomment the glyph(s) you added to Leipzig. The XSL file is then used to extract the glyphs supported by Verovio

#### Make a PR to the develop-leipzig branch

Once the PR will have been merged, the glyphs will be extracted from the SVG font by running the script `./fonts/generate_all.sh` (from `./fonts/`). This will extract all the glyphs from the SVG font file and calculate the their bounding boxes. When this is done you will see your glyphs in `./data/` and in `./include/vrv/smufl.h`
