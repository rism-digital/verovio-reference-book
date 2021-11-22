---
title: "Toolkit methods"
no-edit: true
# This file is auto-generated - do not edit
---

### ConvertHumdrumToHumdrum

Filter Humdrum data.

**Returns**

`std::string` – The Humdrum data as a string

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `humdrumData` | `const std::string &` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::ConvertHumdrumToHumdrum(const std::string &humdrumData)
```

**Example call**

```python
result = toolkit.convertHumdrumToHumdrum(humdrumData)
```

{% include method-doc file="converthumdrumtohumdrum-humdrumdata" %}
### ConvertMEIToHumdrum

Convert MEI data into Humdrum data.

**Returns**

`std::string` – The Humdrum data as a string

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `meiData` | `const std::string &` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::ConvertMEIToHumdrum(const std::string &meiData)
```

**Example call**

```python
result = toolkit.convertMEIToHumdrum(meiData)
```

{% include method-doc file="convertmeitohumdrum-meidata" %}
### Edit

Edit the MEI data.

**Returns**

`bool` – True if the edit action was successfully applied

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `editorAction` | `const std::string &` | ∅ | The editor actions as a stringified JSON object |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::Edit(const std::string &editorAction)
```

**Example call**

```python
result = toolkit.edit(editorAction)
```

{% include method-doc file="edit-editoraction" %}
### EditInfo

Return the editor status.

**Returns**

`std::string` – The editor status as a string

**Original header**

```cpp
std::string vrv::Toolkit::EditInfo()
```

**Example call**

```python
result = toolkit.editInfo()
```

{% include method-doc file="editinfo" %}
### GetAvailableOptions

Return all available options grouped by category.

For each option, returns the type, the default value, and the minimum and maximum value (when available)

**Returns**

`std::string` – A stringified JSON object

**Original header**

```cpp
std::string vrv::Toolkit::GetAvailableOptions() const
```

**Example call**

```python
result = toolkit.getAvailableOptions()
```

{% include method-doc file="getavailableoptions" %}
### GetDescriptiveFeatures

Return descriptive features as a JSON string.

The features are tailored for implementing incipit search

**Returns**

`std::string` – A stringified JSON object with the requested features

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `options` | `const std::string &` | ∅ | A stringified JSON object with the feature extraction options |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::GetDescriptiveFeatures(const std::string &options)
```

**Example call**

```python
result = toolkit.getDescriptiveFeatures(options)
```

{% include method-doc file="getdescriptivefeatures-options" %}
### GetElementAttr

Return element attributes as a JSON string.

The attributes returned include the ones not supported by Verovio

**Returns**

`std::string` – A stringified JSON object with all attributes

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ | the ID (xml:id) of the element being looked for |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::GetElementAttr(const std::string &xmlId)
```

**Example call**

```python
result = toolkit.getElementAttr(xmlId)
```

{% include method-doc file="getelementattr-xmlid" %}
### GetElementsAtTime

Returns array of IDs of elements being currently played.

**Returns**

`std::string` – A stringified JSON object with the page and notes being played

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `millisec` | `int` | ∅ | The time in milliseconds |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::GetElementsAtTime(int millisec)
```

**Example call**

```python
result = toolkit.getElementsAtTime(millisec)
```

{% include method-doc file="getelementsattime-millisec" %}
### GetExpansionIdsForElement

Returns a vector of ID strings of all elements (the notated and the expanded) for a given element.

**Returns**

`std::string` – A stringified JSON object with all IDs

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ | the ID (xml:id) of the element being looked for |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::GetExpansionIdsForElement(const std::string &xmlId)
```

**Example call**

```python
result = toolkit.getExpansionIdsForElement(xmlId)
```

{% include method-doc file="getexpansionidsforelement-xmlid" %}
### GetHumdrum

Get the humdrum buffer.

**Returns**

`std::string` – The humdrum buffer as a string

**Original header**

```cpp
std::string vrv::Toolkit::GetHumdrum()
```

**Example call**

```python
result = toolkit.getHumdrum()
```

{% include method-doc file="gethumdrum" %}
### GetHumdrumFile

Write the humdrum buffer to the file.

This methods is not available in the JavaScript version of the toolkit.

**Returns**

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `filename` | `const std::string &` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::GetHumdrumFile(const std::string &filename)
```

