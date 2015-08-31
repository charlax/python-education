Ramping up with professional Python
===================================

The goal of this documentation is to introduce you to the world of professional
Python. It will be providing concrete exercises, because the best way to learn
is to do.

Learning the language
=====================

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

If you're coming from another language, read this article about the [ten myths of enterprise Python](https://www.paypal-engineering.com/2014/12/10/10-myths-of-enterprise-python/).

Intermediate
------------

* Muhammad Yasoob Ullah Khalid, [Intermediate Python](http://book.pythontips.com/en/latest/)
* Luciano Ramalho, [Fluent
  Python](http://www.amazon.com/gp/product/1491946008/)

Learning to write idiomatic Python
----------------------------------

First things first, let's get code styling out of the way. Make sure you've
read an memorized [PEP8](https://www.python.org/dev/peps/pep-0008/) (code
style) and [PEP257](https://www.python.org/dev/peps/pep-0257/) (docstring
style). Those two code styles are applied by almost all major Python
applications and libraries. Use flake8.

What is called "idiomatic Python" might feel magical at first, especially if
you don't know Python. I'd recommend getting your hands dirty with some real
world Python code. Try to wander around the code, opening random files. Run the
tutorial with a debugger to follow the flow and understand what's going on.

* [bottle.py](https://github.com/bottlepy/bottle/blob/master/bottle.py): bottle
  is a web framework. It's a great resource because it's in all in whole file!
  Recommended reading. You can even print it.
* [flask](https://github.com/mitsuhiko/flask): another web framework, one of
  the best. Reading its code is highly recommended as well.

You can find other ideas on [this hacker news
thread](https://news.ycombinator.com/item?id=9896369).

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
* [What the heck does “pythonic” mean?](http://halitalptekin.tumblr.com/post/30028271874/pythonic-syntax)

Patterns and anti-patterns
--------------------------

Here's a list of good books:

* [Design Patterns: Elements of Reusable Object-Oriented Software](http://www.amazon.com/dp/0201633612/): dubbed "the gang of four", this is almost a required reading for any developer. A lot of those are a bit overkill for Python (because everything is an object, and dynamic typing), but the main idea (composition is better than inheritance) definitely is a good philosophy.
* [Patterns of Enterprise Application Architecture](http://www.amazon.com/dp/0321127420/?tag=stackoverfl08-20): learn about how database are used in real world applications. Mike Bayer's SQLAlchemy has been heavily influenced by this book.
* SourceMaking's [Design Patterns](https://sourcemaking.com/design_patterns) seems to be a good web resource too.

I maintain a [list of antipatterns](https://github.com/charlax/antipatterns) on another repo. This is a highly recommended read.

Exercises
---------

The best way to learn is to do.

Small exercises:

* Create a virtual environment with virtualenv.
* Create a virtual environment with virtualenvwrapper tools.
* Fix a bug in one of the Python packages listed in [the Python guide](http://docs.python-guide.org/en/latest/#scenario-guide).
* Create a server exposing a Thrift API.

Larger projects:

* Build a lock library for redis.
* Build a cache library for redis.
* Build an API for next bus departure time.
* Build an ORM for a SQL database.
* Build a command line parser.
* Build a template engine.
* Build a static site generator.
* Build an HTTP library.

Ramping up with specific libraries
----------------------------------

Regardless of whether you use them, those tutorials introduce you to important
concept and good design patterns, so they're highly recommended:

* Do the [Flask tutorial](http://flask.pocoo.org/docs/tutorial/).
* Watch the [SQLAlchemy introduction
  video](https://www.youtube.com/watch?v=P141KRbxVKc). It lasts 3 hours but is
  extremely insightful, and introduces to some great object oriented patterns.

Other great SQLAlchemy resources include:

* [Handcoded application with SQLAlchemy](http://pyvideo.org/video/665/hand-coded-applications-with-sqlalchemy)

Other specific libraries that are very often used in professional
environments:

* [Celery](http://www.celeryproject.org/) is an asynchronous task queue/job
  queue based on distributed message passing. It is focused on real-time
  operation, but supports scheduling as well.
* [Tornado](http://www.tornadoweb.org/en/stable/) is a Python web framework and
  asynchronous networking library.
* [Alembic](http://alembic.readthedocs.org/en/latest/) is a lightweight
  database migration tool for usage with the SQLAlchemy Database Toolkit for
  Python.
* [Jinja](http://jinja.pocoo.org/) is a full featured template engine for
  Python. It has full unicode support, an optional integrated sandboxed
  execution environment, widely used and BSD licensed.
* [Doubles](http://doubles.readthedocs.org/en/latest/) is a Python package that
  provides test doubles for use in automated tests.
* [Mock](http://www.voidspace.org.uk/python/mock/) is a library for testing in
  Python. It allows you to replace parts of your system under test with mock
  objects and make assertions about how they have been used.
* [pytest](http://pytest.org/latest/) is a test framework.

Topics
------

### Magic methods

* [A Guide to Python's Magic Methods](http://www.rafekettler.com/magicmethods.html)

### Quirks and gotchas

* [Python quirks](http://www.lshift.net/blog/2009/10/29/python-quirks/)
* [Hidden features of Python](http://stackoverflow.com/questions/101268/hidden-features-of-python)
* [30 Python Language Features and Tricks You May Not Know About](http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html)

### Internals

* [Why Python is Slow: Looking Under the Hood](http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/)
* [The internals of Python string interning](http://guilload.com/python-string-interning/)

### Debugging

* General introduction: [Python debugging
  tools](http://blog.ionelmc.ro/2013/06/05/python-debugging-tools/)
* A better debugger: [pudb](http://heather.cs.ucdavis.edu/~matloff/pudb.html)

### Performance optimization

* [cProfile module documentation](https://docs.python.org/2/library/profile.html)
* [Example cProfile session](https://ymichael.com/2014/03/08/profiling-python-with-cprofile.html)
* [A guide to analyzing Python performance](http://www.huyng.com/posts/python-performance-analysis/)
* [RunSnakeRun](http://www.vrplumber.com/programming/runsnakerun/) is a small
  GUI utility that allows you to view (Python) cProfile or Profile profiler
  dumps in a sortable GUI view.
* [SnakeViz](http://jiffyclub.github.io/snakeviz/) is a browser based graphical
  viewer for the output of Python’s cProfile module.
* [Using qcachegrind to visualize profiling data](http://blog.d3in.org/post/51022123117/using-qcachegrind-to-visualize-python-profiling)

### Packaging

* [Read the guide](https://python-packaging-user-guide.readthedocs.org/en/latest/)
* [setup.py vs. requirements.txt](https://caremad.io/2013/07/setup-vs-requirement/): this is an important gotcha for any library developer.
* [Open Sourcing a Python Project the Right Way](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)

Keeping up to date
------------------

There are two main newsletters for Python, which mostly cover the same things:

* [Pycoder's Weekly](http://www.pycoders.com/)
* [Python Weekly](http://www.pythonweekly.com/)

Reference
---------

* [Best Python Resources](http://www.fullstackpython.com/best-python-resources.html)
* [Awesome Python](https://github.com/vinta/awesome-python)
* [PyCon 2015](https://www.youtube.com/channel/UCgxzjK6GuOHVKR_08TT4hJQ)
