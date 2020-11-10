# Learning Python the language

## Intro

- Indentation and spacing are syntax in Python
- Python favours shorter, explicit name
    - `s.upper()` (Python) vs. `s.toUpperCase()` (JS)
- Python has very few keywords and constructs. E.g. no `switch`, no `do... while`.

## Syntax

This part focuses on the syntax.

- Base types: `int`, `float`, `bool`, `str`, `bytes`, `complex`
- Container types: `list` (literal: `[]`), `tuple` (`()`), `dict` (`{"key": "value"}`), `set` (`{1, 2, 3}`), `frozenset`.
- Variable assignment (`a = 1`, `a = b = 1`, `a += 1`)
- Sequence containers indexing: `l[start slide:end slide:step]`
- Boolean logic: `>`, `and`, `or`, `not`
- Imports `import x` vs. `from x import y`
- Conditional statement: `if... else`
- Exceptions: `raise`,  `try... except... finally... else...`
- Conditional loop: `while`
- Iterative loop: `for i in sequence:`, `continue`, `break`
- Display and input: `print`, `input("question?")`
- Operation on containers: see below
- Operation on lists: see below
- Operations on dictionaries: see below
- Operations on set: see below
- Operations on strings: see below
- Files: see below
- Sequence: `range([start], end, step)`

## Mutability, identity, conversion, representation

Most types are immutable. `list`, `set` and `dict` are mutable.

- `id(obj)` returns the object's memory address
- `==` compares equality
- `is` compares identity
- Type conversion: just use the type itself e.g. `int("2")`
- Representation: `repr("a")`, `repr([1, 2, 3])`

More information:

