| Name and parameter | Description | See also |
|---|---|---|
| <span class="lang1">`"adjustPageHeight":  <b>`</span><span class="lang2">`--adjust-page-height `</span> | Adjust the page height to the height of the content |  |
| <span class="lang1">`"adjustPageWidth":  <b>`</span><span class="lang2">`--adjust-page-width `</span> | Adjust the page width to the width of the content |  |
| <span class="lang1">`"breaks":  <s>`</span><span class="lang2">`--breaks  <s>`</span> | Define page and system breaks layout<br/>(default: "auto"; other values: ['none', 'auto', 'line', 'smart', 'encoded']) |  |
| <span class="lang1">`"breaksSmartSb":  <f>`</span><span class="lang2">`--breaks-smart-sb  <f>`</span> | In smart breaks mode, the portion of system width usage at which an encoded sb will be used<br/>(default: 0.66; min: 0.0; max: 1.0) |  |
| <span class="lang1">`"clefChangeFactor":  <f>`</span><span class="lang2">`--clef-change-factor  <f>`</span> | Set the ratio of normal clefs to changing clefs<br/>(default: 0.66; min: 0.25; max: 1.0) |  |
| <span class="lang1">`"condense":  <s>`</span><span class="lang2">`--condense  <s>`</span> | Control condensed score layout<br/>(default: "auto"; other values: ['none', 'auto', 'encoded']) |  |
| <span class="lang1">`"condenseFirstPage":  <b>`</span><span class="lang2">`--condense-first-page `</span> | When condensing a score also condense the first page |  |
| <span class="lang1">`"condenseTempoPages":  <b>`</span><span class="lang2">`--condense-tempo-pages `</span> | When condensing a score also condense pages with a tempo change |  |
| <span class="lang1">`"evenNoteSpacing":  <b>`</span><span class="lang2">`--even-note-spacing `</span> | Specify the linear spacing factor |  |
| <span class="lang1">`"expand":  <s>`</span><span class="lang2">`--expand  <s>`</span> | Expand all referenced elements in the expansion <xml:id><br/>(default: "") |  |
| <span class="lang1">`"footer":  <s>`</span><span class="lang2">`--footer  <s>`</span> | Control footer layout<br/>(default: "auto"; other values: ['none', 'auto', 'encoded', 'always']) |  |
| <span class="lang1">`"header":  <s>`</span><span class="lang2">`--header  <s>`</span> | Control header layout<br/>(default: "auto"; other values: ['none', 'auto', 'encoded']) |  |
| <span class="lang1">`"humType":  <b>`</span><span class="lang2">`--hum-type `</span> | Include type attributes when importing from Humdrum |  |
| <span class="lang1">`"justifyVertically":  <b>`</span><span class="lang2">`--justify-vertically `</span> | Justify spacing vertically to fill the page |  |
| <span class="lang1">`"landscape":  <b>`</span><span class="lang2">`--landscape `</span> | The landscape paper orientation flag |  |
| <span class="lang1">`"mensuralToMeasure":  <b>`</span><span class="lang2">`--mensural-to-measure `</span> | Convert mensural sections to measure-based MEI | [Ligatures](/advanced-topics/mensural-notation.html#ligatures)<br/>[Layout](/advanced-topics/mensural-notation.html#layout) |
| <span class="lang1">`"minLastJustification":  <f>`</span><span class="lang2">`--min-last-justification  <f>`</span> | The last system is only justified if the unjustified width is greater than this percent<br/>(default: 0.8; min: 0.0; max: 1.0) |  |
| <span class="lang1">`"mmOutput":  <b>`</span><span class="lang2">`--mm-output `</span> | Specify that the output in the SVG is given in mm (default is px) |  |
| <span class="lang1">`"noJustification":  <b>`</span><span class="lang2">`--no-justification `</span> | Do not justify the system |  |
| <span class="lang1">`"openControlEvents":  <b>`</span><span class="lang2">`--open-control-events `</span> | Render open control events |  |
| <span class="lang1">`"outputIndent":  <i>`</span><span class="lang2">`--output-indent  <i>`</span> | Output indentation value for MEI and SVG<br/>(default: 3; min: 1; max: 10) |  |
| <span class="lang1">`"outputIndentTab":  <b>`</span><span class="lang2">`--output-indent-tab `</span> | Output indentation with tabulation for MEI and SVG |  |
| <span class="lang1">`"outputSmuflXmlEntities":  <b>`</span><span class="lang2">`--output-smufl-xml-entities `</span> | Output SMuFL charachters as XML entities instead of byte codes |  |
| <span class="lang1">`"pageHeight":  <i>`</span><span class="lang2">`--page-height  <i>`</span> | The page height<br/>(default: 2970; min: 100; max: 60000) |  |
| <span class="lang1">`"pageMarginBottom":  <i>`</span><span class="lang2">`--page-margin-bottom  <i>`</span> | The page bottom margin<br/>(default: 50; min: 0; max: 500) |  |
| <span class="lang1">`"pageMarginLeft":  <i>`</span><span class="lang2">`--page-margin-left  <i>`</span> | The page left margin<br/>(default: 50; min: 0; max: 500) |  |
| <span class="lang1">`"pageMarginRight":  <i>`</span><span class="lang2">`--page-margin-right  <i>`</span> | The page right margin<br/>(default: 50; min: 0; max: 500) |  |
| <span class="lang1">`"pageMarginTop":  <i>`</span><span class="lang2">`--page-margin-top  <i>`</span> | The page top margin<br/>(default: 50; min: 0; max: 500) |  |
| <span class="lang1">`"pageWidth":  <i>`</span><span class="lang2">`--page-width  <i>`</span> | The page width<br/>(default: 2100; min: 100; max: 60000) |  |
| <span class="lang1">`"removeIds":  <b>`</span><span class="lang2">`--remove-ids `</span> | Remove XML IDs in the MEI output that are not referenced |  |
| <span class="lang1">`"shrinkToFit":  <b>`</span><span class="lang2">`--shrink-to-fit `</span> | Scale down page content to fit the page height if needed |  |
| <span class="lang1">`"svgBoundingBoxes":  <b>`</span><span class="lang2">`--svg-bounding-boxes `</span> | Include bounding boxes in SVG output |  |
| <span class="lang1">`"svgFormatRaw":  <b>`</span><span class="lang2">`--svg-format-raw `</span> | Writes SVG out with no line indenting or non-content newlines. |  |
| <span class="lang1">`"svgHtml5":  <b>`</span><span class="lang2">`--svg-html5 `</span> | Write data-id and data-class attributes for JS usage and id clash avoidance. |  |
| <span class="lang1">`"svgRemoveXlink":  <b>`</span><span class="lang2">`--svg-remove-xlink `</span> | Removes the xlink: prefix on href attributes for compatibility with some newer browsers. |  |
| <span class="lang1">`"svgViewBox":  <b>`</span><span class="lang2">`--svg-view-box `</span> | Use viewBox on svg root element for easy scaling of document |  |
| <span class="lang1">`"unit":  <i>`</span><span class="lang2">`--unit  <i>`</span> | The MEI unit (1⁄2 of the distance between the staff lines)<br/>(default: 9; min: 6; max: 20) |  |
| <span class="lang1">`"useBraceGlyph":  <b>`</span><span class="lang2">`--use-brace-glyph `</span> | Use brace glyph from current font |  |
| <span class="lang1">`"useFacsimile":  <b>`</span><span class="lang2">`--use-facsimile `</span> | Use information in the <facsimile> element to control the layout |  |
| <span class="lang1">`"usePgFooterForAll":  <b>`</span><span class="lang2">`--use-pg-footer-for-all `</span> | Use the pgFooter for all pages |  |
| <span class="lang1">`"usePgHeaderForAll":  <b>`</span><span class="lang2">`--use-pg-header-for-all `</span> | Use the pgHeader for all pages |  |
{: .table .table-condensed}
