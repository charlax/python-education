# Python style

<!--TOC-->

- [Python style](#python-style)
  - [Review first](#review-first)
  - [Readability first](#readability-first)
  - [Avoid classes](#avoid-classes)
  - [Avoid heavy OOP stuff](#avoid-heavy-oop-stuff)
  - [Avoid using magic](#avoid-using-magic)
  - [Embrace flexibility](#embrace-flexibility)
    - [Avoid strict typing, prefer duck typing](#avoid-strict-typing-prefer-duck-typing)
    - [Ask for forgiveness, not for permission](#ask-for-forgiveness-not-for-permission)
  - [Avoid long names](#avoid-long-names)
  - [Avoid globals](#avoid-globals)
  - [Avoid using too many dependencies](#avoid-using-too-many-dependencies)
  - [Functional programming in Python](#functional-programming-in-python)

<!--TOC-->

## Review first

See at the end of [02-the-language](./02-the-language.md)

## Readability first

Python code reads and should read very much like pseudo code.

> “Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.”

― Antoine de Saint-Exupéry

## Avoid classes

## Avoid heavy OOP stuff

- There are no private variables.
- Avoid factories.
- Avoid mixins.
- Avoid more than one layer of inheritance.

## Avoid using magic

Explicit is better than implicit

Python is a very dynamic language. There is almost no limit to your imagination. But with great power comes great responsibility: you got to be careful about how far you go with introducing magic in your code. Take inspiration from Golang, which has almost no magic at all!

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

## Avoid using too many dependencies

The standard library is very complete.

[The State of the Octoverse 2020](https://octoverse.github.com/) shows that there are far less dependencies in Python projects:

> 683 median transitive dependencies for npm followed by PHP (70), Ruby (68), and Python (19). All of which can become impacted by one security vulnerability.

## Functional programming in Python

- `map` is builtin.
- `import functools` for some functional tooling
- `itertools`
- Use a lib like `toolz` or `funcy` for more functional tools
- `lambda` are a bit annoying, because they're single line.
- Decorators are a super useful pattern and help understand how dynamic Python is

Python lacks some functional features:

- Immutable by default
- True anonymous functions
- Tail recursion
