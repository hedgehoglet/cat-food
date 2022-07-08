# {{cookiecutter.repository_name}}

[![Formatted with black](https://img.shields.io/badge/format-black-black)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/check-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Checked with mypy](https://img.shields.io/badge/check-mypy-blue)](http://mypy-lang.org/)

{{cookiecutter.repository_description}}

## Set up the environment
* Get your [Poetry](https://python-poetry.org/docs/#installation)
* Set up the environment:
```bash
make activate
make setup
```

## Install new packages
* To install new PyPI packages, run:
```bash
poetry add <package-name>
```
