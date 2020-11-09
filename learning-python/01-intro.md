# Python: intro

## Why learn Python

- It's pervasive
- It's here too stay (hiring)
- It's super versatile and you can use it for almost anything
    - Server-side and client-side
    - ML & NLP
    - CLI scripts and full apps
- It's simple
- Its philosophy can help you become a better programmer, whatever your language

## Python pros & cons

Pros:

- Has been fully battle-tested (created in 1991, 4 years before Java, 3 years before Python)
- Supports numerous paradigm, including OOP and FP
- Focuses on readability (i.e. conciseness)
- Fostered by a welcoming community
- Has very few gotchas compared to JS and PHP
- Embraces its dynamic nature to build very concise DSLs

Pro or con? It depends on use case and viewpoint.

- Can be slow
    - But: not applicable for I/O
    - But: slow parts of the code can be written in C
    - But: PyPy has a JIT
- No static types (Python has dynamic strong typing)
- Jack of trades and master of none? Some paradigms (e.g. FP and OOP) are not fully implemented.
- Some advanced features can be misused when put in the wrong hands (e.g. metaclasses, descriptors).
- Concurrency API (a matter of taste)
- Lots of features added those last days
- Many things are statement where they could be expression

## What we will see

- Syntax
- Tooling: pyenv, pipenv, poetry, dependency management, etc.
- Constructs: lambda, list/dict/set comprehensions
- Building a CLI tool

## Myths about Python

- Python is a weakly typed language
- Python is not compiled

## Starting from first principles: the Zen of Python

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

## Resources

- [charlax/python-education: Reading list for ramping up with professional Python](https://github.com/charlax/python-education) 
- [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/) 