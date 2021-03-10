| Name and parameter | Description | See also |
|---|---|---|
| <span class="lang1">`adjustPageHeight`</span><span class="lang2">`--adjust-page-height`</span> | Adjust the page height to the height of the content |  |
| <span class="lang1">`adjustPageWidth`</span><span class="lang2">`--adjust-page-width`</span> | Adjust the page width to the width of the content |  |
| <span class="lang1">`breaks`</span><span class="lang2">`--breaks`</span> `<s>` | Define page and system breaks layout<br/>(default: "auto"; other values: ['none', 'auto', 'line', 'smart', 'encoded']) |  |
| <span class="lang1">`breaksSmartSb`</span><span class="lang2">`--breaks-smart-sb`</span> `<f>` | In smart breaks mode, the portion of system width usage at which an encoded sb will be used<br/>(default: 0.66; min: 0.0; max: 1.0) |  |
| <span class="lang1">`clefChangeFactor`</span><span class="lang2">`--clef-change-factor`</span> `<f>` | Set the ratio of normal clefs to changing clefs<br/>(default: 0.66; min: 0.25; max: 1.0) |  |
| <span class="lang1">`condense`</span><span class="lang2">`--condense`</span> `<s>` | Control condensed score layout<br/>(default: "auto"; other values: ['none', 'auto', 'encoded']) |  |
| <span class="lang1">`condenseFirstPage`</span><span class="lang2">`--condense-first-page`</span> | When condensing a score also condense the first page |  |
| <span class="lang1">`condenseTempoPages`</span><span class="lang2">`--condense-tempo-pages`</span> | When condensing a score also condense pages with a tempo change |  |
| <span class="lang1">`evenNoteSpacing`</span><span class="lang2">`--even-note-spacing`</span> | Specify the linear spacing factor |  |
| <span class="lang1">`expand`</span><span class="lang2">`--expand`</span> `<s>` | Expand all referenced elements in the expansion <xml:id><br/>(default: "") |  |
| <span class="lang1">`footer`</span><span class="lang2">`--footer`</span> `<s>` | Control footer layout<br/>(default: "auto"; other values: ['none', 'auto', 'encoded', 'always']) |  |
| <span class="lang1">`header`</span><span class="lang2">`--header`</span> `<s>` | Control header layout<br/>(default: "auto"; other values: ['none', 'auto', 'encoded']) |  |
| <span class="lang1">`humType`</span><span class="lang2">`--hum-type`</span> | Include type attributes when importing from Humdrum |  |
| <span class="lang1">`justifyVertically`</span><span class="lang2">`--justify-vertically`</span> | Justify spacing vertically to fill the page |  |
| <span class="lang1">`landscape`</span><span class="lang2">`--landscape`</span> | The landscape paper orientation flag |  |
| <span class="lang1">`mensuralToMeasure`</span><span class="lang2">`--mensural-to-measure`</span> | Convert mensural sections to measure-based MEI | [Ligatures](/advanced-topics/mensural-notation.html#ligatures)<br/>[Layout](/advanced-topics/mensural-notation.html#layout) |
| <span class="lang1">`minLastJustification`</span><span class="lang2">`--min-last-justification`</span> `<f>` | The last system is only justified if the unjustified width is greater than this percent<br/>(default: 0.8; min: 0.0; max: 1.0) |  |
| <span class="lang1">`mmOutput`</span><span class="lang2">`--mm-output`</span> | Specify that the output in the SVG is given in mm (default is px) |  |
| <span class="lang1">`noJustification`</span><span class="lang2">`--no-justification`</span> | Do not justify the system |  |
| <span class="lang1">`openControlEvents`</span><span class="lang2">`--open-control-events`</span> | Render open control events |  |
| <span class="lang1">`outputIndent`</span><span class="lang2">`--output-indent`</span> `<i>` | Output indentation value for MEI and SVG<br/>(default: 3; min: 1; max: 10) |  |
| <span class="lang1">`outputIndentTab`</span><span class="lang2">`--output-indent-tab`</span> | Output indentation with tabulation for MEI and SVG |  |
| <span class="lang1">`outputSmuflXmlEntities`</span><span class="lang2">`--output-smufl-xml-entities`</span> | Output SMuFL charachters as XML entities instead of byte codes |  |
| <span class="lang1">`pageHeight`</span><span class="lang2">`--page-height`</span> `<i>` | The page height<br/>(default: 2970; min: 100; max: 60000) |  |
| <span class="lang1">`pageMarginBottom`</span><span class="lang2">`--page-margin-bottom`</span> `<i>` | The page bottom margin<br/>(default: 50; min: 0; max: 500) |  |
| <span class="lang1">`pageMarginLeft`</span><span class="lang2">`--page-margin-left`</span> `<i>` | The page left margin<br/>(default: 50; min: 0; max: 500) |  |
| <span class="lang1">`pageMarginRight`</span><span class="lang2">`--page-margin-right`</span> `<i>` | The page right margin<br/>(default: 50; min: 0; max: 500) |  |
| <span class="lang1">`pageMarginTop`</span><span class="lang2">`--page-margin-top`</span> `<i>` | The page top margin<br/>(default: 50; min: 0; max: 500) |  |
| <span class="lang1">`pageWidth`</span><span class="lang2">`--page-width`</span> `<i>` | The page width<br/>(default: 2100; min: 100; max: 60000) |  |
| <span class="lang1">`shrinkToFit`</span><span class="lang2">`--shrink-to-fit`</span> | Scale down page content to fit the page height if needed |  |
| <span class="lang1">`svgBoundingBoxes`</span><span class="lang2">`--svg-bounding-boxes`</span> | Include bounding boxes in SVG output |  |
| <span class="lang1">`svgFormatRaw`</span><span class="lang2">`--svg-format-raw`</span> | Writes SVG out with no line indenting or non-content newlines. |  |
| <span class="lang1">`svgHtml5`</span><span class="lang2">`--svg-html5`</span> | Write data-id and data-class attributes for JS usage and id clash avoidance. |  |
| <span class="lang1">`svgViewBox`</span><span class="lang2">`--svg-view-box`</span> | Use viewBox on svg root element for easy scaling of document |  |
| <span class="lang1">`unit`</span><span class="lang2">`--unit`</span> `<i>` | The MEI unit (1⁄2 of the distance between the staff lines)<br/>(default: 9; min: 6; max: 20) |  |
| <span class="lang1">`useBraceGlyph`</span><span class="lang2">`--use-brace-glyph`</span> | Use brace glyph from current font |  |
| <span class="lang1">`useFacsimile`</span><span class="lang2">`--use-facsimile`</span> | Use information in the <facsimile> element to control the layout |  |
| <span class="lang1">`usePgFooterForAll`</span><span class="lang2">`--use-pg-footer-for-all`</span> | Use the pgFooter for all pages |  |
| <span class="lang1">`usePgHeaderForAll`</span><span class="lang2">`--use-pg-header-for-all`</span> | Use the pgHeader for all pages |  |
{: .table .table-condensed}
