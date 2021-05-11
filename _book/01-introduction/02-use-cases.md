---
title: "Use-case scenarios"
---

### Architecture possibilities

Verovio is a C++ codebase that can be compiled and wrapped into different programming languages and integrated into various environments and several use-cases can be imagined for the Verovio toolkit. 

First of all, it can be built and used as a standalone command-line tool. This option is well suited to scripting environments and applications. The command-line tool can be used to render music notation files into SVG or into MIDI files. These files can be embedded in HTML files with everything happening on the server side. Verovio can also be used to convert data (e.g., MusicXML or Humdrum) to MEI. Typical use cases would be :
* generate SVG and MIDI from MEI documents or other supported formats,
* generate MEI documents from other supported formats (e.g., convert files).

Resulting SVG or MEI documents can then be embedded in a HTML page or used as such. 

![server-side use](/images/introduction/overview_server.png){:.img-responsive}

The JavaScript toolkit makes it possible to generate SVG and MIDI directly in the browser. It is easy to set up and platform independent. Interaction with the user can then be handled with basic JavaScript or CSS. An example of how to handle events is given in the tutorial. It is also possible to process the MEI via XSLT in the browser before loading it into Verovio. 

![client-side use](/images/introduction/overview_client.png){:.img-responsive}

Both approaches can be combined: one may choose to process the MEI and to generate the SVG server side for better performance, and then handle interactions client side with JavaScript and CSS.

![hybrid use](/images/introduction/overview_hybrid.png){:.img-responsive}

### Application examples

Interactive applications in which the MEI and Verovio pair is being used are very diverse. In this section, we list some example application uses-cases based on this pair and where interaction is an important component. Most of the projects selected are research projects or research tools, but not only.

#### Critical editions