**Example call**

```python
result = toolkit.getHumdrumFile(filename)
```

{% include method-doc file="gethumdrumfile-filename" %}
### GetLog

Get the log content for the latest operation.

**Returns**

`std::string` – The log content as a string

**Original header**

```cpp
std::string vrv::Toolkit::GetLog()
```

**Example call**

```python
result = toolkit.getLog()
```

{% include method-doc file="getlog" %}
### GetMEI

Get the MEI as a string.

**Returns**

`std::string`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `jsonOptions` | `const std::string &` | `""` | A stringified JSON object with the output options pageNo: integer; (1-based), all pages if none (or 0) specified; scoreBased: true or false; true by default; removeIds: true or false; false by default - remove all @xml:id not used in the data; |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::GetMEI(const std::string &jsonOptions="")
```

**Example call**

```python
result = toolkit.getMEI(jsonOptions)
```

{% include method-doc file="getmei-jsonoptions" %}
### GetMIDIValuesForElement

Return MIDI values of the element with the ID (xml:id)

RenderToMIDI() must be called prior to using this method

**Returns**

`std::string` – A stringified JSON object with the MIDI values

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ | the ID (xml:id) of the element being looked for |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::GetMIDIValuesForElement(const std::string &xmlId)
```

**Example call**

```python
result = toolkit.getMIDIValuesForElement(xmlId)
```

{% include method-doc file="getmidivaluesforelement-xmlid" %}
### GetNotatedIdForElement

Returns the ID string of the notated (the original) element.

**Returns**

`std::string` – A stringified JSON object with all IDs

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ | the ID (xml:id) of the element being looked for |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::GetNotatedIdForElement(const std::string &xmlId)
```

**Example call**

```python
result = toolkit.getNotatedIdForElement(xmlId)
```

{% include method-doc file="getnotatedidforelement-xmlid" %}
### GetOption

Get the value for an option.

**Returns**

`std::string` – The option value as a string

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `option` | `const std::string &` | ∅ | The name of the option |
| `defaultValue` | `bool` | `false` | True to get the default value of the option |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::GetOption(const std::string &option, bool defaultValue=false) const
```

**Example call**

```python
result = toolkit.getOption(option, defaultValue)
```

{% include method-doc file="getoption-option-defaultvalue" %}
### GetOptions

Return a dictionary of all the options.

**Returns**

`std::string` – A stringified JSON object

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `defaultValues` | `bool` | ∅ | True for getting the default values and false for the current values |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::GetOptions(bool defaultValues) const
```

**Example call**

```python
result = toolkit.getOptions(defaultValues)
```

{% include method-doc file="getoptions-defaultvalues" %}
### GetPageCount

Return the number of pages in the loaded document.

The number of pages depends one the page size and if encoded layout was taken into account or not.

**Returns**

`int` – The number of pages

**Original header**

```cpp
int vrv::Toolkit::GetPageCount()
```

**Example call**

```python
result = toolkit.getPageCount()
```

{% include method-doc file="getpagecount" %}
### GetPageWithElement

Return the page on which the element is the ID (xml:id) is rendered.

This takes into account the current layout options.

**Returns**

`int` – the page number (1-based) where the element is (0 if not found)

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ | the ID (xml:id) of the element being looked for |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
int vrv::Toolkit::GetPageWithElement(const std::string &xmlId)
```

**Example call**

```python
result = toolkit.getPageWithElement(xmlId)
```

{% include method-doc file="getpagewithelement-xmlid" %}
### GetScale

Get the scale option.

**Returns**

`int` – the scale option as integer

**Original header**

```cpp
int vrv::Toolkit::GetScale()
```

**Example call**

```python
result = toolkit.getScale()
```

{% include method-doc file="getscale" %}
### GetTimeForElement

Return the time at which the element is the ID (xml:id) is played.

RenderToMIDI() must be called prior to using this method.

