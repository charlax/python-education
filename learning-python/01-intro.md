# Python: intro

<!--TOC-->

- [Python: intro](#python-intro)
  - [Why learn Python](#why-learn-python)
  - [Python pros & cons](#python-pros--cons)
  - [What we will see](#what-we-will-see)
  - [Myths about Python](#myths-about-python)
  - [Starting from first principles: the Zen of Python](#starting-from-first-principles-the-zen-of-python)
  - [Things to unlearn](#things-to-unlearn)
  - [Python glossary](#python-glossary)
  - [Resources](#resources)

<!--TOC-->

Why happy:

- Cool to relearn stuff
- Python is a joy to work with

## Why learn Python

❓ Questions to ask orally:

- Where is Python used?
- What can you use Python for?

Answers:

- It's pervasive.
- It's here too stay (hiring, teaching kids)
- It's super versatile and you can use it for almost anything
    - Server-side and client-side
    - CLI scripts and full apps
    - Web dev
    - Data analysis
    - IoT
    - Computer vision, machine learning, NLP
    - Game dev
    - Sys admin
    - Cybersecurity
    - Testing
    - Network
    - GUI
- It's simple
    - There are almost no gotchas.
- Its philosophy can help you become a better programmer, whatever your language

## Python pros & cons

❓ Questions to ask orally:

- What are the pros & cons of Python?

Pros:

- Has been fully battle-tested (created in 1991, 4 years before Java, 3 years before PHP).
  - So many tools.
  - So much experience deploying and monitoring it.
- Supports numerous paradigm, including OOP and FP
- Focuses on readability (i.e. conciseness). You can get A LOT done with very few lines of code.
- Fostered by a welcoming community
- Has very few gotchas compared to JS and PHP
- Embraces its dynamic nature to build very concise DSLs
- Comes "batteries included": its standard lib is very complete, well designed and well documented
- Has a vibrant ecosystem: there is a pip package for almost everything in Python.
- Portable: runs on almost all OSes.

Pro or con? It depends on use case and viewpoint.

- Can be slow
    - But: not applicable for I/O
    - But: slow parts of the code can be written in C
    - But: PyPy has a JIT
- No static types (Python has dynamic strong typing).
    - There are tools (mypy) to add type checking, but there's not fully integrated into the process yet.
- Jack of all trades and master of none? Some paradigms (e.g. FP and OOP) are not fully implemented.
- Some advanced features can be misused when put in the wrong hands (e.g. metaclasses, descriptors).
- Concurrency API (a matter of taste)
- Lots of features added those last days
- Many things are statement where they could be expression
- Packaging
- GIL (global interpreter lock) means that only one thread can run the code (in CPython)

## What we will see

First session:

- Syntax
- Constructs: lambda, list/dict/set comprehensions

Later sessions:

- Tooling: pyenv, pipenv, poetry, dependency management, etc.
- Building a CLI tool
    - Walkthrough solutions
- Building a simple web API

## Myths about Python

❓ Questions to ask orally:

- Have you heard about "..."?
- What do you think about it.

Myths about Python:

- Python does not scale
    - Uber API: about 400k lines of code (on top of the Pyramid web framework)
    - Sentry
- Python is a weakly typed language
    - "static" vs "dynamic" typing (vs. C)
    - "weak" vs "strong" typing (vs. Perl)
- Python is not compiled
    - The Python VM
- Python is single-threaded
    - CPython has the GIL but multi-threaded (see [Understanding the Python GIL](http://www.dabeaz.com/GIL/), especially the presentation)
    - Python spec vs. Python implementation (CPython, PyPy, Jython, IronPython)
    - There are other ways to achieve concurrency: processes

## Starting from first principles: the Zen of Python

❓ Questions to ask orally:

- Have you heard about the Zen of Python?
- Have you heard about "pythonic"?

```
In [1]: import this
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

The most important ones:

- **Readability counts.**
- Explicit is better than implicit.
- Simple is better than complex. Complex is better than complicated.
- There should be one -- and preferably only one -- obvious way to do it

Those are not included but also important:

- Ask for forgiveness, not for permission (e.g. there are no real private variables in classes in Python).
- With great powers come great responsibility
- Principle of least surprise

## Things to unlearn

Learning a new language requires unlearning some stuff. Those items are mostly for PHP/JS developers.

- Heavy/fancy solution
    - Python favors simple solutions
    - Python developers are very strict about readability and simplicity
- Heavy OOP style
    - Python favors simple OOP style
    - Python does not support strict OOP: there are no private variables, for instance.
- Features that are only necessary in statically typed languages
    - There is no real need for a dependency injection framework in Python (the pattern is fine though)
    - There are no interfaces.
- OOP is not the solution to all problems.
    - Python usually prefer simple functions (KISS).
- You absolutely need Docker.
    - Python on bare metal is fine. There are ways to isolate from the local env.
- Any programming style is fine
    - Python is a very opinionated language, there is usually a single best way
      to something in Python, and usually it's the simplest way.

> “Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.”

― Antoine de Saint-Exupéry

## Python glossary

- PEP: Python Enhancement Proposal = RFC

## Resources

- [charlax/python-education: Reading list for ramping up with professional Python](https://github.com/charlax/python-education)
- [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/)
- https://repl.it/
