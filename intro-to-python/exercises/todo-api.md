# Python exercise: write a todo API

- Difficulty: easy
- Time to complete: 2-4h

## Functional specs

Write an API with the following endpoints:

```raw
GET /todos
GET /todos/{id}
POST /todos {title: "Buy toaster", status: "todo"}
PUT /todos/{id} {title: "Buy toaster for my dog"}
DELETE /todos/{id}
```

## Technical specs

You are free to choose a db. We recommend postgres (relational) or Redis
(non-relational).

You are free to choose any library, but we recommend the following setup in
2021:

- poetry: package management
- fastapi: web framework
- SQLAlchemy: ORM (if you chose a relational DB)

## To go further

Functional specs:

- Add due dates, order `GET /todos` by due date.

Developer experience:

- Add tests with pytest
- Add types with mypy
- Add linting with flake8
- Add autoformatting with black and isort