**Returns**

`int` – The time in milliseconds

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ | the ID (xml:id) of the element being looked for |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
int vrv::Toolkit::GetTimeForElement(const std::string &xmlId)
```

**Example call**

```python
result = toolkit.getTimeForElement(xmlId)
```

{% include method-doc file="gettimeforelement-xmlid" %}
### GetTimesForElement

Return a JSON object string with the following key values for a given note.

Return scoreTimeOnset, scoreTimeOffset, scoreTimeTiedDuration, realTimeOnsetMilliseconds, realTimeOffsetMilliseconds, realTimeTiedDurationMilliseconds.

**Returns**

`std::string` – A stringified JSON object with the values

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ | the ID (xml:id) of the element being looked for |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::GetTimesForElement(const std::string &xmlId)
```

**Example call**

```python
result = toolkit.getTimesForElement(xmlId)
```

{% include method-doc file="gettimesforelement-xmlid" %}
### GetUuid

Return the ID of the Toolkit instance.

**Returns**

`std::string` – The ID as as string

**Original header**

```cpp
std::string vrv::Toolkit::GetUuid()
```

**Example call**

```python
result = toolkit.getUuid()
```

{% include method-doc file="getuuid" %}
### GetVersion

Return the version number.

**Returns**

`std::string` – the version number as a string

**Original header**

```cpp
std::string vrv::Toolkit::GetVersion()
```

**Example call**

```python
result = toolkit.getVersion()
```

{% include method-doc file="getversion" %}
### LoadData

Load a string data with the type previously specified in the options.

By default, the methods try to auto-detect the type.

**Returns**

`bool` – True if the data was successfully loaded

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `data` | `const std::string &` | ∅ | A string with the data (e.g., MEI data) to be loaded |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::LoadData(const std::string &data)
```

**Example call**

```python
result = toolkit.loadData(data)
```

{% include method-doc file="loaddata-data" %}
### LoadFile

Load a file from the file system.

Previously convert UTF16 files to UTF8 or extract files from MusicXML compressed files.

**Returns**

`bool` – True if the file was successfully loaded

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `filename` | `const std::string &` | ∅ | The filename to be loaded |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::LoadFile(const std::string &filename)
```

**Example call**

```python
result = toolkit.loadFile(filename)
```

{% include method-doc file="loadfile-filename" %}
### LoadZipDataBase64

Load a MusicXML compressed file passed as base64 encoded string.

**Returns**

`bool` – True if the data was successfully loaded

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `data` | `const std::string &` | ∅ | A ZIP file as a base64 encoded string |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::LoadZipDataBase64(const std::string &data)
```

**Example call**

```python
result = toolkit.loadZipDataBase64(data)
```

{% include method-doc file="loadzipdatabase64-data" %}
### LoadZipDataBuffer

Load a MusicXML compressed file passed as a buffer of bytes.

**Returns**

`bool` – True if the data was successfully loaded

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `data` | `const unsigned char *` | ∅ | A ZIP file as a buffer of bytes |
| `length` | `int` | ∅ | The size of the data buffer |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::LoadZipDataBuffer(const unsigned char *data, int length)
```

**Example call**

```python
result = toolkit.loadZipDataBuffer(data, length)
```

{% include method-doc file="loadzipdatabuffer-data-length" %}
### RedoLayout

Redo the layout of the loaded data.

This can be called once the rendering option were changed, for example with a new page (sceen) height or a new zoom level.

**Returns**

`void`

**Original header**

```cpp
void vrv::Toolkit::RedoLayout()
```

**Example call**

```python
toolkit.redoLayout()
```

{% include method-doc file="redolayout" %}
### RedoPagePitchPosLayout

Redo the layout of the pitch postitions of the current drawing page.

Only the note vertical positions are recalculated with this method. RedoLayout() needs to be called for a full recalculation.

**Returns**

`void`

**Original header**

```cpp
void vrv::Toolkit::RedoPagePitchPosLayout()
```

**Example call**

```python
toolkit.redoPagePitchPosLayout()
```

{% include method-doc file="redopagepitchposlayout" %}
### RenderToMIDI

