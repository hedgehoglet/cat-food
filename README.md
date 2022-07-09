# 🦔🐈 (cat-food)

Cat food is available to almost everyone, no matter where they live, and contains a high amount of protein which is what a hedgehog needs.

## Getting Started

* Install [Cookiecutter](https://github.com/cookiecutter/cookiecutter):
```bash
pip install cookiecutter
```

* Open your bag with cookiecutter:
```bash
cookiecutter https://github.com/hedgehoglet/cat-food.git
```

## Cat Food Package Design
```bash
🦔
├── .flake8                         # configuration for flake8 - a Python formatter tool
├── .gitignore                      # ignore files that we don't want to commit to Git
├── .pre-commit-config.yaml         # configurations for pre-commit
├── .pylintrc                       # configurations for pylint - a Python static code analyzer
├── LICENSE                         # license of your project
├── Makefile                        # store useful commands to set up the environment
├── README.md                       # describe your project
├── pyproject.toml                  # dependencies for poetry
├── {{cookiecutter.__repository_name}}/
│        ├── __init__.py                     # make {{cookiecutter.__repository_name}} a Python module
│        ├── src/                            # store source code
│        │   └── __init__.py                 # make src a Python module
│        └── tests/                          # store tests
│            └── __init__.py                 # make tests a Python module
└── notebooks/                               # store ipynb files
         └── playground.ipynb                # pre-defined jupyter notebook playground
```

## How Is Cat Food Made?
* [Poetry](https://python-poetry.org/): Dependency management
* [pre-commit plugins](https://pre-commit.com/): Automate code reviewing and formatting before create a commit
  - [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks): Predefined hooks such as detect-private-key, trailing-whitespace, etc.
  - [isort](https://github.com/PyCQA/isort): Imports sorter
  - [black](https://github.com/psf/black): Powerful code formatter
  - [flake8](https://github.com/PyCQA/flake8), [mypy](https://github.com/pre-commit/mirrors-mypy), [pylint](https://github.com/PyCQA/pylint): Static typing analyzer
  - [interrogate](https://github.com/econchick/interrogate): Docstrings checker