---
title: "Controlling the SVG output"

examples:
    - name: default
      test-suite: score/score-013.mei
      options:
        breaks: 'auto'
        spacingStaff: 12
        adjustPageHeight: False
        footer: 'auto'
        header: 'auto'
        justifyVertically: True

    - name: view-box
      test-suite: score/score-013.mei
      options:
        breaks: 'auto'
        spacingStaff: 12
        adjustPageHeight: False
        footer: 'auto'
        header: 'auto'
        justifyVertically: True
        svgViewBox: True

    - name: page-size
      test-suite: score/score-013.mei
      options:
        pageHeight: 3050
        pageWidth: 2290
        breaks: 'auto'
        scale: 41
        spacingStaff: 12
        adjustPageHeight: False
        footer: 'auto'
        header: 'auto'
        justifyVertically: True

    - name: responsive-page-100
      test-suite: score/score-013.mei
      options:
        adjustPageHeight: False
        breaks: 'auto'
        pageHeight: 800
        pageWidth: 900
        scale: 100
        scaleToPageSize: True
        spacingStaff: 12

    - name: responsive-page-30
      test-suite: score/score-013.mei
      options:
        adjustPageHeight: False
        breaks: 'auto'
        pageHeight: 800
        pageWidth: 900
        scale: 30
        scaleToPageSize: True
        spacingStaff: 12

    - name: units
      test-suite: score/score-013.mei
      options:
        breaks: 'auto'
        unit: 6.0
        spacingStaff: 12
        adjustPageHeight: False
        footer: 'auto'
        header: 'auto'
        justifyVertically: True
---

### Units and page dimensions

#### Verovio abstract unit

Verovio layout calculation is based on an internal abstract unit. This abstract unit is also used for specifying a few options, such as the page dimensions. By default, the page height is `2970` and the page width is `2100`. These are equivalent to the dimension of an A4 page in portrait orientation in tenths of a millimeter. When generating SVG, these units are interpreted as pixels, which means that the default SVG image size is **2970px** height by **2100px** width. 

The example below shows an empty page with the default dimensions – and the option `--justifyVertically` enabled.

{% include music-notation-only example="01-default" %}

Page margins (`--page-margin-bottom`,  `--page-margin-left`,  `--page-margin-right` and  `--page-margin-top`) are also specified in abstract units, with a default value of `50`. That is **50px** with the SVG image output.

Changing the page dimension will increase the amount of music that fits on the page. The example below if the same file rendered with a page height of `3050` and a page width of `2290`, a more typical paper size for sheet music than A4.

{% include music-notation-only example="page-size" %}

#### MEI unit

Most of the options in Verovio are given in MEI units. An MEI unit (or MEI virtual unit) corresponds to half the distance between adjacent staff lines where the interline space is measured from the middle of a staff line. The value of the MEI unit in Verovio is given in abstract units and determines the size of the staff on a page. By default, the MEI unit is `9.0`, which means that a staff space is 9 abstract units, or **9px** in the SVG image output with the default options.
 
In traditional music engraving, the staff size corresponds to the raster which would be chosen depending of the type and size of score to be engraved. However, in digital environments the size of the notation can be changed on the screen depending on the size and orientation of the screen (i.e., "responsive" environments), and the size of the raster can remain fixed. Adjusting the size of the notation in Verovio is usually changed by adjusting the page size and scaling factors, which are described in the next section.

### Scaling

The SVG output in Verovio can be scaled by using the `--scale` option. The option value is an integer representing a scaling percentage. It is `100` percent by default.

When changing the scale option, Verovio will by default change the size of the output SVG image. For example, with the default page size and a scale option set to `50` percent, the resulting SVG image will have a size of **1485px** by **1050px**. The same amount of music will be engraved on the page as with the default scale value.

In responsive environments, Verovio can be used to create user interfaces where the user can change the magnification ("zoom"). This can be achieved by changing the scale and the page dimensions. Zooming out means increasing the page dimensions and reducing the scale by the same factor, and zooming in the opposite. For example, if the window in which the output of Verovio will be displayed is **1800px** by **800px**, these can be set as a page height and page width and Verovio will produce an SVG image that fits the window with the default scale value of `100` percent. To implement a zooming out function, for example by a factor 2, the page dimensions have to be changed to `3600` by `1600` and the scale to `50`. The output SVG image will then still have a size that fits the window.

Verovio has a `--scale-to-page-size` option that simplifies this process. Using this option is recommended in responsive environments. The advantage is that does not require the page dimensions to be calculated and changed by the user. With this option, the SVG output image will always have the same size independently from the scale percentage. The scale percentage determines how the rendering is scaled within this image. For example, reducing the scale percentage will increase the amount of music on the page. When this option is enabled, the layout needs to be recalculated when the scale value is changed – see below.

The example below shows a file rendered with a page height of `800`, a width of `1600` and the default scale of `100` percent.

{% include music-notation-only example="responsive-page-100" %}

The example below is the same file rendered with the same page dimensions as above, but with the option `--scale-to-page-size` enabled and a scale of `30` percent. The SVG image size remains the same but the amount of music rendered has increased accordingly.

{% include music-notation-only example="responsive-page-30" %}

Changing the values of some options often requires the layout to be recalculated. For example, when the ratio of the page dimension are changed, or the margins are changed, then a call to `RedoLayout` must be made before rendering a page again. It is also important to keep in mind that redoing the layout might yield a different number of pages and that it is important to check the a page still exists with `GetPageCount` before rendering it.

When the `--scale-to-page-size` option is **not** enabled on (default), then changing only the scale option does not require the layout to be recalculated before rendering a page again because the amount of music per page and the number of pages will **not** change. However, when the option `--scale-to-page-size` is enabled, then the layout recalculation and the page existence check need to happen before rendering a page.

### SVG optimised for PDF generation

The SVG image output in pixel units is well suited to digital environments and rendering on screens. However, in some cases, the SVG will be subsequently converted to a PDF for printing. In such uses, it is recommended to enable the option `--mm-output` to change the page dimensions to millimeters. In this case, the SVG image produced with the default page height and page width will have a size of **297mm** by **210mm**. The page margins, with their default value of `50`, will have a size of **5mm**.

If you want to increase or decrease the amount of music on a page, there are two solutions. The first one is to enable the `--scale-to-page-size` option described above and to adjust the scale value. Because the image produced with the option remains fixed, the page will have a larger or a smaller amount of music on the page depending if the scale option was decreased or increased respectively. The other solution for changing the amount of music on a page is to adjust the MEI unit, which is described below.

#### Adjusting the MEI unit

If you want to replicate a print layout with a specific traditional page and staff size, you need to control the size of the staff (or raster). With Verovio, the raster  can be adjusted with the `--unit` option, which adjusts the definition of an MEI unit. One MEI unit (or MEI virtual unit) corresponds to half the distance between adjacent staff lines. In terms of staff size (or raster), it means a staff size of **7.2mm** with the `--mm-output` option enabled. Bear in mind that this size do not factor in the width of the staff line. Because the MEI unit size is measured from the middle of a staff line, the actual staff height will be two half staff line widths more. 

The table below gives an indication of values for the MEI unit in Verovio corresponding to raster sizes (without staff line width factored in) as found in the literature or some music notation software applications.

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

The example below shows the same file as above with the default A4 page size but with a unit value of `6.0`. More music is rendered on a page because the staff size is smaller.

{% include music-notation-only example="units" %}