Render the document to MIDI.

**Returns**

`std::string` – A MIDI file as a base64 encoded string

**Original header**

```cpp
std::string vrv::Toolkit::RenderToMIDI()
```

**Example call**

```python
result = toolkit.renderToMIDI()
```

{% include method-doc file="rendertomidi" %}
### RenderToMIDIFile

Render a document to MIDI and save it to the file.

This methods is not available in the JavaScript version of the toolkit.

**Returns**

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `filename` | `const std::string &` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::RenderToMIDIFile(const std::string &filename)
```

**Example call**

```python
result = toolkit.renderToMIDIFile(filename)
```

{% include method-doc file="rendertomidifile-filename" %}
### RenderToPAE

Render a document to Plaine and Easie.

Only the top staff / layer is exported.

**Returns**

`std::string` – The PAE as a string

**Original header**

```cpp
std::string vrv::Toolkit::RenderToPAE()
```

**Example call**

```python
result = toolkit.renderToPAE()
```

{% include method-doc file="rendertopae" %}
### RenderToPAEFile

Render a document to Plaine and Easie and save it to the file.

Only the top staff / layer is exported. This methods is not available in the JavaScript version of the toolkit.

**Returns**

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `filename` | `const std::string &` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::RenderToPAEFile(const std::string &filename)
```

**Example call**

```python
result = toolkit.renderToPAEFile(filename)
```

{% include method-doc file="rendertopaefile-filename" %}
### RenderToSVG

Render a page to SVG.

**Returns**

`std::string` – The SVG page as a string

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `pageNo` | `int` | `1` | The page to render (1-based) |
| `xmlDeclaration` | `bool` | `false` | True for including the xml declaration in the SVG output |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::RenderToSVG(int pageNo=1, bool xmlDeclaration=false)
```

**Example call**

```python
result = toolkit.renderToSVG(pageNo, xmlDeclaration)
```

{% include method-doc file="rendertosvg-pageno-xmldeclaration" %}
### RenderToSVGFile

Render a page to SVG and save it to the file.

This methods is not available in the JavaScript version of the toolkit.

**Returns**

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `filename` | `const std::string &` | ∅ |  |
| `pageNo` | `int` | `1` |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::RenderToSVGFile(const std::string &filename, int pageNo=1)
```

**Example call**

```python
result = toolkit.renderToSVGFile(filename, pageNo)
```

{% include method-doc file="rendertosvgfile-filename-pageno" %}
### RenderToTimemap

Render a document to a timemap.

**Returns**

`std::string` – The timemap as a string

**Original header**

```cpp
std::string vrv::Toolkit::RenderToTimemap()
```

**Example call**

```python
result = toolkit.renderToTimemap()
```

{% include method-doc file="rendertotimemap" %}
### RenderToTimemapFile

Render a document to timemap and save it to the file.

This methods is not available in the JavaScript version of the toolkit.

**Returns**

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `filename` | `const std::string &` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::RenderToTimemapFile(const std::string &filename)
```

**Example call**

```python
result = toolkit.renderToTimemapFile(filename)
```

{% include method-doc file="rendertotimemapfile-filename" %}
### ResetOptions

Reset all options to default values.

**Returns**

`void`

**Original header**

```cpp
void vrv::Toolkit::ResetOptions()
```

**Example call**

```python
toolkit.resetOptions()
```

{% include method-doc file="resetoptions" %}
### ResetXmlIdSeed

Reset the @xml:id seed.

Passing 0 will seed the xml:id generator with a random (time-based) seed value. This method will have no effect if the xml-id-checksum option is set.

**Returns**

`void`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `seed` | `int` | ∅ | The seed value for generating the xml:id values (0 for a time-based random seed) |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
void vrv::Toolkit::ResetXmlIdSeed(int seed)
```

**Example call**

```python
toolkit.resetXmlIdSeed(seed)
```

{% include method-doc file="resetxmlidseed-seed" %}
### SaveFile

Get the MEI and save it to the file.

This methods is not available in the JavaScript version of the toolkit.

**Returns**

