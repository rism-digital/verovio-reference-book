---
title: "Python"
---

### Pre-build versions

Pre-build versions of the Python version of the toolkit are available through [PyPi](https://pypi.org/project/verovio/) for every release since version 3.1.0.

The Python versions for which a pre-build is provided are 3.7, 3.8, 3.9, 3.10 and 3.11. The platforms supported are macOS 10.9, Linux with [manylinux](https://github.com/pypa/manylinux) for x86-64, Win-32 and Win-amd64. 

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

The options are set on the toolkit instance. For the Python version of the toolkit, the options (and all other parameters or values return by a function that are a JSON string in the C++ version) are a Python Dictionary. For example, the following code will change the dimensions of the page and redo the layout for the previously loaded data:

```python
options = { "pageHeight": 2100, "pageWidth": 2950, "scale": 25 }
tk.setOptions(options)
tk.redoLayout()
tk.renderToSVGFile( "page-scaled.svg", 1 )
```

#### Building the toolkit

To build the Python toolkit you need to have swig and swig-python installed on your machine (see <a href="http://swig.org" target="_blank">SWIG</a>) and the Python distutils package. Version 4.0 or newer of SWIG is recommended but older versions should work too.  To install SWIG in macOS using [Homebrew](http://brew.sh), type the command `brew install swig`. 

The Python toolkit can be built with [CMake](https://cmake.org), You need at least version 3.13 of CMake because it uses the option `-B` introduced in that version of CMake. The steps are:

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

By default, Python 3 is used. If you want to use a specific version of Python, you can do:

```bash
cmake ../cmake -B python -DBUILD_AS_PYTHON=ON -DPYTHON_VERSION=3.9
```

*Installation with CMake has not be tested yet*

### Building the toolkit without CMake

The toolkit can be build without CMake. However, SWIG is still needed. It needs to be built from from the root directory of the repository content. To build it in-place, run:

```bash
python setup.py build_ext --inplace
```

If you want to install it, run:

```bash
python setup.py build_ext
sudo python setup.py install
```

For building it with one or more specific options (e.g., without Plaine & Easie support), run:

```bash
python setup.py build_ext --inplace --define NO_PAE_SUPPORT
```

#### Building with pip

You can build and install with `pip` by passing a path to a local repository with:

```bash
pip install <path_to_local_repo>
```

Note that installing directly from GitHub with `pip install git+https://github.com/rism-digital/verovio` will not work.

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

### Resources for versions built locally

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
