# Learning Python the language

## Intro

- Indentation and spacing are syntax in Python
- Python favours shorter, explicit name
    - `s.upper()` (Python) vs. `s.toUpperCase()` (JS)
- Python has very few keywords and constructs. E.g. no `switch`, no `do... while`.

## Syntax

This part focuses on the syntax.

- Base types: `int`, `float`, `bool`, `str`, `bytes`
- Container types: `list` (literal: `[]`), `tuple` (`()`), `dict` (`{"key": "value"}`), `set` (`{1, 2, 3}`), `frozenset`.
- Variable assignment (`a = 1`, `a = b = 1`, `a += 1`)
- Sequence containers indexing: `l[start slide:end slide:step]`
- Boolean logic: `>`, `and`, `or`, `not`
- Imports `import x` vs. `from x import y`
- Conditional statement: `if... else`
- Exceptions: `raise`,  `try... except... finally... else...`
- Conditional loop: `while`
- Iterative loop: `for i in sequence:`
- Display and input: `print`, `input("question?")`
- Operation on containers: `len`, `min`, `sorted`, `enumerate`, `zip`, `all`, `any`, `reversed`
- Operation on lists: `l.append`, `l.extend`, `l.insert(index, val)`, `l.remove(val)`, `l.pop([index])`, `l.sort()` (in place), `l.reverse()`
- Operations on dictionaries: see below
- Operations on set: see below
- Operations on strings: see below
- Files: see below
- Sequence: `range([start], end, step)`

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
    print("hello world")
```

```python

# x, y, z are positional arguments
# args are the rest positional arguments (list)
# a, b are keyword arguments
# kwargs are the rest keyword arguments (dict)

def hello(x, y, z, *args, *, a=1, b="2", **kwargs):
    pass
```

## Defining a class

```python
class Toaster:
    pass
```

## Files

## References

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Python Cheatsheet](https://www.pythoncheatsheet.org/) 
- [Memento Python](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)