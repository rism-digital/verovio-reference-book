# Verovio book scripts

These scripts are used to generate certain parts of the Verovio book.

# Install

Python dependencies are managed with the `uv` tool. Formatting is provided by the `ruff` tool.

Both of these can be installed with Homebrew: `brew install uv ruff`.

To install the dependencies and the virtual environment, run: 

```
$ cd scripts
$ uv sync
```

This will create a virtual environment and install the dependencies. The `.python-version` file is used by `uv` to ensure that the correct version of Python is used, and it should install it automatically.

The virtual environment can be activated with (in the `scripts` directory):

```
$ source .venv/bin/activate
```

# Running

To run the scripts, ensure you have everything installed, activate the virtual env and run the `generate-all.sh` script:

```
$ cd scripts
$ uv sync
$ source .venv/bin/activate
$ cd ../
$ ./scripts/generate-all.sh
```

This should run all the scripts and generate the files.

# Developing

If you don't have a development environment that has `ruff` integration you can manually check the files:

`$ ruff check *.py`

And format them:

`$ ruff format *.py`

The configuration for ruff is in the `pyproject.toml` file.

To upgrade the dependencies:

`$ uv sync --upgrade`

Be sure to commit the `uv.lock` file so that everyone has the same versions of the dependencies installed.
