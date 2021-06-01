# Learning Python as a language

<!--TOC-->

- [Learning Python as a language](#learning-python-as-a-language)
  - [Intro](#intro)
  - [Syntax](#syntax)
  - [Mutability, identity, conversion, representation](#mutability-identity-conversion-representation)
  - [Boolean logic](#boolean-logic)
  - [Operations on strings](#operations-on-strings)
  - [Containers](#containers)
  - [Lists](#lists)
  - [Loops](#loops)
  - [Dict](#dict)
  - [Set](#set)
  - [Function](#function)
  - [Exceptions](#exceptions)
  - [OOP and classes (introduction)](#oop-and-classes-introduction)
    - [Class objects](#class-objects)
    - [Class instance](#class-instance)
    - [Inheritance](#inheritance)
    - [See also](#see-also)
  - [Imports and modules](#imports-and-modules)
  - [Files](#files)
  - [Typing Python](#typing-python)
  - [Scopes, assignment and pass by reference/value](#scopes-assignment-and-pass-by-referencevalue)
    - [Namespaces](#namespaces)
    - [Scope](#scope)
    - [The LEGB rule](#the-legb-rule)
    - [Modifying scope behavior](#modifying-scope-behavior)
    - [Assignment](#assignment)
  - [Python is fully dynamic and everything is an object](#python-is-fully-dynamic-and-everything-is-an-object)
  - [The standard library](#the-standard-library)
  - [Navigating the Python documentation](#navigating-the-python-documentation)
  - [Python "gotchas"](#python-gotchas)
  - [What's next?](#whats-next)
  - [Self-review](#self-review)
  - [References](#references)

<!--TOC-->

## Intro

- Indentation and spacing are syntax in Python
- Python favours shorter, explicit name
    - `s.upper()` (Python) vs. `s.toUpperCase()` (JS)
- Python has very few keywords and constructs. E.g. no `switch`, no `do... while`.

## Syntax

❓ Questions to ask orally:

- How do you display something?
    - `print`
- How do you get some input?
    - `input("yes or no?")`
- What are the base types?
    - `int`, `float`, `bool`, `str`, `bytes`, `complex`
- What are the container types?
    - `list` (literal: `[]`), `tuple` (`()`), `dict` (`{"key": "value"}`), `set` (`{1, 2, 3}`), `frozenset`.
- How do you assign a variable?
    - `a = 1`, `a = b = 1`, `a += 1`
- How do you write a conditional statement? `if... else`

## Mutability, identity, conversion, representation

❓ Questions to ask orally:

- What are mutable and immutable types in Python?
- What is the difference between equality and identity?
- How do you convert between types?
- How do you display the value of a name?

Most types are immutable. `list`, `set` and `dict` are mutable.

- `id(obj)` returns the object's memory address
- `==` compares equality
- `is` compares identity
- Type conversion: just use the type itself e.g. `int("2")`
- Representation: `repr("a")`, `repr([1, 2, 3])`

More information:

- [Pointers in Python: What's the Point?](https://realpython.com/pointers-in-python/#immutable-vs-mutable-objects)

## Boolean logic

```python
# How do you compare numbers?
x > 1

# How do you check for truthiness?
bool(True)

# ternary operator
ternary = "a" if v else "b"

# or, and, not?
```

## Operations on strings

❓ Questions to ask orally:

- How do you check if a string starts with something?
- Is all alphabetical characters?
- How do you join a list with a string?

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

❓ Questions to ask orally:

- How do you `print` a variable within a string?

Formatting:

```python
name = "Toaster"
print(f"Hello {name}")
```

## Containers

❓ Questions to ask orally:

- How do you get the length of a container?
- How do you get the minimum of a list?
- How do you return `True` if all values within a container are truthy?

`len`, `min`, `sorted`, `enumerate`, `zip`, `all`, `any`, `reversed`

```python
# You can mix types
l = ["a", 1]

# Presence check with "in"
v = "a" in ["a"]
assert v is True
```

Comprehensions:

```python
# List
r = [i ** 2 for i in range(10) if i % 3]

# Generator
r = (i ** 2 for i in range(10) if i % 3)

# Dict
r = {v: v * 2 for f in range(10)}
```

## Lists

❓ Questions to ask orally:

- How do you append to a list?
- How do you get the last item in a list?
- How do you get the last 3 items in a list?

Operation on lists: `l.append`, `l.extend`, `l.insert(index, val)`, `l.remove(val)`, `l.pop([index])`, `l.sort()` (in place), `l.reverse()`

```python
v = list([1, 2])
# literals are preferred
v = [1, 2]

# Sequence containers indexing: l[start slide:end slide:step]
# -1 works as you would expect
```

## Loops

❓ Questions to ask orally:

- How do you count from 1 to 10?
    - Sequence: `range([start], end, step)`

```python
for i in range(10):
    print(i)

for item in [0, 2, 4]:
    print(item)

# What will this loop do?
while v == True:
    v = False

# continue
# break
```

## Dict

❓ Questions to ask orally:

- How do you write a dict?
- How do you add a key and value to a dict?
- How do you access a dict key?
- How do you check of a key in a dict?
- How do you get a value in a dict or a default if it's not there?

```python
# Definition
value = 1
c = dict(key=value)
# literal is preferred
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

d.pop(key, default)
d.popitem()  # (key, value)
d.get(key, default)
d.setdefault(key, default)
```

## Set

```python
# How do you define a set?
s = {1, 2, 3}
# How do you get the union of a set with another?
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

## Function

❓ Questions to ask orally:

- How do you define a function?
- How do you define a function with mandatory arguments?
- How do you define a function with optional arguments?
- What happens when mandatory arguments are not provided?

```python
def hello():
    """Say hello."""
    print("hello world")


help(hello)
```

```python
# arguments
def hello(name: str):
    print(f"Hello {name}")


# Both work!
hello("Louis")
hello(name="Louis")

# arguments are required in Python! No default null or undefined

# Optional argument:
def hello(name: str = "toaster"):
    print(f"Hello {name}")


# x, y, z are positional arguments
# args are the rest positional arguments (list)
# a, b are keyword arguments
# kwargs are the rest keyword arguments (dict)

# def hello(x, y, z, *args, *, a=1, b="2", **kwargs):
#     pass
```

❓ Questions to ask orally:

- Are there anonymous functions?
    - Not really.
    - `lambda` is not supposed to be assigned and only supports a single line
- How do you transform a list in positional arguments?
    - `f(*args)`
- How do you transform a dict in keyword arguments?
    - `f(**kwargs)`

```python
c = map(lambda v: v + "a", ["b", "c"])
assert c == ["ba", "ca"]
```

See also:

- https://docs.python.org/3/tutorial/controlflow.html

## Exceptions

❓ Questions to ask orally:

- How do you try something?
- How do you create a custom exception?

```python
# Simple try... except... with raise
try:
    raise ValueError("Wrong value")
except ValueError:
    print("caught ValueError")


try:
    raise ValueError("e")
except ValueError as e:
    print(e)
else:
    print("no exception")
finally:
    print("always run")


# Custom exception
class MyException(Exception):
    pass
```

## OOP and classes (introduction)

❓ Questions to ask orally:

- When are classes created? Runtime or compile time?
- What are instances?
- What are class attributes vs. instance attributes?
- What are class methods vs. instance methods?

Classes are created at runtime and can be modified at runtime.

- Class = type
- Class instance = object
- Class can have class attributes and class methods
- Instance have attributes and methods defined on the class

- `super()`
- Multiple inheritance (e.g. mixins)
- `isinstance`, `issubclass`

```python
class Toaster:
    pass
```


### Class objects

❓ Questions to ask orally:

- How do you define a class?
- How do you define a constructor?
- How do you define a method? A classmethod?
- How do you define a class variable?

```python
class Toaster:
    """A toaster."""

    brand = "Moulinex"

    def say_hello(self):
        return "hello bread!"


print(Toaster)
print(Toaster.brand)
print(Toaster.say_hello)
print(Toaster.__doc__)


# Let's create a new instance
toaster = Toaster()
print(toaster.brand)
print(toaster.say_hello)
print(toaster.say_hello())
```

### Class instance

❓ Questions to ask orally:

- How do you create a class instance?
- How do you assign instance attributes?

```python
class Toaster:
    brand = "Moulinex"

    def __init__(self, color: str) -> None:
        self.color = color

    def say_color(self) -> None:
        return f"hello my color is {self.color}"


t = Toaster("red")
print(t.color)
print(t.say_color)
print(t.say_color())

# Attribute change
t.color = "green"

say_color = t.say_color
# It works! (poke JavaScript)
say_color()

t2 = Toaster("blue")

assert t.brand == t2.brand
assert t.color != t2.color

# Watch out when using mutable variables as class variable
```

- There are no private methods or private attribute. Prefix with `_`
  (preferred) or `__` to state that this should not be accessed.


```python
class BetterToaster:
    def __init__(self, color: str, brand: str) -> None:
        self.color = color
        self._brand = brand
        self._is_toasting = False

    def start_toasting(self) -> None:
        self._is_toasting = True

    def toast(self) -> None:
        self.color = "red"
        self.start_toasting()

    # Custom getter
    @property
    def status(self) -> str:
        return "on" if self._is_toasting else "off"


t = BetterToaster("red", "moulinex")
t.toast()
assert t.status == "on"
```

### Inheritance

❓ Questions to ask orally:

- How do you inherit?
- Does Python support multiple inheritance?

```python
class Animal:
    pass


class Dog(Animal):
    pass


class GoldenRetriever(Dog):
    pass


olympe = GoldenRetriever()
assert isinstance(olympe, Dog)
assert isinstance(olympe, Animal)

assert issubclass(GoldenRetriever, Dog)
assert issubclass(GoldenRetriever, Animal)


# Multiple inheritance
class HasName:
    pass


class DogPet(Dog, HasName):
    pass
```

### See also

https://docs.python.org/3/tutorial/classes.html

## Imports and modules

❓ Questions to ask orally:

- How do you group functionality in Python?
- How do you import and export?

```python
from module import x
import x
```

❓ Questions to ask orally:

- How do you export stuff in Python?
    - You don't! Everything is exported by default.
- Should you use relative or absolute imports?

## Files

❓ Questions to ask orally:

- What can go wrong when not using `with`?

```python
f = open("file.md")
content = f.read()
f.close()

# Better: using "context" with "with"
with open("file.md", "w") as f:
    f.write("# Hello")


import json

with open("file.json") as f:
    content = json.load(f)

# That's it!
```

## Typing Python

❓ Questions to ask orally:

- Is Python weakly typed?
- Is Python statically typed?

Important points:

- Types are always optional.
- Types are not checked at runtime, only if you use a tool like `mypy`.

```python
a: str = "a"
v: list[str] = [a]
c: dict[str, int] = {a: 1}  # {"a": 1}


def get_double(i: int) -> int:
    return i * 2
```

## Scopes, assignment and pass by reference/value

### Namespaces

❓ Questions to ask orally:

- What is a namespace?
- When are they created?

> A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries, but that’s normally not noticeable in any way (except for performance), and it may change in the future. Examples of namespaces are: the set of built-in names (containing functions such as abs(), and built-in exception names); the global names in a module; and the local names in a function invocation. In a sense the set of attributes of an object also form a namespace. The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces; for instance, two different modules may both define a function maximize without confusion — users of the modules must prefix it with the module name.

https://docs.python.org/3/tutorial/classes.html

- Namespaces are created at different moments and have different lifetimes.

### Scope

❓ Questions to ask orally:

- What is a scope?

> A scope is a textual region of a Python program where a namespace is directly accessible. “Directly accessible” here means that an unqualified reference to a name attempts to find the name in the namespace.

- Assignment `x = 1`
- Imports `import sys`
- Function definition `def func(): pass`
- Function parameters `def func(a): pass`
- Class definition `class Toaster: pass`

Some other ways:

- Container comprehension
- Exception block
- Classes and instances

> A special quirk of Python is that – if no global or nonlocal statement is in effect – assignments to names always go into the innermost scope. Assignments do not copy data — they just bind names to objects.

### The LEGB rule

❓ Questions to ask orally:

- Where does Python look for references?

Python looks for a reference in this order:

- **Local** (or function) scope
    - A scope is created for each run, not at function definition
    - True even if you call the function recursively
    - `locals()`
- **Enclosing** (or nonlocal) scope
    - Names of the enclosing function for nested function definition
- **Global** (or module) scope
    - Top-level scope
    - Formatted `UPPER_CASE_WITH_UNDERSCORE`
    - `globals()`
- **Builtin**
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

### Modifying scope behavior

❓ Questions to ask orally:

- How do you write a global var?

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
- https://docs.python.org/3/tutorial/classes.html

### Assignment

```python
# a is the name, 2 is the value
# the name "a" is bound to the value 2
a = 2

# the name a is rebound to the value 3
a = 3

# Python keeps track of how many names are bound to a value
class Toaster:
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

## Python is fully dynamic and everything is an object

❓ Questions to ask orally:

- Is a class an object?
- Is a function an object?
- Is an exception an object?
- Is a module an object?

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
Toaster.__name__
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

# Exception are objects!
try:
    raise ValueError("hello")
except ValueError as e:
    print(e)
    dir(e)


# You can return class and function just like any other object
def get_class_and_function():
    def func():
        return 1

    class MyClass:
        pass

    return func, MyClass


# ImportError can happen anywhere and can be caught
try:
    import toaster
except ImportError:
    toaster = None

# You can programmatically import
import importlib

toaster = importlib.import_module("toaster")
```

See also:

- https://docs.python.org/3/library/inspect.html

## The standard library

See:

- https://docs.python.org/3/tutorial/stdlib.html
- https://docs.python.org/3/tutorial/stdlib2.html

## Navigating the Python documentation

https://docs.python.org/3/

- builtin vs. standard lib

## Python "gotchas"

- Mutable default arguments
- Circular module dependencies
- Clashes with builtin naming (e.g. `id`)
- String identity
- Identity (`is`) vs. equality (`==`)
- Late binding closures
- Tuple by default `a = "b",`
- `sort` vs. `sorted`

## What's next?

Next course: [Python style](./03-the-style.md)

See [my course on advanced Python](../advanced-python/).

- Context (`with`)
- Iterators
- Generators
- Operator overloading
- Magic methods
- Descriptors
- Properties
- Decorators
- Useful builtin packages: `dataclasses`
- Walrus (`:=`) operator
- `is not` (a single binary operator) vs. `is (not ...)` (`is` and `not` are separated)

## Self-review

❓ Questions to ask orally:

- What are the base types?
- What are the container types?
- How do you get the length of a list?
- How do you check if a key is in a dict?
- How do you get a value from a dict? Even if it's not there?
- How do you iterate over a dict's `key, value` in a `for` loop?
- How do you coerce as a string? As a boolean?
- How can you write a switch in Python?
    - `dict`
    - `if... elif... else`
- What's the difference between equality and identity? What are the operators?
- How do you count from 1 to 10?
- How do you type a function?
- How do function arguments work?
- How do you write a class? With a constructor? With a class method? With inheritance?
- How do you export a function from a module?
- In what sense can we say that Python is a dynamic language?

## References

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Python Cheatsheet](https://www.pythoncheatsheet.org/)
- [Memento Python](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)
- [satwikkansal/wtfpython: What the f*ck Python?](https://github.com/satwikkansal/wtfpython)
