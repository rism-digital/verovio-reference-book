---
title: "Overview"
---

Verovio is a C++ codebase that can be compiled and wrapped into different programming languages and integrated into various environments.

The Command-line interface or the Python toolkit can be used in scripting environments or server side. Typical use cases would be :
* generate SVG and MIDI from MEI documents or other supported formats,
* generate MEI documents from other supported formats (e.g., convert files).

Resulting SVG or MEI documents can then be embedded in a HTML page or used as such. 

![server-side use](/images/introduction/overview_server.png){:.img-responsive}

The JavaScript toolkit makes it possible to generate SVG and MIDI directly in the browser. It is easy to set up and platform independent. Interaction with the user can then be handled with basic JavaScript or CSS. An example of how to handle events is given in the tutorial. It is also possible to process the MEI via XSLT in the browser before loading it into Verovio. 

![client-side use](/images/introduction/overview_client.png){:.img-responsive}

Both approaches can be combined: one may choose to process the MEI and to generate the SVG server side for better performance, and then handle interactions client side with JavaScript and CSS.

![hybrid use](/images/introduction/overview_hybrid.png){:.img-responsive}