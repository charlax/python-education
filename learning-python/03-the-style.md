# Python style

<!--TOC-->

- [Python style](#python-style)
  - [Readability first](#readability-first)
  - [Avoid classes](#avoid-classes)
  - [Avoid heavy OOP stuff](#avoid-heavy-oop-stuff)
  - [Avoid using magic](#avoid-using-magic)
  - [Embrace flexibility](#embrace-flexibility)
    - [Avoid strict typing, prefer duck typing](#avoid-strict-typing-prefer-duck-typing)
    - [Ask for forgiveness, not for permission](#ask-for-forgiveness-not-for-permission)
  - [Avoid long names](#avoid-long-names)
  - [Avoid globals](#avoid-globals)
  - [Functional programming in Python](#functional-programming-in-python)

<!--TOC-->

## Readability first

Python code reads and should read very much like pseudo code.

## Avoid classes

## Avoid heavy OOP stuff

- There are no private variables.
- Avoid factories.
- Avoid mixins.
- Avoid more than one layer of inheritance.

## Avoid using magic

Explicit is better than implicit

## Embrace flexibility

### Avoid strict typing, prefer duck typing

`getattr` and `hasattr`.

### Ask for forgiveness, not for permission

- [Idiomatic Python: EAFP versus LBYL](https://devblogs.microsoft.com/python/idiomatic-python-eafp-versus-lbyl/)

## Avoid long names

```python
class AbstractToasterFactoryClass:
    pass
```

## Avoid globals

Globals are:

- Difficult to debug (anything can modify them)
- Difficult to reuse outside the library

## Functional programming in Python

- `map` is builtin.
- `import functools` for some functional tooling
- Use a lib like `toolz` or `funcy` for more functional tools

Python lacks some functional features:

- Immutable by default
- True anonymous functions
- Tail recursion
