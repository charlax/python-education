# Python exercise: write a cache decorator

- Difficulty: medium
- Time to complete: 1-2h

## Functional specs

Write a Python decorator that can be used to cache a function's result. Its API
should look like this:

```python
@cache(ttl=3600)
def slow_function():
    import time

    time.sleep(5)
    return "result"


assert slow_function() == "result"  # takes 5 seconds
assert slow_function() == "result"  # returns immediately
```

## Technical specs

You are free to how to store results:

- In memory, with a simple dict
- On the file system
- In a Redis DB
- On AWS S3

## To go further

Functional specs:

- Make sure this works as you would expect if the function accepts arguments

Developer experience:

- Add tests with pytest
- Add types with mypy
- Add linting with flake8
- Add autoformatting with black and isort
