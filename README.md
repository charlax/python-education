Ramping up with professional Python
===================================

Beginner
--------

* [Learn Python the Hard Way](http://learnpythonthehardway.org/book/): slow
  introduction, suitable for people with limited programming language
  experience.
* [Dive Into Python](http://www.diveintopython.net/toc/index.html): much faster
  introduction to Python, a bit outdated but will get you ramped up really
  fast, especially if you've learned a number of programming language in the
  past. There's a version for [Python 3](http://www.diveinto.org/python3/) as
  well.
* [Official Tutorial](https://docs.python.org/2/tutorial/index.html): Python's
  official doc is really good, highly recommended read.

[The Python Guide](http://docs.python-guide.org/en/latest/intro/learning/) has
some other good resources.

Learning to write idiomatic Python
----------------------------------

First things first, let's get code styling out of the way. Make sure you've
read an memorized [PEP8](https://www.python.org/dev/peps/pep-0008/) (code
style) and [PEP257](https://www.python.org/dev/peps/pep-0257/) (docstring
style). Those two code styles are applied by almost all major Python
applications and libraries.

What is called "idiomatic Python" might feel magical at first, especially if
you don't know Python. I'd recommend getting your hands dirty with some real
world Python code. Try to wander around the code, opening random files. Run the
tutorial with a debugger to follow the flow and understand what's going on.

* [bottle.py](https://github.com/bottlepy/bottle/blob/master/bottle.py): bottle
  is a web framework. It's a great resource because it's in all in whole file!
  Recommended reading. You can even print it.
* [flask](https://github.com/mitsuhiko/flask): another web framework, one of
  the best. Reading its code is highly recommended as well.

I feel it's more important to understand the vision behind Python's design,
than to know specific Python idioms. The Zen of Python will let you understand
the fundamental reasoning behind each idiom.

```
>>> import this
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

Learning idiomatic Python:

* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/)
* [Idiomatic Python](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)

Packaging Python code
---------------------

* [Read the guide](https://python-packaging-user-guide.readthedocs.org/en/latest/)

Small exercises
---------------

* Create a virtual environment with virtualenv.
* Create a virtual environment with virtualenvwrapper tools.
* Fix a bug in one of the Python packages listed in [the Python guide](http://docs.python-guide.org/en/latest/#scenario-guide).

Ramp up with specific library
-----------------------------

Regardless of whether you use them, those tutorials introduce you to important
concept and good design patterns, so they're highly recommended:

* Do the [Flask tutorial](http://flask.pocoo.org/docs/tutorial/).
* Watch the [SQLAlchemy introduction
  video](https://www.youtube.com/watch?v=P141KRbxVKc). It lasts 3 hours but is
  extremely insightful, and introduces to some great object oriented patterns.

Other specific libraries that are very often used in professional
environments:


Keeping up to date
------------------

There are two main newsletter for Python, which mostly cover the same things:

* [Pycoder's Weekly](http://www.pycoders.com/)
* [Python Weekly](http://www.pythonweekly.com/)