`bool` – True if the file was successfully written

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `filename` | `const std::string &` | ∅ | The output filename |
| `jsonOptions` | `const std::string &` | `""` | A stringified JSON object with the output options |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::SaveFile(const std::string &filename, const std::string &jsonOptions="")
```

**Example call**

```python
result = toolkit.saveFile(filename, jsonOptions)
```

{% include method-doc file="savefile-filename-jsonoptions" %}
### SetInputFrom

Set the input from option.

**Returns**

`bool` – True if the option was successfully set

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `inputFrom` | `std::string const &` | ∅ | the input from value as string |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::SetInputFrom(std::string const &inputFrom)
```

**Example call**

```python
result = toolkit.setInputFrom(inputFrom)
```

{% include method-doc file="setinputfrom-inputfrom" %}
### SetOption

Set the value for an option.

**Returns**

`bool` – True if the option was successfully set

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `option` | `const std::string &` | ∅ | The name of the option |
| `value` | `const std::string &` | ∅ | The option value as string |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::SetOption(const std::string &option, const std::string &value)
```

**Example call**

```python
result = toolkit.setOption(option, value)
```

{% include method-doc file="setoption-option-value" %}
### SetOptions

Set option values.

The name of each option to be set is to be given as JSON key.

**Returns**

`bool` – True if the options were successfully set

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `jsonOptions` | `const std::string &` | ∅ | A stringified JSON objects with the output options |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::SetOptions(const std::string &jsonOptions)
```

**Example call**

```python
result = toolkit.setOptions(jsonOptions)
```

{% include method-doc file="setoptions-jsonoptions" %}
### SetOutputTo

Set the output to option.

**Returns**

`bool` – True if the option was successfully set

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `outputTo` | `std::string const &` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::SetOutputTo(std::string const &outputTo)
```

**Example call**

```python
result = toolkit.setOutputTo(outputTo)
```

{% include method-doc file="setoutputto-outputto" %}
### SetResourcePath

Set the resource path for the Toolkit instance.

This method needs to be called if the constructor had initFont=false or if the resource path needs to be changed.

**Returns**

`bool` – True if the resources was successfully loaded

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `path` | `const std::string &` | ∅ | The path to the resource directory |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::SetResourcePath(const std::string &path)
```

**Example call**

```python
result = toolkit.setResourcePath(path)
```

{% include method-doc file="setresourcepath-path" %}
### SetScale

Set the scale option.

**Returns**

`bool` – True if the option was successfully set

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `scale` | `int` | ∅ | the scale value as integer |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::SetScale(int scale)
```

**Example call**

```python
result = toolkit.setScale(scale)
```

{% include method-doc file="setscale-scale" %}
### Toolkit

Constructor.

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `initFont` | `bool` | `true` | If set to false, resource path is not initialized and SetResourcePath will have to be called explicitely |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
vrv::Toolkit::Toolkit(bool initFont=true)
```

**Example call**

```python
result = toolkit.toolkit(initFont)
```

{% include method-doc file="toolkit-initfont" %}
### ValidatePAE

Validate the Plaine and Easie code passed in the string data.

A single JSON object is returned when there is a global input error. When reading the input succeeds, validation is grouped by input keys. The methods always returns errors in PAE pedantic mode. No data remains loaded after the validation.

**Returns**

`std::string` – A stringified JSON object with the validation warnings or errors

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `data` | `const std::string &` | ∅ | A string with the data in JSON or with PAE @ keys |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::ValidatePAE(const std::string &data)
```

**Example call**

```python
result = toolkit.validatePAE(data)
```

{% include method-doc file="validatepae-data" %}
### ValidatePAEFile

Validate the Plaine and Easie file from the file system.

The method calls Toolkit::ValidatePAE. This methods is not available in the JavaScript version of the toolkit.

**Returns**

`std::string` – A stringified JSON object with the validation warnings or errors

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `filename` | `const std::string &` | ∅ | The filename to be validated |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::ValidatePAEFile(const std::string &filename)
```

**Example call**

```python
result = toolkit.validatePAEFile(filename)
```

{% include method-doc file="validatepaefile-filename" %}
