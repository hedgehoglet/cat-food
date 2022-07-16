# {{cookiecutter.repository_name}}

[![Build for Python 3.9.13](https://img.shields.io/badge/python-v3.9.13-blue)](https://www.python.org/downloads/release/python-3913/)
[![Formatted with black](https://img.shields.io/badge/format-black-black)](https://github.com/psf/black)
[![Checked with pylint](https://img.shields.io/badge/check-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Checked with mypy](https://img.shields.io/badge/check-mypy-blue)](http://mypy-lang.org/)

{{cookiecutter.repository_description}}

## Set up the environment
* Get Python 3.9.13 using [pyenv](https://github.com/pyenv/pyenv)
```bash
pyenv install 3.9.13
```
* Activate it as local Python environment
```bash
pyenv local 3.9.13
```
* Get your [Poetry](https://python-poetry.org/docs/#installation)
* Execute Makefile to get the environment ready
```bash
make activate
make setup
```

## Install new packages
* To install new PyPI packages, run
```bash
poetry add <package-name>
```
