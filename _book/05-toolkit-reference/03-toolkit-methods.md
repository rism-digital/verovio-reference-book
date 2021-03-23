---
title: "Toolkit methods"
no-edit: true
# This file is auto-generated - do not edit
---

### Edit

Parse the editor actions passed as JSON string.

Only available for Emscripten-based compiles

**Returns**

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `json_editorAction` | `const std::string &` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::Edit(const std::string &json_editorAction)
```

**Example call**

```python
result = toolkit.edit(json_editorAction)
```

{% include method-doc file="edit-json_editoraction" %}
### EditInfo

**Returns**

`std::string`

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

**Returns**

`std::string`

**Original header**

```cpp
std::string vrv::Toolkit::GetAvailableOptions() const
```

**Example call**

```python
result = toolkit.getAvailableOptions()
```

{% include method-doc file="getavailableoptions" %}
### GetElementAttr

Return element attributes as a JSON string.

**Returns**

`std::string`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ |  |
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

`std::string`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `millisec` | `int` | ∅ |  |
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

`std::string`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ |  |
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

**Returns**

`void`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `output` | `std::ostream &` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
void vrv::Toolkit::GetHumdrum(std::ostream &output)
```

**Example call**

```python
toolkit.getHumdrum(output)
```

{% include method-doc file="gethumdrum-output" %}
### GetHumdrum

**Returns**

`std::string`

**Original header**

```cpp
std::string vrv::Toolkit::GetHumdrum()
```

**Example call**

```python
result = toolkit.getHumdrum()
```

{% include method-doc file="gethumdrum" %}
### GetHumdrumBuffer

**Returns**

`const char *`

**Original header**

```cpp
const char* vrv::Toolkit::GetHumdrumBuffer()
```

**Example call**

```python
result = toolkit.getHumdrumBuffer()
```

{% include method-doc file="gethumdrumbuffer" %}
### GetHumdrumFile

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
### GetInputFrom

**Returns**

`int`

**Original header**

```cpp
int vrv::Toolkit::GetInputFrom()
```

**Example call**

```python
result = toolkit.getInputFrom()
```

{% include method-doc file="getinputfrom" %}
### GetLog

Concatenates the vrv::logBuffer into a string an returns it.

This is used only for Emscripten-based compilation. The vrv::logBuffer is filled by the vrv::LogXXX functions.

**Returns**

`std::string`

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

Options (JSON) can be: pageNo: integer; (1-based), all pages if none (or 0) specified scoreBased: true|false; true by default (noXmlIds: true|false; false by default - remove all @xml:id not used in the data - not implemented)

**Returns**

`std::string`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `jsonOptions` | `const std::string &` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::GetMEI(const std::string &jsonOptions)
```

**Example call**

```python
result = toolkit.getMEI(jsonOptions)
```

{% include method-doc file="getmei-jsonoptions" %}
### GetMIDIValuesForElement

Return MIDI values of the element with the ID (xml:id).

RenderToMidi() must be called prior to using this method.

**Returns**

`std::string`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ |  |
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

`std::string`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ |  |
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

**Returns**

`std::string`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `option` | `const std::string &` | ∅ |  |
| `defaultValue` | `bool` | `false` |  |
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

**Returns**

`std::string`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `defaultValues` | `bool` | ∅ |  |
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
### GetOptions

Return the Options object of the Toolkit instance.

**Original header**

```cpp
Options* vrv::Toolkit::GetOptions()
```

**Example call**

```python
result = toolkit.getOptions()
```

{% include method-doc file="getoptions" %}
### GetOutputTo

**Returns**

`int`

**Original header**

```cpp
int vrv::Toolkit::GetOutputTo()
```

**Example call**

```python
result = toolkit.getOutputTo()
```

{% include method-doc file="getoutputto" %}
### GetPageCount

**Returns**

`int`

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

This takes into account the current layout options. Returns 0 if no element is found.

**Returns**

`int`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ |  |
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

**Returns**

`int`

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

RenderToMidi() must be called prior to using this method. Returns 0 if no element is found.

**Returns**

`int`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ |  |
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

Return a JSON object string with the following key values for a given note: scoreTimeOnset, scoreTimeOffset, scoreTimeTiedDuration, realTimeOnsetMilliseconds, realTimeOffsetMilliseconds, realTimeTiedDurationMilliseconds.

Returns 0 if no element is found.

**Returns**

`std::string`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `xmlId` | `const std::string &` | ∅ |  |
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

`std::string`

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

Returns the version number as a string.

This is used only for Emscripten-based compilation.

**Returns**

`std::string`

**Original header**

```cpp
std::string vrv::Toolkit::GetVersion()
```

**Example call**

```python
result = toolkit.getVersion()
```

{% include method-doc file="getversion" %}
### IdentifyInputFrom

**Returns**

`FileFormat`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `data` | `const std::string &` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
FileFormat vrv::Toolkit::IdentifyInputFrom(const std::string &data)
```