The [Digital Interactive Mozart Edition (DIME)](https://mozarteum.at/dime/) is a joint project of the Salzburg Mozarteum Foundation and the Packard Humanities Institute in California. It is one example project in the field of digital critical editions that takes advantage of very rich and powerful markup possibilities offered by the MEI schema. In this context, interaction capabilities open completely new and welcome perspectives in interface design. Critical editions traditionally encompass extremely dense information networks that have to be laid out on paper with all the associated bi-dimensional constraints. Variant display is notoriously cumbersome and the information often has to be scattered between various part of the books (e.g., the critical notes referring to the music scores listed at the end of a volume).

![mozarteum](/images/introduction/use-cases/ism.png){:.img-responsive .example}

#### Genetic editing

Genetic editing is still an exploratory field in music. In this context, MEI is in active development under the lead of the [Beethovens Werkstatt](https://beethovens-werkstatt.de/) project. In genetic editing, time is a key dimension to be taken into account in the representation of differences. The differences in genetic editing represent different stages of writing for which it is not always possible to determine clearly their scope, their order in time or even their content because it is not always readable. This yields potentially very complex and large datasets for which the music notation content cannot be visualised as a whole. Only subsets of the data can here be reasonably visualised at a time, and interaction is the perfect approach for allowing highlighting, selection and navigation in the data.

![beethoven](/images/introduction/use-cases/beethoven.png){:.img-responsive .example}


#### Early music

Thanks to the overall simple structure of its notation (e.g., monophony for chant), early music has often been at the forefront of development of digital projects. Nonetheless, most of the time they remained isolated because of the need to develop dedicated encoding schemes and tools. The [Measuring Polyphony](https://measuringpolyphony.org/) project, a repository of digital encoding of late medieval polyphony at Brandeis University, is a good example of a change. The same ecosystem as for CWMN is used here. The MEI modularity allows for precise representation of the mensural notation, and the development of MEI and Verovio allow, for the first time, early music notation to be properly encoded accurately regarding the ternary and binary durations in the music. Interaction perspectives can be seen for linking original notation and modern transcriptions, which remains desirable for non-expert audiences.

![measuring-polyphony](/images/introduction/use-cases/mp.png){:.img-responsive .example}

#### Audio alignment

Alignment of scores with audio recordings, also known as score following, is a typical music information retrieval task. The main challenge is to generate the alignment data taking into account the fact that performances vary in tempo and that sections of the score can be repeated in some performances. The [Freischütz Digital](https://freischuetz-digital.de/) is an example project where the alignment data is stored in MEI with synchronisation information at the measure level generated for multiple recordings. The playback is synchronised with Verovio using measure xml:id for following the score or jumping anywhere in it. Clicking anywhere on the score can conversely be used to jump to the corresponding place in the recording. In the case of this project, because the MEI data also contains mapping of the measures with their corresponding zone in the facsimile image of the handwritten manuscript, the same synchronisation can be realized with it.

![freischütz](/images/introduction/use-cases/freischuetz.png){:.img-responsive .example}

#### Music notation editing

Interaction with music notation can take the form of data editing, either in a WYSIWYG manner or by allowing music encoding text editing. The Neon.js project for neume notation is an example of the former approach. It is currently going in-depth refactoring for switching from a previous ad-hoc rendering solution to Verovio rendering. The later editing approach is implemented in the [Verovio Humdrum Viewer](https://verovio.humdrum.org/) (VHV) project where editing of the encoding (Humdrum or MEI) is updated on the fly. The same setup has recently been integrated into Atom as a plugin package, MEI-tools-atom. In both the VHV and the Atom package, the rendered notation can be clicked to navigate in the encoding.

![vhv](/images/introduction/use-cases/vhv.png){:.img-responsive .example}

#### Music addressability

In music literature or in music practice, addressing music notation generally relies on movement names and measure numbers, and additionally voice or instrument names and beat numbers when necessary. However, there is no formalised concept behind this practical approach. Addressing music notation in the digital world has been recently the focus of the [Enhancing Music Notation Addressability](https://github.com/music-addressability/ema) (EMA) project at the University of Maryland. The goal of the project is to develop a generic system for expressing addresses in music notation documents. In order to evaluate it, the project developed a web service with an API for addressing MEI documents, the Open MEI Addressability Service (OMAS). The Verovio rendering is used to display a selection. Conversely, the rendered music notation can serve as the basis for selecting interactively a zone to be transformed into an address in the music notation data.

![continuo](/images/introduction/use-cases/continuo.png){:.img-responsive .example}

#### Visualisation

Visualisation is an important field of research and experimentation in digital humanities. With digital publications and digital devices, interactivity significantly increases the visualisation possibilities. For example, the visualisation scope or perspective can change dynamically following the choice of the user or the content of the data. With dynamic music notation rendering, it is possible to augment it with additional visualisation layers as demonstrated by the performance analysis and re-synthesis of piano music [PerformScore](https://mac.kaist.ac.kr/classic_music.html) project at the Music and Audio Computing Lab. A player featuring score following for multiple performances to be selected by the user as seen with the Freichütz Digital project is enhanced here with the visualisation of additional characteristics of the performance being played. They include tempo and dynamic changes but also the intensity of individual notes through colour and opacity adjustment. Louder notes become darker with high opacity and softer notes thinner with low opacity.

![PerformScore](/images/introduction/use-cases/scoreperform.png){:.img-responsive .example}

#### Composition

Contemporary music compositions can rely directly on the distinct features of digital score technology. An example is the 
[Chance Of Weather](https://raffazizzi.github.io/chanceOfWeather/) composition by Joseph Arkfeld based on Emily Dickinson’s poetic fragments “Fortitude - flanked with Melody”. The idea behind this project is to apply in the composition process the paradigm of fragment and variation as found in critical editions. The composition is made up of a set of fragments inspired by the poem and the encoding of the score is itself based on markup traditionally used for critical editions. Ultimately, the choice of the fragments for a particular instance of the composition is determined by an external data source, namely weather conditions (wind, cloud cover, temperature, etc.) at a geographical place to be chosen by the user. The weather conditions are transformed into a query that selects the corresponding fragments.

![chanceweather](/images/introduction/use-cases/chanceweather.png){:.img-responsive .example}

#### Performance

Interaction with music notation is quite common in the domain of performance. However, a significant breakthrough came on stage with the [Music Encoding and Linked Data](https://github.com/oerc-music/meld) (MELD) framework and Climb!, a music composition that mixes the idea of classical virtuoso piece and computer game. The major innovation of the project is that the dataset is stored as Linked Data using MELD. Climb! is a non-linear composition also made from a set of fragments moving from the bottom to the top of a graph representing a mountain. The path of a performance is not pre-determined and changes at each performance. At some stages, the performer has to play some excerpts, whose accuracy is dynamically verified in order to decide if the performer can proceed to the next stage. Feedback to the performer can be provided by the highlighting of score fragments.

![meld](/images/introduction/use-cases/meld.png){:.img-responsive .example}

#### Education

In the field of music education, interactive applications are more and more common and increasingly sophisticated. They typically link music notation with recordings, but also with user feedback (measure tempo, tuning, etc.). They are often built as mobile device applications, such as the [NomadPlay](https://www.nomadplay.app/en/) application. NomadPlay features a catalogue of recordings of a wide range of pieces from which the user can select his instrument. He can then rehearse the piece with the score of his instrument being displayed and synchronized with the recording but with the sound of his instrument removed. It is also possible to loop a difficult passage, or to change the tempo of the recording interactively.

![nomadplay](/images/introduction/use-cases/nomadplay-4.jpg){:.img-responsive .example}
