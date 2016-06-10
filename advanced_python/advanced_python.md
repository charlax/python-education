<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
# Table of Contents

- [Introduction to Advanced Python](#introduction-to-advanced-python)
  - [Presentation](#presentation)
  - [Introduction](#introduction)
  - [Prerequisite](#prerequisite)
  - [Object Oriented Programming](#object-oriented-programming)
    - [Metaclasses](#metaclasses)
      - [What are they?](#what-are-they)
      - [Use cases](#use-cases)
      - [Further reading](#further-reading)
    - [Special methods](#special-methods)
      - [What are they?](#what-are-they-1)
      - [Use cases](#use-cases-1)
      - [Further reading](#further-reading-1)
    - [Descriptors and properties](#descriptors-and-properties)
      - [What are they?](#what-are-they-2)
      - [Use cases](#use-cases-2)
      - [Further reading](#further-reading-2)
    - [Context Managers](#context-managers)
      - [What are they?](#what-are-they-3)
      - [Use cases](#use-cases-3)
      - [Further reading](#further-reading-3)
  - [Functional Programming](#functional-programming)
    - [Decorators](#decorators)
      - [What are they?](#what-are-they-4)
      - [Use cases](#use-cases-4)
      - [Further reading](#further-reading-4)
    - [List, dict, set comprehensions](#list-dict-set-comprehensions)
      - [What are they?](#what-are-they-5)
      - [Use cases](#use-cases-5)
      - [Further reading](#further-reading-5)
    - [Iterators](#iterators)
      - [What are they?](#what-are-they-6)
      - [Use cases](#use-cases-6)
      - [Further reading](#further-reading-6)
    - [Generators](#generators)
      - [What are they?](#what-are-they-7)
      - [Use cases](#use-cases-7)
      - [Further reading](#further-reading-7)
    - [The itertools module](#the-itertools-module)
      - [What is it?](#what-is-it)
      - [Use cases](#use-cases-8)
      - [Further reading](#further-reading-8)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Introduction to Advanced Python

The goal of this article is to broaden your knowledge of Python, exploring some concepts and techniques you might have never heard about. I won't go into too much detail, the goal is only to inspire you to research those features and patterns.

*Note: all examples are run with Python 3.4*

## Presentation

This is also available as a [presentation](http://www.slideshare.net/charlax/introduction-to-advanced-python). The source of this presentation can be found in this repo.

## Introduction

Python's elegance can be attributed to the language's uncompromising focus on *readability*. Most of the design choices are discussed based on the fundamental premise that a programming language is first made to be read by human beings. That's probably why writing Python sometimes feels like writing English.

That's also the raison d'être behind a lot of the advanced Python concepts introduced here - you should use them when they objectively make the code more readable. You should definitely not use them "when you feel like it". Metaclasses, decorators, context, iterators... should be conscious choices that improve the code's readability.

For a refresher of Python's design principles, run `import this` in the Python interpreter:

```reStructuredText
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
```

## Prerequisite

This article assumes knowledge of those core Python concepts:

* Core syntax and programming constructs
* Basic differences between Python 2 and Python 3
* Modules
* Everything is an object

If you don't understand one of those concepts, or feel rusty, you should revisit it before carrying with the rest of the article.

## Object Oriented Programming

### Metaclasses

#### What are they?

A metaclass is just the class (or the type) of a class.

In Python, even classes are object.

```python
>>> class LaClasse(object):
...     pass
>>> LaClasse
<class '__main__.LaClasse'>
```

Classes are instances of `type`:

```python
>>> type(LaClasse)
<class 'type'>
>>> isinstance(LaClasse, type)
True
```

The builtin function `type` can be also used to create new classes on the fly.  The first argument is the class name, the second one the base classes, the last one the class attributes.

```python
>>> LaClasse = type("LaClasse", (object, ), {})
>>> LaClasse
<class '__main__.LaClasse'>
```

Python uses type to create classes. So the class of a class is `type`, or, in other words, the metaclass of classes is `type`. Because this is the default, the following does nothing different from what Python would have done. It just says that the class Toaster's class is type:

```python
>>> class Toaster(object):
...     __metaclass__ = type
```

So a basic way to use metaclass would be (note: the syntax is a bit different in Python 2):

```python
>>> def prepend_class_name(name, bases, attr):
...     new_attr = {}
...     for key, value in attr.items():
...         new_attr[name.lower() + "_" + key] = value
...     return type(name, bases, new_attr)
...
>>> class Toaster(metaclass=prepend_class_name):
...     color = "red"
...
>>> Toaster.color
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Toaster' has no attribute 'color'
>>> Toaster.toaster_color
'red'
```

#### Use cases

As Tim Peters puts it, "Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don't." That being said, there's some very legitimate use cases for metaclasses:

* Use the class as a way for developer to configure something. This is how ORM such as SQLAlchemy allow you to use a class to define the table, the mapper and the class all at one (see the documentation about its [declarative extension](http://docs.sqlalchemy.org/en/rel_0_9/orm/extensions/declarative.html)).
* Add some logic after a class has been defined: verify that some methods/attributes are present, automatically apply decorators, etc.

#### Further reading

* StackOverflow, [What is a metaclass in Python](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python)
* Python Docs, [Customizing class creation](http://docs.python.org/3.3/reference/datamodel.html#customizing-class-creation)

### Special methods

#### What are they?

Python allows operator overloading by allowing classes to override methods with special names. For instance:

```python
>>> class Toaster(object):
...     def __init__(self, number_of_slots):
...             self.number_of_slots = number_of_slots
...     def __lt__(self, other):
...             return self.number_of_slots < other.number_of_slots
...
>>> Toaster(3) < Toaster(4)
True
```

In this example, we have defined a way to compare whether a toaster is lower than another one.

Pretty much every operation can be redefined. Object identity (`is`) cannot be overridden though (`Toaster is Toaster`). 

Here's a list of the main operations:

* `__repr__`: official string representation of an object. Typically used to ease debugging.
* `__lt__`, `__le__`, `__eq__`...: rich comparison methods. Note that you can use `functools.total_ordering` so that you don't have to define all of them to allow all the possible rich comparison operations.
* `__bool__`: when doing truth value testing.
* `__getattr__`, `__setattr__`, `__delattr__`: respectively used for attribute lookup, assignment and deletion.
* `__call__`: called when the instance is called as a function.
* Container type emulation
  * `__len__`: called with `len()`
  * `__getitem__`, `__setitem__`, `__delitem__`: respectively used for evaluation, assignment and deletion of `self[key]`.
  * `__contains__`: called with `item in self`.
* Numeric types emulation: `__add__`, `__sub__`, `__mul__`... Also includes the augmented arithmetic assignments (`+=`, `-=`...): `__iadd__`, `__isub__`...)

#### Use cases

Overriding special methods lets you write much more readable code. Let's imagine we want to compare two cards:

```python
import functools


@functools.total_ordering
class Card(object):
    _order = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

    def __init__(self, rank, suite='hearts'):
        assert rank in self._order
        self.rank = rank
        self.suite = suite

    def __repr__(self):
        return '<Card %s of %s>' % (self.rank, self.suite)

    def __lt__(self, other):
        return self._order.index(self.rank) < self._order.index(other.rank)

    def __eq(self, other):
        return self.rank == other.rank

ace_of_spades = Card('A', 'spades')
eight_of_hearts = Card(8, 'hearts')

assert ace_of_spades > eight_of_hearts
```

This code is arguably much easier to read and keeps the logic of how to compare two cards encapsulated in the class.

Another interesting use cases is how SQLAlchemy is able to have the following work:

```python
session.query(Toaster.name == 'the_name')
```

The reason this works is that `Toaster.name` overloads the `__eq__` special method to return a specific comparator object (this is hugely simplified, but that's the basic idea).

#### Further reading

* Python docs, [Data model](http://docs.python.org/3.3/reference/datamodel.html)
* Rafe Kettler, [A Guide to Python's Magic Methods](http://www.rafekettler.com/magicmethods.html)

### Descriptors and properties

#### What are they?

The basic idea is that descriptors are reusable properties. This might sound quite confusing, so let's start with a very simple example:

```python
CACHE = {
    'toaster1': {'color': 'red', 'brand': 'noname'},
}


class CachedObject(object):

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return CACHE[instance.key][self.name]

    def __set__(self, instance, value):
        CACHE.get[instance.key][self.name] = value


class Toaster(object):
    color = CachedObject('color')
    brand = CachedObject('brand')

    def __init__(self, key):
        self.key = key


toaster = Toaster('toaster1')
assert toaster.color == 'red'
assert toaster.brand == 'noname'
toaster.color = 'blue'
assert toaster.color == 'blue'
```

In this example, descriptors let us define some behavior once (i.e. where to get the data from), and reuse for two different attributes. Descriptors only work as class attribute and define one or multiple of the following methods:

* `__get__(self, instance, owner)` where `instance` is the instance it's called on and can be `None` if it's called on the class, and `owner` the class.
* `__set__(self, instance, value)` for overriding attribute assignment.
* `__del__(self, instance)` for overriding attribute deletion (with `del`).

Properties (usually created by decorating a method with the `property` builtin function) are a simpler and more pervasive way of using descriptors. They're defined in `Objects/descrobject.c` in the CPython code.

The function's signature is: `property(fget=None, fset=None, fdel=None, doc=None)`, where `fget` is the attribute getter, `fset` the setter, `fdel` the deleter and `doc` the docstring. `property` can also be used as a decorator.  Once it's applied, it exposes a `getter`, `setter` and `deleter` method that can also be used as decorators. Those two ways are completely identical:

```python
class Toaster(object):

    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = color

    def del_color(self):
        raise AttributeError("can't delete attribute")

    color = property(get_color, set_color, del_color)

toaster = Toaster('red')
assert toaster.color == 'red'


class Toaster(object):

    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def set_color(self, value):
        self._color = color

    @color.deleter
    def del_color(self):
        raise AttributeError("can't delete attribute")

toaster = Toaster('red')
assert toaster.color == 'red'
```

#### Use cases

Property are very often use to create readonly attributes, defining only the getter:

```python
import pytest


class Toaster(object):

    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color


toaster = Toaster('red')
assert toaster.color == 'red'

with pytest.raises(AttributeError):
    toaster.color = 'blue'
```

Descriptors themselves are rarely used. Notable uses include SQLAlchemy's `ColumnDescriptor`.

#### Further reading

* Python docs, [Implementing descriptors](http://docs.python.org/3.3/reference/datamodel.html#implementing-descriptors)
* Python docs, [property](http://docs.python.org/3.3/library/functions.html#property)
* Chris Beaumont, [Python Descriptors Demystified](http://nbviewer.ipython.org/urls/gist.github.com/ChrisBeaumont/5758381/raw/descriptor_writeup.ipynb)
* Alex Munroe, Fuzzy Notepad, [Python FAQ: Descriptors](http://me.veekun.com/blog/2012/05/23/python-faq-descriptors/)

### Context Managers

#### What are they?

Context managers are used with the `with` statement. They let you define code that is run before and after the block. You could achieve the same result with `try... except... finally` but a `with` block can be more readable and provide some more flexibility. The canonical example is probably the following:

```python
with open("/etc/resolv.conf") as f:
    print(f.read())

# Is **roughly** equivalent to:

try:
    f = open("/etc/resolv.conf")
    print(f.read())
finally:
    f.close()
```

In the first example, `f.close()` is omitted because `open` can be used directly (as in the second example), but also as a context manager. In the latter case, it will handle closing automatically. This behavior is defined in `Lib/_pyio.py`:

```python
class IOBase(metaclass=abc.ABCMeta):
    ...

    def __exit__(self, *args):
        """Context management protocol.  Calls close()"""
        self.close()
```

There's multiple ways to define a context manager. The most explicit one is to create an object that has the `__enter__()` and `__exit__(exc_type, exc_val, exc_tb)` methods. The `contextlib` module also provides a more functional way to define them. Here's two equivalent examples.

Class-based way:

```python
class assert_raises(object):
    """Assert that an exception is raised."""

    def __init__(self, exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        print("Enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        if not exc_type:
            raise AssertionError("No exception raised")
        if not issubclass(exc_type, self.exceptions):
            raise AssertionError("Exception %r raised" % exc_type)

        # From the doc:
        # Returning a true value from this method will cause the with
        # statement to suppress the exception and continue execution
        # with the statement immediately following the with statement.

        return True


with assert_raises(ValueError):
    raise ValueError("Whatever")
```

Function-based way:

```python
from contextlib import contextmanager


@contextmanager
def assert_raises(exceptions):
    """Assert that an exception is raised."""
    print("Enter")
    try:
        yield
    except Exception as exc:
        print("Exit")
        if not isinstance(exc, exceptions):
            raise AssertionError("Exception %r raised" % exc_type)
    else:
        raise AssertionError("No exception raised")


with assert_raises(ValueError):
    raise ValueError("Whatever")
```

#### Use cases

The [`contextlib`](http://docs.python.org/3/library/contextlib.html) module provides a lot of interesting use cases for context managers:

* `closing`: closes something upon completion
* `suppress`: suppresses specific exceptions
* `redirect_stdout`

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('somefile.tmp')
```

SQLAlchemy's [`Session.begin()`](http://docs.sqlalchemy.org/en/latest/orm/session.html#sqlalchemy.orm.session.Session.begin) is a context manager. You could imagine a lot of other use cases: Redis pipelines, wrapping SQL transactions, etc.

```python
from contextlib import contextmanager

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def run_my_program():
    with session_scope() as session:
        ThingOne().go(session)
        ThingTwo().go(session)
```

Here's how a reds pipeline command can be created using [redis-py](https://github.com/andymccurdy/redis-py):

```python
with redis_client.pipeline() as pipe:
    pipe.set('toaster:1', 'brioche')
    bread = pipe.get('toaster:2')
    pipe.set('toaster:3', bread)
```

#### Further reading

* Python docs, [The `with` statement](http://docs.python.org/3.4/reference/compound_stmts.html#with)
* Python docs, [Context Manager Types](http://docs.python.org/3.4/library/stdtypes.html#context-manager-types)
* Python docs, [`contextlib`](http://docs.python.org/3.4/library/contextlib.html)

## Functional Programming

Even though `object` are first class citizen in Python, the language can totally be used in a more functional way.

### Decorators

#### What are they?

Decorator are nothing complicated. They're just syntactic sugar.

```python
def function():
    pass

function = decorate(function)

# is exactly equivalent to:

@decorate
def function():
    pass
```

Now what is `decorate`? Let's think about the behavior it needs to have:

* It takes a function as its single arguments.
* It returns a function (or more generally a callable).

Here's the simplest possible decorator (which does not do anything:

```python
def decorate(function):
    return function
```

Not terribly useful. Let's create a decorator that will return `None` if the function raises an exception.

```python
import functools


def silence_exception(function):

    # The 'wraps' decorator just copies the docstring and function name.
    # It eases debugging.

    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            # Equivalent to returning None
            return

    return wrapped


@silence_exception
def toast(bread):
    if bread == 'baguette':
        raise ValueError("Scandalous!")
    return "toasted"


assert toast('croissant') == 'toasted'
assert toast('baguette') is None
```

That's it! Decorator lets you very easily *decorate* (i.e. add behavior) to a function.

By the way: the example above can be considered an anti-pattern. There's almost never a good reason to silence exceptions this way.

How would you change the decorator's behavior? You would need to write a decorator maker instead. Let's think about what kind of behavior this decorator maker will have:

* It takes some arguments that change the decorator's behavior..
* It returns a decorator, i.e. something that takes a function as its single argument, and return another callable.

Let's make the simplest possible decorator maker:

```python
def decorater_maker():
    def decorator(function):
        return function
    return decorator


@decorator_maker()  # Note the function call here "()"
def function():
    pass
```

Note that we **call** `decorator_maker`, because we need it to return the decorator. Now, let's see a more useful example:

```python
# This the decorator factory. It returns a decorator.
def silence_exception(exceptions):
    """Create a decorator to ignore some exceptions."""

    # This is the actual decorator. It returns the wrapped function.
    def decorator(function):
        """Ignore some exceptions."""

        # This is the 'new' function. It returns whatever the original
        # function returns, or None on specific exceptions.
        @functools.wraps(function)
        def wrapped(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except Exception as exception:
                # Raise exceptions that are not in the list. `isinstance`
                # accepts a single object or a container.
                if not isinstance(exception, exceptions):
                    raise

        return wrapped

    return decorator


class Champagne(object):
    pass


@silence_exception(ValueError)
def toast(bread):
    """Toast some bread."""
    if isinstance(bread, Champagne):
        raise TypeError("Are you crazy?")
    if bread == 'baguette':
        raise ValueError("Scandalous!")
    return "toasted"


assert toast('croissant') == 'toasted'
assert toast('baguette') is None
with assert_raises(TypeError):
    toast(Champagne())
```

Note that this is effectively reinventing `contextlib`'s simpler `suppress` context manager:

```python
class suppress:
    """Context manager to suppress specified exceptions

    After the exception is suppressed, execution proceeds with the next
    statement following the with statement.

         with suppress(FileNotFoundError):
             os.remove(somefile)
         # Execution still resumes here if the file was already removed
    """

    def __init__(self, *exceptions):
        self._exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):
        return exctype is not None and issubclass(exctype, self._exceptions)
```

Decorators can also be applied to class. There's not much difference in the behavior:

```python
@decorator
class Foo:
    pass
```

Is equivalent to:

```python
class Foo:
    pass
Foo = decorator(Foo)
```

Since the class object `Foo` is just an object, I'll let as an exercise to the reader to imagine what you can do with a class decorator.

#### Use cases

Decorators are an extremely versatile tool. Here's some examples:

* Celery uses them to define tasks from Python functions.
* Flask uses them to attach routing metadata (such as method and URL) to Python functions.
* Flask-cache uses them to cache the result of functions. It hashes the parameters to get the caching key.
* Mock uses them to define the context in which a specific object will be mocked.
* SQLAlchemy uses them for all sorts of different use. One of the most interesting one is `hybrid_attribute`, which basically lets you define an attribute once that can be used both as a class attribute and as an instance attribute.

#### Further reading

* Python docs, [Function definitions](http://docs.python.org/3/reference/compound_stmts.html#function-definitions)
* StackOverflow, [How can I make a chain of function decorators in Python?](http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python/1594484#1594484)

### List, dict, set comprehensions

#### What are they?

Just a simpler way to define list/dict/set:

```python
>>> [str(i) for i in range(4)]
['0', '1', '2', '3']
>>> {key: str(key) for key in range(4)}
{0: '0', 1: '1', 2: '2', 3: '3'}
>>> {i % 2 for i in range(10)}
{0, 1}
```

Note that they can be nested as well:

```python
>>> [[(i, j) for i in range(2)] for j in range(2)]
[[(0, 0), (1, 0)], [(0, 1), (1, 1)]]
```

This is just an example - the `itertools` module provides simpler ways to do this.

#### Use cases

List/dict/set comprehensions can provide a more readable way to create simple list, especially for math.

They lower the readability when used for complex data structures, in which case it's usually better to use a plain loop.

```python
>>> my_dict = {str(i): [j % 2 for j in range(i)] for i in range(2)}
>>> my_dict2 = {}
>>> for i in range(2):
...     value = []
...     for j in range(i):
...         value.append(j % 2)
...     my_dict2[str(i)] = value
>>> my_dict == my_dict2
True
```

This is just an example but sometimes it's a better idea to be more verbose.

#### Further reading

* Python docs, [Data Structures](https://docs.python.org/3.4/tutorial/datastructures.html#data-structures)

### Iterators

#### What are they?

What's an iterator? It's a class that can be iterated upon. Iterator objects define the method `__next__()` (`next` in Python 2) which will be called for each iteration, raising `StopIteration` when it's finished.

Note that when you do a `for` loop over a container, the container is guaranteed to be the iterator. Python first calls `iter()` over the container (which effectively calls the `__iter__()` magic method on the object), and use the returned object as the iterator. In practice, most objects return themselves in `__iter__()` and override the `__next__()` method.

Here's a very simple iterator:

```python
>>> class Toaster(object):
...    def __init__(self):
...        self.toasts = [0, 1]
...        self._index = 0
...
...    def __iter__(self):
...        return self
...
...    def __next__(self):
...        try:
...            returned = self.toasts[self._index]
...        except IndexError:
...            raise StopIteration
...
...        self._index += 1
...        return returned

>>> for toast in Toaster():
...    print(toast)
0
1
```

Let's use the `dis` module, which lets you disassemble Python to see what's going on:

```python
>>> import dis
>>> def over_list():
...     for i in None: pass
...
>>> dis.dis(over_list)
  2           0 SETUP_LOOP              14 (to 17)
              3 LOAD_CONST               0 (None)
              6 GET_ITER
        >>    7 FOR_ITER                 6 (to 16)
             10 STORE_FAST               0 (i)
             13 JUMP_ABSOLUTE            7
        >>   16 POP_BLOCK
        >>   17 LOAD_CONST               0 (None)
             20 RETURN_VALUE
>>> over_list()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in over_list
TypeError: 'NoneType' object is not iterable
```

Obviously this would never have worked but the most interesting part is that we can verify what we just said: Python calls `iter` on the object (`GET_ITER`), and then calls (`FOR_ITER`) on its result. Another way to verify that:

```python
>>> iter(None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'NoneType' object is not iterable
```

#### Use cases

Iterators provide a very clean way to support looping over some content. You could imagine having a class that gives a simpler access to a list of resources:

```python
>>> def get_api_resource(url):
...     """Return an API resource."""
...     if url.endswith("2"):
...         # This is purely arbitrary and so that this function ends
...         return
...     return "found " + url

>>> class Toasters(object):
...     """Loop through toasters."""
...     def __init__(self):
...         self.index = 0
...
...     def __next__(self):
...         resource = get_api_resource("/toasters/" + str(self.index))
...         self.index += 1
...         if resource:
...             return resource
...         raise StopIteration
...
...     def __iter__(self):
...         return self

>>> for resource in Toasters():
...     print(resource)
found /toasters/0
found /toasters/1
```

Iterator are in particular used for lazy evaluation, so that you compute the results one by one instead of computing all of them. This brings some interesting performance improvement: you might not want all results or do not want to suffer the cost of computing all results when you might raise an exception in the middle.

They're also useful for unbounded sets of results (where, by definition, you can't compute all the results beforehand).

#### Further reading

* Python docs, [Iterators](https://docs.python.org/3.4/tutorial/classes.html#iterators)

### Generators

#### What are they?

To simplify, they're just a simple way to create an iterator using a function instead of a class.

If we were to re-implement the `ApiResources` class from above, we could it do this way:

```python
>>> def get_toasters():
...    while True:
...        resource = get_api_resource("/toasters/" + str(index))
...        if not resource:
...            break
...        yield resource
>>> for resource in get_resources():
...     print(resource)
found /toasters/0
found /toasters/1
```

This is arguably much more readable. Here's the interesting piece:

```python
>>> type(get_resources)
<class 'function'>
>>> type(get_resources())
<class 'generator'>
```

What this means is that while `get_resources` is a function, it returns a `generator` type. Now it's important to take a step back and think about the difference between `return` and `yield`.

* When a function does a `return`, it's completely relinquishing the control of execution.
* When it does a `yield`, it temporarily passes on the control of execution, keeping its state between calls. In the example above, the variable `index` is stored between calls.

Let's see if we can verify this using the `inspect` module, which provides useful functions to get more insights into live objects.

```python
>>> import inspect
>>> gen = get_resources()
```

At this point, we just got the generator and we haven't started generating, which means that nothing has been run yet:

```python
>>> inspect.getgeneratorlocals(gen)
{}
```

We can use the `next()` builtin to manually advance to the next iteration and see that the generator now has two local variables that are stored: `index` and `resource`:

```python
>>> next(gen)
'found /toasters/0'
>>> inspect.getgeneratorlocals(gen)
{'index': 0, 'resource': 'found /toasters/0'}
>>> next(gen)
'found /toasters/1'
>>> inspect.getgeneratorlocals(gen)
{'index': 1, 'resource': 'found /toasters/1'}
```

Note that generators do not return the implicit `None` that you're used to.  Instead, they raise `StopIteration` to comply with the iteration protocol:

```python
>>> next(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

What happens if you mix `return` and `yield`? In that case, `return <something>` will just be equivalent to `raise StopIteration(<something>)`, which means that this will end the generator.

Generator expression can be used for simple generators:

```python
>>> toasters = (get_api_resource("/toasters/%d" % i) for i in range(2))
>>> toasters
<generator object <genexpr> at ...>
```

Note that `toasters` is a generator, not a list. List comprehensions use `[]`:

```python
>>> toasters_list = [get_api_resource("/toasters/%d" % i) for i in range(2)]
>>> toasters_list
['found /toasters/0', 'found /toasters/1']
```

As we explained, generators' main interest is that they are evaluated lazily one by one, which is why `toasters` has not yet evaluated all its resources, while `toasters_list` has. This brings an interesting memory optimization: the list comprehension instantiates all the objects, which might require a lot of memory. In the generator case though, objects are instantiated one by one, and forgotten immediately (provided nothing else retains a reference).

Note that you can evidently force evaluation of all the iterator's items with the `list()` constructor, which accepts an iterable and will construct a list from it:

```python
>>> list(toasters)
['found /toasters/0', 'found /toasters/1']
```

#### Use cases

Generator are just iterators, so their use cases are the same.

#### Further reading

* Python docs, [Generators](https://docs.python.org/3.4/tutorial/classes.html#generators)
* Python docs, [Generator expressions](https://docs.python.org/2/reference/expressions.html#generator-expressions)
* [PEP 255: Simple Generators](http://legacy.python.org/dev/peps/pep-0255/)
* [PEP 289: Generator Expressions](http://legacy.python.org/dev/peps/pep-0289/)
* [PEP 380:	Syntax for Delegating to a Subgenerator](http://legacy.python.org/dev/peps/pep-0380/)
* Jeff Knupp, [Improve Your Python: 'yield' and Generators Explained](https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)

### The itertools module

#### What is it?

From the documentation:

    This module implements a number of iterator building blocks inspired by
    constructs from APL, Haskell, and SML. Each has been recast in a form
    suitable for Python.

    The module standardizes a core set of fast, memory efficient tools that are
    useful by themselves or in combination. Together, they form an “iterator
    algebra” making it possible to construct specialized tools succinctly and
    efficiently in pure Python.

There's three main categories:

* Infinite: `count`, `cycle`, `repeat`
* Finite: `accumulate`, `chain`, `chain.from_iterable`, `compress`, `dropwhile`, `filterfalse`, `groupby`, `islice`, `starmap`, `takewhile`, `tee`, `zip_longest`
* Combinatoric: `product`, `permutations`, `combinations`, `combinations_with_replacement`

#### Use cases

`itertools` can represent a huge boost in developer productivity. Imagine that you can construct very complex iterator out of the core building blocks this module provides.

For instance, let's say you want to generate all permutations in the order of cards for a straight flush. No need to reinvent the wheel... `itertools` has a handy `permutations` iterator:

```python
>>> all = list(itertools.permutations([Card('A'), Card('K'), Card('Q'), Card('J'), Card(10)])
>>> all
[(<Card A of hearts>,
  <Card K of hearts>,
  <Card Q of hearts>,
  <Card J of hearts>,
  <Card 10 of hearts>),
 (<Card A of hearts>,
  <Card K of hearts>,
  <Card Q of hearts>,
  <Card 10 of hearts>,
  <Card J of hearts>),
  ...
]
>>> len(all)
120
```

#### Further reading

* Python docs, [itertools](https://docs.python.org/3/library/itertools.html)
