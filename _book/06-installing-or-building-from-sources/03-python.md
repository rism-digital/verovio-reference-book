---
title: "Python"
---

### Pre-build versions

Pre-build versions of the Python toolkit are available through [PyPI](https://pypi.org/project/verovio/) for every release since version 3.1.0.

Current wheels support Python 3.10 and newer. The package is built as a CPython stable-ABI (`abi3`) wheel, so the same wheel can be reused across multiple Python versions. The currently supported platforms are macOS, Linux with [manylinux](https://github.com/pypa/manylinux) for x86-64 and aarch64, and Windows for win32 and win-amd64.

The latest release can be installed with:

```bash
pip install verovio
```

A previous version can be installed with:

```bash
pip install verovio==3.2.0
```

For platforms or architectures for which a wheel is not available from PyPI, a source distribution is also published. Installing it with `pip` will trigger a local build of the package.

### Basic usage of the toolkit

Once installed, the Verovio toolkit module can be imported with

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
tk.renderToSVGFile("page.svg", 1)
```

#### Setting the resource path

The Python wheels include the resource directory and it is normally resolved automatically when using the module. In some nonstandard environments or with locally built copies, it may still be necessary to set it explicitly. In such cases, you can use the resources included in the module with:

```python
import os
import verovio

tk = verovio.toolkit(False)
tk.setResourcePath(os.path.join(os.path.dirname(verovio.__file__), "data"))
```

#### Setting options

The options are set on the toolkit instance. For the Python version of the toolkit, the options (and all other parameters or values returned by a function that are a JSON string in the C++ version) are a Python dictionary. For example, the following code will change the dimensions of the page and redo the layout for the previously loaded data:

```python
options = {"pageHeight": 2100, "pageWidth": 2950, "scale": 25}
tk.setOptions(options)
tk.redoLayout()
tk.renderToSVGFile("page-scaled.svg", 1)
```

### Building the toolkit locally

The Python package is built from the root directory of the repository with `pyproject.toml`.

A standard local build can be done with the built-in Python tools `venv` and `pip`. Create a virtual environment from the Python interpreter you want to use:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Upgrade `pip` in the virtual environment:

```bash
python -m pip install --upgrade pip
```

Install the development build tools:

```bash
python -m pip install ".[dev]"
```

Build a wheel from the repository root:

```bash
python -m build --wheel
```

By default, this now produces a CPython stable-ABI `abi3` wheel targeting Python 3.10 and newer.

Build a source distribution with:

```bash
python -m build --sdist
```

Validate the built distributions with:

```bash
python -m twine check dist/*
```

Install the locally built wheel into the virtual environment with:

```bash
python -m pip install --force-reinstall dist/*.whl
```

Run the installed-wheel smoke test with:

```bash
python doc/python-smoke-test.py
```

The build uses an isolated PEP 517 environment. Build dependencies such as `scikit-build-core`, `swig`, and `ninja` are installed into that isolated build environment as needed.

#### Using uv for Python version and environment management

[uv](https://docs.astral.sh/uv/) can be used to install a specific Python version and create the virtual environment more conveniently. For example, to use Python 3.12:

```bash
uv python install 3.12
uv venv --python 3.12 .venv
```

You can then activate that environment and use the same build commands shown above:

```bash
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install ".[dev]"
python -m build --wheel
```

### How the Python package is built

`pyproject.toml` uses `scikit-build-core` as the build backend. It configures the existing CMake build with `BUILD_AS_PYTHON=ON`, and CMake builds the `verovio._verovio` extension module from the C++ sources and the SWIG interface.

The Python packaging configuration sets `wheel.py-api = "cp310"`, so the wheel is built for the CPython stable ABI and can be reused on Python 3.10 through 3.14.

The generated wheel installs:

- the compiled `_verovio` extension module
- the generated `verovio.py` SWIG proxy
- `__init__.py`
- `py.typed` and `verovio.pyi`
- the Verovio resource data under `verovio/data`

The `data/` directory is included by the CMake install rules.

### Resources for versions built locally

When using a locally built version in a nonstandard environment, you may still need to specify the path to the Verovio resources explicitly:

```python
import verovio

tk = verovio.toolkit(False)
tk.setResourcePath("path-to-resource-dir")
```

Alternatively, you can set it before you create the instance of the toolkit:

```python
import verovio

verovio.setDefaultResourcePath("path-to-resource-dir")
tk = verovio.toolkit()
```
