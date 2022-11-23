{% row option_row %}{% col 4 %} <span class="lang1">∅</span><span class="lang2">`-a, --all-pages `</span> {% endcol %}{% col 8 %} Output all pages {% endcol %}
{% endrow %}{% row option_row %}{% col 4 %} <span class="lang1">∅</span><span class="lang2">`-h, --help `</span> {% endcol %}{% col 8 %} Display this message {% endcol %}
{% endrow %}{% row option_row %}{% col 4 %} <span class="lang1">`"inputFrom": <string>`</span><span class="lang2">`-f, --input-from <string>`</span> {% endcol %}{% col 8 %} Select input format from: &quot;abc&quot;, &quot;darms&quot;, &quot;humdrum&quot;, &quot;mei&quot;, &quot;pae&quot;, &quot;xml&quot; (musicxml)<br/>(default: "mei")

See also: [Input formats](/toolkit-reference/input-formats.html) {% endcol %}
{% endrow %}{% row option_row %}{% col 4 %} <span class="lang1">∅</span><span class="lang2">`-l, --log-level <string>`</span> {% endcol %}{% col 8 %} Set the log level: &quot;off&quot;, &quot;error&quot;, &quot;warning&quot;, &quot;info&quot;, or &quot;debug&quot;<br/>(default: "warning") {% endcol %}
{% endrow %}{% row option_row %}{% col 4 %} <span class="lang1">∅</span><span class="lang2">`-o, --outfile <string>`</span> {% endcol %}{% col 8 %} Output file name (use &quot;-&quot; as file name for standard output)<br/>(default: "svg") {% endcol %}
{% endrow %}{% row option_row %}{% col 4 %} <span class="lang1">∅</span><span class="lang2">`-t, --output-to <string>`</span> {% endcol %}{% col 8 %} Select output format to: &quot;mei&quot;, &quot;mei-pb&quot;, &quot;mei-basic&quot;, &quot;svg&quot;, or &quot;midi&quot;<br/>(default: "svg")

See also: [Output formats](/toolkit-reference/output-formats.html) {% endcol %}
{% endrow %}{% row option_row %}{% col 4 %} <span class="lang1">∅</span><span class="lang2">`-p, --page <integer>`</span> {% endcol %}{% col 8 %} Select the page to engrave (default is 1) {% endcol %}
{% endrow %}{% row option_row %}{% col 4 %} <span class="lang1">∅</span><span class="lang2">`-r, --resource-path <string>`</span> {% endcol %}{% col 8 %} Path to the directory with Verovio resources<br/>(default: "/usr/local/share/verovio")

See also: [SetResourcePath](/toolkit-reference/toolkit-methods.html#setresourcepath) \| [Building the toolkit](/installing-or-building-from-sources/python.html#building-the-toolkit) {% endcol %}
{% endrow %}{% row option_row %}{% col 4 %} <span class="lang1">`"scale": <integer>`</span><span class="lang2">`-s, --scale <integer>`</span> {% endcol %}{% col 8 %} Scale of the output in percent (100 is normal size)<br/>(default: 100; min: 1; max: 1000) {% endcol %}
{% endrow %}{% row option_row %}{% col 4 %} <span class="lang1">∅</span><span class="lang2">`- , --stdin `</span> {% endcol %}{% col 8 %} Use &quot;-&quot; as input file or set the &quot;--stdin&quot; option for reading from the standard input {% endcol %}
{% endrow %}{% row option_row %}{% col 4 %} <span class="lang1">∅</span><span class="lang2">`-v, --version `</span> {% endcol %}{% col 8 %} Display the version number

{% include options/0-base/version.md %} {% endcol %}
{% endrow %}{% row option_row %}{% col 4 %} <span class="lang1">`"xmlIdSeed": <integer>`</span><span class="lang2">`-x, --xml-id-seed <integer>`</span> {% endcol %}{% col 8 %} Seed the random number generator for XML IDs (default is random) {% endcol %}
{% endrow %}