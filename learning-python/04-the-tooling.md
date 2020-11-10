# Python: the tooling

## Code style & linting

To enforce following the [PEP8 style guide](https://www.python.org/dev/peps/pep-0008/), use those tools:

- black (autoformatter like `go fmt` or `prettier`)
- flake8
- pylint (I prefer flake8 because it's less strict)

## Packaging

- **Poetry**
- pipenv
- virtualenv

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