- [Pointers in Python: What's the Point?](https://realpython.com/pointers-in-python/#immutable-vs-mutable-objects)

## Operations on strings

```python
s.startswith(value)
s.endswith(value)

s.find(sub, start, end)
s.isalpha(), s.islower()
s.upper(), s.lower()

# join
s.join(sequence)
assert ", ".join([1, 2]) == "1, 2"
```

Formatting:

```python
name = "Toaster"
print(f"Hello {name}")
```

## Containers

`len`, `min`, `sorted`, `enumerate`, `zip`, `all`, `any`, `reversed`

```python
# You can mix types
l = ["a", 1]

# Presence check with "in"
v = "a" in ["a"]
assert v is True
```

## Lists

Operation on lists: `l.append`, `l.extend`, `l.insert(index, val)`, `l.remove(val)`, `l.pop([index])`, `l.sort()` (in place), `l.reverse()`

```python
v = [1, 2]
```

## Loops

```python
for i in range(10):
    print(i)

for item in [0, 2, 4]:
    print(item)
```

## Dict

```python
# Definition
value = 1
c = {"key": value}

# Access
assert c["key"] == 1

# Deletion
del c["key"]

# Assignment
c["key"] = 1

d.keys()
d.values()
d.items()

d.pop(key[, default)
d.popitem()  # (key, value)
d.get(key[, default])
d.setdefault(key[, default])
```

## Set

```python
s = {1, 2, 3}
# Union
s |= {1, 2}
# Intersection
s &= {1, 2}

# ~ difference
# < <= > >= inclusion relations

s.update(s2)
s.copy()
s.add(value)
s.remove(value)
s.pop()
```

## Defining a function

```python
def hello():
    """Say hello."""
    print("hello world")

print(help(hello))
```

```python
# arguments
def hello(name: str):
    print(f"Hello {name}")


# arguments are required in Python! No default null or undefined

# Optional argument:
def hello(name: str = "toaster"):
    print(f"Hello {name}")

# x, y, z are positional arguments
# args are the rest positional arguments (list)
# a, b are keyword arguments
# kwargs are the rest keyword arguments (dict)

def hello(x, y, z, *args, *, a=1, b="2", **kwargs):
    pass
```

- Are there anonymous functions? No.
- `lambda` is not supposed to be assigned and only support a single line

```python
c = map(lambda v: v + "a", ["b", "c"])
assert c == ["ba", "ca"]
```

## OOP and classes (introduction)

- `super()`
- Multiple inheritance (e.g. mixins)

```python
class Toaster:
    pass
```

## Files

## Advanced topics

Those topics build upon your understanding the syntax.

```python
ternary = "a" if v else "b"

# pass
def a():
    pass  # Empty statement, sometimes useful
```

### Typing

- Types are always optional.
- Types are not checked at runtime, only if you use a tool like `mypy`.

```python
a: str = "a"
v: list[str] = [a]
c: dict[str, int] = {a: 1}  # {"a": 1}


def get_double(i: int) -> int:
    return i * 2
```

### Scopes, assignment and pass by reference/value

#### Ways to add to scope

- Assignment `x = 1`
- Imports `import sys`
- Function definition `def func(): pass`
- Function parameters `def func(a): pass`
- Class definition `class Toaster: pass`

Some other ways:

- Container comprehension
- Exception block
- Classes and instances

#### The LEGB rule

Python looks for a reference in this order:

- Local (or function) scope
    - A scope is created for each run, not at function definition
    - True even if you call the function recursively
    - `locals()`
- Enclosing (or nonlocal) scope
    - Names of the enclosing function for nested function definition
- Global (or module) scope
    - Top-level scope
    - Formatted `UPPER_CASE_WITH_UNDERSCORE`
    - `globals()`
- Builtin
    - E.g. `dir`, `open`, `len`, etc.
    - `dir(__builtins__)`

Questions:

- When inside a function, where does Python look at?
- When outside a function, where does Python look at?

```python
FIRST_NAME = "Louis"


def say_hello(last_name: str) -> None:
    def say(message: str) -> None:
        print(f"{message} {name}")

    say(f"Hello {FIRST_NAME}")


say_hello("de Funès")
```

#### Modifying scope behavior

In Python, you can't modify `global` or `nonlocal` variables without being explicit about it:

```python
NAME = "Louis"


def func():
    # This creates a new name in the local scope
    NAME = "Claude"


func()
# NAME did not change
assert NAME == "Louis"
```

You need to use the `global` or `nonlocal` keyword when you want to write globals:

```python
NAME = "Louis"


def func():
    global NAME
    NAME = "Claude"


func()
# Now it works!
assert NAME == "Claude"

```

For more information:

- [Python Scope & the LEGB Rule: Resolving Names in Your Code](https://realpython.com/python-scope-legb-rule/)
- [Pass by Reference in Python: Background and Best Practices](https://realpython.com/python-pass-by-reference/)

#### Assignment

```python
# a is the name, 2 is the value
# the name "a" is bound to the value 2
a = 2

# the name a is rebound to the value 3
a = 3

# Python keeps track of how many names are bound to a value
class Toaster():
    pass


t = Toaster()
t2 = t

from sys import getrefcount

assert getrefcount(t) > 2


def modify_dict(d):
    d["a"] = None


the_dict = {"b": 1}
return_value = modify_dict(the_dict)
print(return_value)
print(the_dict)

# To avoid modifying:
def modify_dict(d):
    d = d.copy()
    d["a"] = None
```

### Python is fully dynamic and everything is an object

```python
class Toaster:
    def __init__(self, color: str):
        self.color = color

t = Toaster("red")

dir(t)
vars(t)

# You can get a dict of local variables!
locals()
globals()

# Classes are objects!
Toaster.name
dir(Toaster)


def hello(t: Toaster) -> None:
    print(f"Hello {t.color}")


# Functions are objects!
hello.__name__
hello.__doc__
dir(hello)

# Modules are objects!
import sys

dir(sys)
```

See also:

- https://docs.python.org/3/library/inspect.html

#### Operator overloading

Almost all operators can be overloaded (seeing how is an advanced topic). `+=`, `==` etc.

### Context (`with`)

See advanced Python

## References

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Python Cheatsheet](https://www.pythoncheatsheet.org/)
- [Memento Python](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)
