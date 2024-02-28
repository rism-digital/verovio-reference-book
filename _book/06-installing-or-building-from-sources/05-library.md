---
title: "Using as a library"
---

Verovio can be built and use as C++ or C library.

#### Building libverovio.so on Linux or libverovio.dylib on macOS

```sh
cd tools
cmake -DBUILD_AS_LIBRARY=ON .
make
```

Running `sudo make install` will copy the library and the headers in `/usr/local/lib` and `/usr/local/include/verovio` respectively.

#### Building verovio.dll on Windows using Microsoft Visual Studio Build Tools 2022

In addition to Microsoft Visual Studio Build Tools 2022, also [Make](https://gnuwin32.sourceforge.net/packages/make.htm) is used.

Open `x64 Native Tools Command Prompt for VS 2022` and enter:

```
cd cmake
cmake -G "Unix Makefiles" -DBUILD_AS_LIBRARY=ON -DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE .
make
```

### Examples

#### C++ interface

The following code is a minimal example using the C++ Toolkit class:

```cpp
#include <iostream>
using namespace std;

// Include header for the vrv::Toolkit classl
#include "toolkit.h"
 
int main()
{
    vrv::Toolkit tk(false);
    // Print the version
    cout << tk.GetVersion() << endl;
 
    return 0;
}
```

The example can be built with:

```sh
g++ main.cpp -o main --std=c++17 -lverovio -I/usr/local/include/verovio
```

Running `./main` should display the Verovio version.

#### C function interface

To use Verovio with any language that supports a plain C function interface you will first need to build Verovio as a library.
The compiled library (`libverovio.so`/`verovio.dll`) will contain callable C symbols. These wrapper symbols are defined in `./tools/c_wrapper.h`

To run a `main.c` example you can use gcc to compile the example and link to the pre-built library.

```sh
gcc main.c -o main -L../../tools -lverovio
```

Run (without changing your default `LD_LIBRARY_PATH`):

```sh
LD_LIBRARY_PATH=../../tools ./main
```
