---
title: "Coding guidelines"
---

This document describes the coding style for the Verovio project for the C++ part of the codebase.

### Formatting

Verovio uses a [ClangFormat](http://clang.llvm.org/docs/ClangFormat.html) (**15.0**) coding style based on the [WebKit](https://webkit.org/code-style-guidelines/) style, with a few minor modifications. The modifications include:

```yaml
AllowShortIfStatementsOnASingleLine: true
AllowShortLoopsOnASingleLine: true
ColumnLimit: 120
ConstructorInitializerAllOnOneLineOrOnePerLine: true
PointerAlignment: Right
```

The simplest way to fullfil the Verovio coding style is to use a clang-format tool and to apply the style defined in the `.clang-format` file available in the project root directory.

Short if-statements should be as single line only with single boolean evaluation.

#### How to install clang-format on macOS

An easy way to install clang-format on macOS computers is to use [Hombrew](http://brew.sh). Type this command in the terminal to install:

```bash
brew install clang-format
```

#### How to install clang-format on Ubuntu

On Ubuntu clang-format is available in the universe repository. You can install it easily with the command:

```bash
sudo apt install clang-format
```

#### Running clang-format

*Please make sure you use at least version 10.0*

To use clang-format to adjust a single file:

```bash
clang-format -style=file -i some-directory/some-file.cpp
```

The `-style=file` option instructs clang-format to search for the .clang-format configuration file (recursively in some parent directory). The `-i` option is used to alter the file "in-place". If you don't give the `-i` option, a fomatted copy of the file will be sent to standard output.

### Includes and forward declarations

Includes in the header files must list first the system includes followed by the Verovio includes, if any, and then the includes for the libraries included in Verovio. All includes have to be ordered alphabetically:

```cpp
#include <string>
#include <utility>
#include <vector>

//----------------------------------------------------------------------------

#include "attclasses.h"
#include "atttypes.h"

//----------------------------------------------------------------------------

#include "pugixml.hpp"
#include "utf8.h"
```

In the header files, always use forward declarations (and not includes) whenever possible. Forward declaration have to be ordered alphabetically:

```cpp
class DeviceContext;
class Layer;
class StaffAlignment;
class Syl;
class TimeSpanningInterface;
```

In the implementation files, the first include in always the include of the corresponding header file, followed by the system includes and then the other Verovio includes with libraries at the end too, if any, also ordered alphabetically:

```cpp
#include "att.h"

//----------------------------------------------------------------------------

#include <sstream>
#include <stdlib.h>

//----------------------------------------------------------------------------

#include "object.h"
#include "vrv.h"

//----------------------------------------------------------------------------

#include "pugixml.hpp"
```

### Null and boolean

The null pointer value should be written as `NULL`. Boolean values should be written as `true` and `false`.

### Integer data types

Integer numbers should be `int`, or `char` but only when this is clearly appropropriate. The use of `short` is to be avoided unless there are some particular reasons to use it. Variables and class members should not be `unsigned` numbers unless strictly necessary.

We use `int` and not `size_t`, even when working with C++ standard containers. Values such as the one returned by `std::vector::size()` need to be cast to `int` when assigned or compared to variables. However, in cases where the scope is limited to local operations on the container and the use of `int` would yield a warning, `size_t` is acceptable.

We avoid the use of `auto` and prefer explicit typing.

### Loop variable scope and increment

Variables should be made local to loops when possible (C99) and preferably pre-incremented.

```cpp
for (int i = 0; i < limit; ++i) {}
```

### Class, method and member names

All class names must be in upper CamelCase. The internal capitalization follows the MEI one:

```cpp
class Measure;
class ScoreDef;
class StaffDef;
```

All method names must also be in upper CamelCase:

```cpp
void Measure::AddStaff(Staff *staff) {}
```

All member names must be in lower camelCase. Instance members must be prefixed with `m_` and class (static) members with `s_`:

```cpp
class Glyph {
public:

    /** An instance member */
    int m_unitsPerEm;
    
    /** A static member */
    static std::string s_systemPath;
};
```

In the class declaration, the methods are declared first, and then the member variables. For both, the declaration order is `public`, `protected`, and `private`.

#### Use of `this`

The convention for the pointer `this` is to use it for method calls and not to use if for member access because these are prefixed with `m_`.

*As it stands, the codebase is not consistently following this convention*

### Comments

Comments for describing methods can be grouped using `///@{` and `///@}` delimiters together with the `@name` indication:

```cpp
/**
 * @name Add children to an editorial element.
 */
///@{
void AddFloatingElement(FloatingElement *child);
void AddLayerElement(LayerElement *child);
void AddTextElement(TextElement *child);
///@}
```

### LibMEI

The code for the attribute classes of Verovio are generated from the MEI schema using a modified version of LibMEI available [here](https://github.com/rism-digital/libmei). See the section [Generate code with LibMEI](/contributing/generate-code-with-libmei.html) for detailed information on how to modify and generate this code.

The attribute classes generated from the MEI schema provide all the members for the element classes of Verovio. They are implemented via multiple inheritance in element classes. The element classes corresponding to the MEI elements are not generated by LibMEI but are implemented explicitly in Verovio. They all inherit from the `Object` class (of the `vrv` namespace) or from a `Object` child class. They can inherit from various interfaces used for the rendering. All the MEI member are defined through the inheritance of generated attribute classes, either grouped as interfaces or individually.

For example, the MEI &lt;note&gt; is implemented as a `Note` class that inherit from `Object` through `LayerElement`. It also inherit from the StemmedDrawingInterface that holds data used for the rendering.

Its MEI members are defined through the `DurationInterface` and `PitchInterface` that regroup common functionnalities for durational and pitched MEI elements respectively plus some additional individual attribute classes.

The inheritance should always list `Object` (or the `Object` child class) first, followed by the rendering interfaces, followed by the attribute class interfaces, followed by the individual attribute classes, each of them ordered alphabetically:

```cpp
class Note : public LayerElement,
                public StemmedDrawingInterface,
                public DurationInterface,
                public PitchInterface,
                public AttColoration,
                public AttGraced,
                public AttStems,
                public AttTiepresent
```

In the implementation, the same order must be followed, for the constructor calls and for the registration of the interfaces and individual attribute classes:

```cpp
Note::Note()
    : LayerElement("note-")
    , StemmedDrawingInterface()
    , DurationInterface()
    , PitchInterface()
    , AttColoration()
    , AttGraced()
    , AttStems()
    , AttTiepresent()
{
    RegisterInterface(DurationInterface::GetAttClasses(), DurationInterface::IsInterface());
    RegisterInterface(PitchInterface::GetAttClasses(), PitchInterface::IsInterface());
    RegisterAttClass(ATT_COLORATION);
    RegisterAttClass(ATT_GRACED);
    RegisterAttClass(ATT_STEMS);
    RegisterAttClass(ATT_TIEPRESENT);

    Reset();
}
```

Resetting the attributes is required and follows the same order

```cpp
void Note::Reset()
{
    LayerElement::Reset();
    StemmedDrawingInterface::Reset();
    DurationInterface::Reset();
    PitchInterface::Reset();
    ResetColoration();
    ResetGraced();
    ResetStems();
    ResetTiepresent();
    
    // ...
}
```
