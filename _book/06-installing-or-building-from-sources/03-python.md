---
title: "Python"
---

### Pre-build versions

Pre-build versions of the Python version of the toolkit are available through [PyPi](https://pypi.org/project/verovio/) for every release since version 3.1.0.

The Python versions for which a pre-build is provided are 3.6, 3.7, 3.8 and 3.9. The platforms supported are MacOS 10.9, Linux with [manylinux](https://github.com/pypa/manylinux) for x86-64, Win-32 and Win-amd64. 

The latest release can be installed with:

```bash
pip install verovio
```

A previous version can be installed with:

```bash
 pip install verovio==3.2.0
 ```

For all platforms or architectures for which a pre-build version is not available in the PyPi repository, a source distribution is available. It can be installed with the same command as above. This will automatically trigger the compilation of the package.

### Basic usage of the toolkit

Once installed, the Verovio tookit module can be imported with

```python
import verovio
```

You can then create an instance of the toolkit and load data. For example:

```python
tk = verovio.toolkit()
tk.loadFile("path-to-mei-file")
tk.getPageCount()
```

Once loaded, the data can be rendered to a string:

```python
svg_string = tk.renderToSVG(1)
```

It can also be rendered to a file:

```python
tk.renderToSVGFile( "page.svg", 1 )
```

#### Setting options

The options are set on the toolkit instance. For example, the following code will change the dimensions of the page and redo the layout for the previously loaded data:

```python
tk.setOption( "pageHeight", "2100" )
tk.setOption( "pageWidth", "2900" )
tk.setScale(25)
tk.redoLayout()
tk.renderToSVGFile( "page-scaled.svg", 1 )
```

It is also possbile to collect options in a Python Dictionary and pass them as Json dump to the toolkit:  

```python
import json
options = {
    'pageHeight': 1000,
    'pageWidth': 1000
}
tk.setOptions(json.dumps(options))    
tk.redoLayout()
tk.renderToSVGFile( "page-square.svg", 1 )
```

### Building the toolkit

To build the Python toolkit you need to have swig and swig-python installed on your machine (see <a href="http://swig.org" target="_blank">SWIG</a>) and the Python distutils package. Version 4.0 or newer of SWIG is recommended but older versions should work too.  To install SWIG in MacOS using [Homebrew](http://brew.sh), type the command `brew install swig`. 

The toolkit needs to be built from from the root directory of the repository content. To build it in-place, run:

```bash
python setup.py build_ext --inplace
```

If you want to install it, run:

```bash
python setup.py build_ext
sudo python setup.py install
```

For building it with one or more specific options (e.g., without Plain and Easy support), run:

```bash
python setup.py build_ext --inplace --define NO_PAE_SUPPORT
```

#### Building a Python wheel locally

You can build a Python wheel locally with:

```bash
python setup.py bdist
```

For a source distribution, do:

```bash
python setup.py sdist
```

In both cases, the wheel will be written to the `./dist` directory.

#### Building with CMake

The Python toolkit can be built with [CMake](https://cmake.org), which can be significantly faster because parallel processing can be used. This is also the approach to recommend when developing because it will not rebuild the entire codebase when a change it made to a file but only the files that actually need to rebuilt.

For this approach to work you need at least version 3.13 of CMake because it uses the option `-B` introduced in that version of CMake. The steps are:

```bash
cd bindings
cmake ../cmake -B python -DBUILD_AS_PYTHON=ON
cd python
make -j8
```

If you want to enable or disable other specific options, you can do:

```bash
cmake ../cmake -B python -DBUILD_AS_PYTHON=ON -DNO_PAE_SUPPORT=ON
```

*Installation with CMake has not be tested yet*

#### Resources for versions built locally

When using a version built locally, you usually have to specify the path to the Verovio resources. To do so, you can do

```python
import verovio
tk = verovio.toolkit(False)
tk.setResourcePath("path-to-resource-dir")
```

Alternatively, you can set it before you create the instance of the toolkit

```python
import verovio
verovio.setDefaultResourcePath("path-to-resource-dir")
tk = verovio.toolkit()
```