**Example call**

```python
result = toolkit.identifyInputFrom(data)
```

{% include method-doc file="identifyinputfrom-data" %}
### LoadData

Load a string data with the type previously specified in the options.

By default, the methods try to auto-detect the type.

**Returns**

`bool`

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

`bool`

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

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `data` | `const std::string &` | ∅ | A ZIP file in base64 encoded string |
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

True if loading the buffer succeed, false otherwise

**Returns**

`bool` – True if loading the buffer succeed, false otherwise

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

This can be called once the rendering option were changed, For example with a new page (sceen) height or a new zoom level.

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
### RenderToDeviceContext

Render the page to the deviceContext.

Page number is 1-based.

**Returns**

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `pageNo` | `int` | ∅ |  |
| `deviceContext` | `` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::RenderToDeviceContext(int pageNo, DeviceContext *deviceContext)
```

**Example call**

```python
result = toolkit.renderToDeviceContext(pageNo, deviceContext)
```

{% include method-doc file="rendertodevicecontext-pageno-devicecontext" %}
### RenderToMIDI

Creates a midi file, opens it, and returns it (base64 encoded).

**Returns**

`std::string`

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

Creates a midi file, opens it, and writes to it.

currently generates a dummy midi file.

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

Render the content to Plaine and Easie.

Only the top staff / layer is exported.

**Returns**

`std::string`

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

Export the content to a Plaine and Easie file.

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

Render the page in SVG and returns it as a string.

Page number is 1-based

**Returns**

`std::string`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `pageNo` | `int` | `1` |  |
| `xml_declaration` | `bool` | `false` |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
std::string vrv::Toolkit::RenderToSVG(int pageNo=1, bool xml_declaration=false)
```

**Example call**

```python
result = toolkit.renderToSVG(pageNo, xml_declaration)
```

{% include method-doc file="rendertosvg-pageno-xml_declaration" %}
### RenderToSVGFile

Render the page in SVG and save it to the file.

Page number is 1-based.

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

Creates a timemap file, and return it as a JSON string.

**Returns**

`std::string`

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
### SaveFile

Save an MEI file.

This is a lond description for Save.

**Returns**

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `filename` | `const std::string &` | ∅ | This parameter is the filename |
| `jsonOptions` | `const std::string &` | ∅ | There are the options. It cannot be null |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
bool vrv::Toolkit::SaveFile(const std::string &filename, const std::string &jsonOptions)
```

**Example call**

```python
result = toolkit.saveFile(filename, jsonOptions)
```

{% include method-doc file="savefile-filename-jsonoptions" %}
### SetHumdrumBuffer

**Returns**

`void`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `contents` | `const char *` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
void vrv::Toolkit::SetHumdrumBuffer(const char *contents)
```

**Example call**

```python
toolkit.setHumdrumBuffer(contents)
```

{% include method-doc file="sethumdrumbuffer-contents" %}
### SetInputFrom

**Returns**

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `inputFrom` | `std::string const &` | ∅ |  |
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
### SetInputFrom

**Returns**

`void`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `format` | `FileFormat` | ∅ |  |
{: .table .table-condensed .table-sm .text-xsmall}

**Original header**

```cpp
void vrv::Toolkit::SetInputFrom(FileFormat format)
```

**Example call**

```python
toolkit.setInputFrom(format)
```

{% include method-doc file="setinputfrom-format" %}
### SetOption

**Returns**

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `option` | `const std::string &` | ∅ |  |
| `value` | `const std::string &` | ∅ |  |
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

**Returns**

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `jsonOptions` | `const std::string &` | ∅ |  |
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

**Returns**

`bool`

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

`bool`

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

**Returns**

`bool`

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `scale` | `int` | ∅ |  |
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

If initFont is set to false, Resources::InitFonts will have to be called explicitely.

**Parameters**

|---|---|---|
| Name | Type | Default | Description |
| `initFont` | `bool` | `true` |  |
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
