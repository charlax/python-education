# Python: the tooling

<!--TOC-->

- [Python: the tooling](#python-the-tooling)
  - [Code style & linting & typing](#code-style--linting--typing)
  - [Packaging & dependencies & local environment](#packaging--dependencies--local-environment)
    - [Virtual environment](#virtual-environment)
  - [Tests](#tests)
  - [Web apps](#web-apps)
    - [HTTP framework](#http-framework)
    - [ORM/DB](#ormdb)
    - [Async tasks](#async-tasks)
    - [CLI](#cli)

<!--TOC-->

## Code style & linting & typing

To enforce following the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/), use those tools:

- black (autoformatter like `go fmt` or `prettier`)
- flake8
- pylint (I prefer flake8 because it's less strict)
- mypy
- [pydocstyle](http://www.pydocstyle.org/en/stable/)
- [isort](https://github.com/PyCQA/isort)

## Packaging & dependencies & local environment

- **Poetry**
- pipenv
- virtualenv
- pyenv

### Virtual environment

- Why
- How (without poetry & the likes)

```bash
python -m venv env
source env/bin/activate
pip install sqlalchemy  # compare with local env
```

## Tests

- **pytest**
- unittest (standard library)

## Web apps

### HTTP framework

- **Flask**
- Sanic
- fastapi

### ORM/DB

- **sqlalchemy** with alembic for running migrations
- peewee

### Async tasks

- celery

### CLI

- https://docs.python.org/3/library/argparse.html
- typer
- click
