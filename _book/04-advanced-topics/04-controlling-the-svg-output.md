---
title: "Controlling the SVG output"

examples:
    - name: 01-default
      test-suite: score/score-013.mei
      options:
        breaks: 'auto'
        spacingStaff: 12
        adjustPageHeight: False
        header: 'auto'
        footer: 'auto'
        justifyVertically: True

    - name: 02-units
      test-suite: score/score-013.mei
      options:
        breaks: 'auto'
        unit: 6.0
        spacingStaff: 12
        adjustPageHeight: False
        header: 'auto'
        footer: 'auto'
        justifyVertically: True

    - name: 03-page-size
      test-suite: score/score-013.mei
      options:
        pageHeight: 3050
        pageWidth: 2290
        breaks: 'auto'
        scale: 41
        spacingStaff: 12
        adjustPageHeight: False
        header: 'auto'
        footer: 'auto'
        justifyVertically: True

    - name: 04-responsive-page
      test-suite: score/score-013.mei
      options:
        adjustPageHeight: False
        breaks: 'auto'
        pageHeight: 800
        pageWidth: 1800
        scale: 100
        scaleToPageSize: True
        spacingStaff: 12

    - name: 05-responsive-page
      test-suite: score/score-013.mei
      options:
        adjustPageHeight: False
        breaks: 'auto'
        pageHeight: 800
        pageWidth: 1800
        scale: 30
        scaleToPageSize: True
        spacingStaff: 12
---

### Page units and dimensions

Verovio uses an abstract unit for specifying the page dimensions. By default, the page height is `2970` and the page width is `2100`. These are equivalent to the dimension of an A4 page in portrait orientation in tenths of a millimeter. When generating SVG, these units are interpreted as pixels, which means that the default SVG image size is **2970px** height by **2100px** width. 

The example below shows an empty page with the default dimensions – and the option `--justifyVertically` turned on.

{% include music-notation-only example="01-default" %}

The option `--mm-output` can be enabled to change the page dimensions to millimeters. In this case, the SVG image will have a size of **297mm** by **210mm**, which is recommended if the SVG is meant to be printed or converted to PDF.

Page margins (`--page-margin-bottom`,  `--page-margin-left`,  `--page-margin-right` and  `--page-margin-top`) are all specified in abstract units, with a default value of `50`. That is **50px** with the default SVG output and **5mm** with the `--mm-output` option turned on.

#### MEI unit

Most of the options in Verovio are given in MEI units. An MEI unit (or MEI virtual unit) corresponds to half the distance between adjacent staff lines where the interline space is measured from the middle of a staff line. The value of the MEI unit in Verovio will determine the size of the staff on a page. By default, the MEI unit is `9.0`, which means that a staff space is 9 abstract units. In terms of staff size (or raster), it means a staff size of **72px** in the default SVG output, or **7.2mm** with the `--mm-output` option turned on.
 
In traditional music engraving, the staff size corresponds to the raster, which would be chosen depending of the type of score to be engraved. That would mean changing the MEI unit. However, in digital environments featuring responsive layout, there should be no need to change the default value of the MEI unit. The layout should be controlled with the page (i.e., the window or screen) size and scaling (see below). Nonetheless, the unit can be adjusted in Verovio with the `--unit` option. That can be useful if Verovio is used to replicate a print layout with a specific traditional page and staff size. The table below gives an indication of values for the MEI unit in Verovio corresponding to raster sizes as found in the literature or some music notation software applications.

| --- | --- | --- | --- |
| MEI unit | Raster | Staff size in mm | Example use |
| --- | --- | --- | --- |
| 11.5 | 0 | 9.2 | Educational music |
| 9.875 | 1 | 7.9 | |
| 9.25 | 2 | 7.4 | Piano music |
| 8.75 | 3 | 7.0 | Single-staff parts
| 8.125 | 4 | 6.5 | |
| 7.5 | 5 | 6.0 | |
| 6.875 | 6 | 5.5 | Choral music |
| 6.0 | 7 | 4.8 | |
| 4.625 | 8 | 3.7 | Full score |
{: .table .table-condensed .table-sm .text-xsmall}

{% aside .warning %}
Up to Verovio 3.13 only integer MEI units are supported.
{% endaside %}

The example below shows the same file as above with the default A4 page size but with a unit value of `6.0`. More music will be rendered on a page because the staff size is smaller.

{% include music-notation-only example="02-units" %}

Changing the page dimension will increase the amount of music that fits on the page. The example below has been rendered with the default unit of `9.0` but a page height of `3050` and a page width of `2290`, a more typical paper size for sheet music than A4.

{% include music-notation-only example="03-page-size" %}

### Scaling

The SVG output in Verovio can be scaled by using the `--scale` option. The option value is an integer representing a scaling percentage. It is `100` percent by default.

When changing the scale option, Verovio will by default change the size of the output SVG image. For example, with the default page size and a scale option set to `50` percent, the resulting SVG image will have a size of **1485px** by **1050px**. The same amount of music will be engraved on the page as with the default scale value.

In responsive environments, Verovio can be used to create user interfaces where the user can change the magnification ("zoom"). This can be achieved by changing the scale and the page dimensions. Zooming out means increasing the page dimensions and reducing the scale by the same factor, and zooming in the opposite. For example, if the window in which the output of Verovio will be displayed is 1800px by 800px, these can be set as a page height and page width and Verovio will produce an SVG image that fits the window with the default scale value of 100 percent. To implement a zooming out function, for example by a factor 2, the page dimensions have to be changed to 3600 by 1600 and the scale to 50. The output SVG image will then still have a size that fits the window.

Verovio has a `--scale-to-page-size` option that simplifies this process. Using this option is recommended in responsive environments. The advantage is that does not require the page dimensions to be calculated and changed by the user. With this option, the SVG output image will always have the same size independently from the scale percentage. The scale percentage determines how the rendering is scaled within this image. For example, reducing the scale percentage will increase the amount of music on the page. Keep in mind that when this option is enabled, the layout needs to be recalculated when the scale value is changed – see below.

The example below shows a file rendered with a page height of `800`, a width of `1600` and the default scale of `100` percent.

{% include music-notation-only example="04-responsive-page" %}

The example below is the same file rendered with the same page dimensions as above, but with the option `--scale-to-page-size` turned on and a scale of `30` percent. The SVG image size remains the same but the amount of music rendered has increased accordingly.

{% include music-notation-only example="05-responsive-page" %}

Changing the values of some options often requires the layout to be recalculated. For example, when the page dimensions are changed, then a call to `RedoLayout` must be made before rendering a page again. It is also important to keep in mind that redoing the layout might yield a different number of pages and that it is important to check the a page still exists with `GetPageCount` before rendering it.

When the `--scale-to-page-size` option is not turned on (default), then changing the scale option only does not require the layout to be recalculated before rendering a page again because the amount of music per page and the number of pages will not change. However, when the option `--scale-to-page-size` is turned on, then the layout recalculation and the page existence check need to happen before rendering a page.
