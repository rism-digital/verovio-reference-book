---
chapter-title: "Tutorial 1: First Steps"
title: "Introduction"
---

The first tutorial will look at how you can use Verovio to render music notation on a web page, using the pre-built JavaScript library. In this tutorial you will be building a small HTML page, with a minimal amount of JavaScript, to create an SVG rendering of an MEI file. In-depth technical expertise is not necessary, but you should be familiar with the basic principles of HTML to get the most out of this tutorial, and have access to a plain-text editor, preferably with facilities for automatically highlighting HTML and JavaScript code. (The [Atom](https://atom.io) editor is a good choice if you need a recommendation.)

By the end of this tutorial, you should understand the following:

 1. How to load the Verovio JavaScript library using the `<script>` tag;
 2. How to initialize Verovio, and how to set some basic rendering options;
 3. How to load an MEI file from a URL and pass it to Verovio to render;
 4. How to navigate between pages a multi-page score.

Later tutorials will cover more in-depth topics, such as how to have more control over rendering options, how to interact with the rendered notation, and how to play the notation back using MIDI.

### Basic browser skills

A good skill to have in working through these tutorials is how to access and use the JavaScript error console in your browser. Every modern browser comes with this facility. This feature is useful to see what might be causing problems since these problems may not be otherwise noticeable; your page just may not work, or it may not do what you expect.

Accessing the JavaScript console is slightly different in each browser.

#### Chrome

Keyboard shortcut:

- Ctrl + Shift + J (Windows/Linux)
- Command + Option + J (Mac)

Menu location:

- Menu > More Tools > Developer Tools > Console tab

[Chrome documentation](https://developers.google.com/web/tools/chrome-devtools/debug/console/console-ui?hl=en)

#### Firefox

Keyboard shortcut:

- Ctrl + Shift + K (Windows/Linux)
- Command + Option + K (Mac)

Menu location:

- Menu > Developer > Web Console

[Firefox documentation](https://developer.mozilla.org/en-US/docs/Tools/Web_Console/Opening_the_Web_Console)

#### Internet Explorer / Edge

Keyboard shortcut: F12

Menu location: Menu "three dots" icon > F12 Developer Tools > Console tab

[Edge documentation](https://dev.windows.com/en-us/microsoft-edge/platform/documentation/f12-devtools-guide/)

#### Safari

Keyboard shortcut:

- Command + Option + C

Menu location:

The Safari developer tools must be enabled before use.

 1. Safari > Preferences > Advanced > enable "Show Develop menu in menu bar"
 2. Develop > Show Error Console

[Safari documentation](https://developer.apple.com/library/safari/documentation/AppleApplications/Conceptual/Safari_Developer_Guide/GettingStarted/GettingStarted.html#//apple_ref/doc/uid/TP40007874-CH2-SW1)

[Source](https://documentation.concrete5.org/tutorials/how-open-browser-console-view-errors)
