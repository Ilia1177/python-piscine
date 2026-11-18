# ft_package

A sample Python package, built with `setuptools` and installable with `pip`.

## Description

`ft_package` is a small exercise in Python packaging. It shows how to:

- describe a project in `pyproject.toml`,
- build a source archive (`.tar.gz`) and a wheel (`.whl`),
- install the result with `pip`.

The package exposes a single dumb function, `greet`.

## Project structure

```
.
├── LICENSE
├── README.md
├── pyproject.toml
└── ft_package/
    ├── __init__.py
    └── ft_package.py
```

## Requirements

- Python 3.10 or later
- `pip`
- the `build` package (only needed to build the archives)

## Build

From the folder that contains `pyproject.toml`:

```bash
python -m pip install build
python -m build
```

This creates a `dist/` folder containing:

- `ft_package-0.0.1.tar.gz` (source distribution)
- `ft_package-0.0.1-py3-none-any.whl` (wheel)

## Installation

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

or

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

For development, an editable install picks up code changes without
rebuilding:

```bash
pip install -e .
```

## Usage

```python
from ft_package import greet

greet("your name -- super -- try test")
```

Check that the package is installed:

```bash
pip show -f ft_package
```

## Uninstall

```bash
pip uninstall ft_package
```

## License

See the [LICENSE](LICENSE) file.
