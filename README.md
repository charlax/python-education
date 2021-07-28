<!--TOC-->

- [Learning the language](#learning-the-language)
  - [Beginner](#beginner)
  - [Intermediate](#intermediate)
- [Writing idiomatic Python](#writing-idiomatic-python)
- [Exercises](#exercises)
  - [Code practice websites](#code-practice-websites)
  - [Small exercises](#small-exercises)
  - [Larger projects](#larger-projects)
  - [My exercises](#my-exercises)
- [Topics](#topics)
  - [Algorithms](#algorithms)
  - [Best Practices](#best-practices)
  - [Celery](#celery)
  - [Code Architecture](#code-architecture)
  - [Configuration](#configuration)
  - [Debugging](#debugging)
  - [Deployment](#deployment)
  - [Design patterns](#design-patterns)
  - [File organisation (monorepo, folders, etc.)](#file-organisation-monorepo-folders-etc)
  - [Functional code](#functional-code)
  - [Internals](#internals)
  - [Magic methods](#magic-methods)
  - [Open source Python apps](#open-source-python-apps)
  - [Packages (finding them)](#packages-finding-them)
  - [Packaging & pip](#packaging--pip)
  - [Performance optimization](#performance-optimization)
  - [Python and beyond](#python-and-beyond)
  - [Quirks and gotchas](#quirks-and-gotchas)
  - [SQLAlchemy](#sqlalchemy)
  - [Static analysis of code](#static-analysis-of-code)
  - [Tests](#tests)
  - [Types](#types)
  - [Unicode](#unicode)
- [Reference and other lists](#reference-and-other-lists)
- [Staying up to date](#staying-up-to-date)
- [Non-Python professional coding education](#non-python-professional-coding-education)

<!--TOC-->

The goal of this documentation is to help you become a productive Python developer.

It assumes that those skills will be used in a professional environment. It includes concrete exercises, because the best way to learn is by doing. It focuses on real-world, applied documentation that will help your programming on a day-to-day basis.

This doc assumes programming knowledge and experience.

If you're also interested in generic programming best practices, I've compiled a list of [professional programming](https://github.com/charlax/professional-programming) resources.

## Learning the language

### Beginner

First, [Why Beginners Should Learn Python](http://stackabuse.com/why-beginners-should-learn-python/)

Here are some free books:

- [Official Tutorial](https://docs.python.org/3/tutorial/index.html): Python's official doc is really good, highly recommended read.
- [Dive Into Python](https://diveintopython3.problemsolving.io/): much faster
  introduction to Python, a bit outdated but will get you ramped up really fast, especially if you've learned a number of programming language in the past.

[The Python Guide](http://docs.python-guide.org/en/latest/intro/learning/) has some other good resources.

If you're coming from another language, read this article about the [ten myths of enterprise Python](https://medium.com/paypal-engineering/10-myths-of-enterprise-python-8302b8f21f82).

If you want to review algorithms at the same time, you can use [Problem Solving with Algorithms and Data Structures using Python](http://interactivepython.org/runestone/static/pythonds/index.html) by Bradley N. Miller, David L. Ranum.

Other resources include (prefer the one listed above):

- [Automate the boring stuff with Python](https://automatetheboringstuff.com/)
- [Invent with Python](http://inventwithpython.com/chapters/)
- [Learn Python in one picture](https://github.com/coodict/python3-in-one-pic)
- [11 Beginner Tips for Learning Python Programming](https://realpython.com/python-beginner-tips/)
- [BeginnersGuide - Python Wiki](https://wiki.python.org/moin/BeginnersGuide)
- [Learning Python — The Hitchhiker's Guide to Python](https://docs.python-guide.org/intro/learning/)
- [Crash into Python](https://stephensugden.com/crash_into_python/): for experienced programmers
- [Full Stack Python](https://www.fullstackpython.com/)
- [Learn Computer Science](https://hyperskill.org/onboarding/tracks/2) with Python, from JetBrains

### Intermediate

I wrote some introductory material to advanced Python:

- [Introduction to advanced Python](advanced_python/advanced_python.md) (article). [Advanced Python presentation](http://www.slideshare.net/charlax/introduction-to-advanced-python) (Slideshare).

#### Articles, videos and presentations

- [py-must-watch](https://github.com/s16h/py-must-watch)

#### Books

- Muhammad Yasoob Ullah Khalid, [Intermediate Python](http://book.pythontips.com/en/latest/)
- Luciano Ramalho, [Fluent Python](http://www.amazon.com/gp/product/1491946008/)
- Dusty Phillips, [Python 3 Object-Oriented Programming](http://www.amazon.com/gp/product/1784398780/)
- Brett Slatkin, [Effective Python: 59 Specific Ways to Write Better Python](http://www.amazon.com/gp/product/0134034287/)

Lists of books:

- [Legally Free Python Books List](https://www.pythonkitchen.com/legally-free-python-books-list/)

## Writing idiomatic Python

First things first, let's get **code style** out of the way. Make sure you've read and memorized [PEP8](https://www.python.org/dev/peps/pep-0008/) (code style, [more readable version here](http://pep8.org/)) and [PEP257](https://www.python.org/dev/peps/pep-0257/) (docstring style). Those two code styles are applied by almost all major Python applications and libraries. Use flake8, autopep8 and black to ensure they are applied.

What is called "idiomatic Python" might feel magical at first, especially if you don't know Python. I'd recommend getting your hands dirty with some real world Python code. Try to wander around the code, opening random files. Run the tutorial with a debugger to follow the flow and understand what's going on.

- [bottle.py](https://github.com/bottlepy/bottle/blob/master/bottle.py): bottle is a web framework. It's a great resource because it's in all in whole file!
  Recommended reading. You can even print it.
- [flask](https://github.com/mitsuhiko/flask): another web framework, one of the best. Reading its code is highly recommended as well.

You can find other ideas on [this hacker news thread](https://news.ycombinator.com/item?id=9896369).

I feel it's more important to understand the vision behind Python's design, than to know specific Python idioms. The Zen of Python will help you understand the fundamental reasoning behind each idiom.

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

- [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/)
- [What the heck does “pythonic” mean?](http://halitalptekin.tumblr.com/post/30028271874/pythonic-syntax)
- [Elements of Python style](https://github.com/amontalenti/elements-of-python-style)
- [Meditations on the Zen of Python](https://orbifold.xyz/zen-of-python.html)

List of books:

- [Awesome Python Books](https://github.com/Junnplus/awesome-python-books)

## Exercises

The best way to learn is to do.

### Code practice websites

- [Exercism](https://exercism.io/)
- [Codingame](https://www.codingame.com/start)
- Solve some of the [Project Euler problems](https://projecteuler.net/)
- [LeetCode](https://leetcode.com/)
- [Codewars](https://www.codewars.com/)
- [HackerRank](https://www.hackerrank.com/)

### Small exercises

- Create a virtual environment with `virtualenv`.
- Fix a bug in one of the Python packages listed in [the Python guide](http://docs.python-guide.org/en/latest/#scenario-guide).
- Take inspiration from this [list of Raspberry Pi projects on reddit](https://www.reddit.com/r/Python/comments/4e59wb/what_have_you_done_with_python_and_raspberry_pi/)

### Larger projects

- Build a lock library for Redis.
- Build a cache library for Redis.
- Build an API for storing todos
- Build an API for next bus departure time.
- Build an ORM for a SQL database.
- Build a command line parser.
- Build a template engine.
- Build a static site generator.
- Build an HTTP library.
- Clone one of those [games](http://inventwithpython.com/blog/2012/02/20/i-need-practice-programming-49-ideas-for-game-clones-to-code/)
- Write a game using [pyarcade](https://arcade.academy/)

Reddit's [dailyprogrammer subreddit](https://www.reddit.com/r/dailyprogrammer)
has some good exercises as well.

Another great way to learn Python is by contributing to one of the numerous
open source libraries. Coding is not something that is to be learn in
isolation, and you'll learn great valuable insights from the code review you'll
get from those communities. You can look for tickets (e.g. Github issues) for
Python libraries you're using, or find some in the list below, or pick one of
the libraries listed in [Awesome
Python](https://github.com/vinta/awesome-python). Make sure you pick a library
where the tickets are not too involved, and where the community is still alive
(i.e. there's recent merged pull requests).

### My exercises

- Check [intro-to-python/exercises](./intro-to-python/exercises/).
- Check [advanced-python/exercises](./advanced-python/exercises/).

## Topics

### Algorithms

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python): all algorithms implemented in Python

### Best Practices

- [The Best of the Best Practices (BOBP) Guide for Python](https://gist.github.com/sloria/7001839)
- [When Python Practices Go Wrong](https://rhodesmill.org/brandon/slides/2019-11-codedive/): a pretty opinionated presentation that can be too concise at times, but nonetheless very interesting for somebody looking to constrain their creativity with Python constructs.
- [Stop naming your python modules "utils"](https://breadcrumbscollector.tech/stop-naming-your-python-modules-utils/)
- [zedr/clean-code-python](https://github.com/zedr/clean-code-python): Clean Code concepts adapted for Python

### Celery

Celery is a distributed async tasks runner.

- [Celery best practices](https://blog.balthazar-rouberol.com/celery-best-practices), Balthazar

### Code Architecture

- [The clean architecture](http://rhodesmill.org/brandon/slides/2014-07-pyohio/clean-architecture/)
- [python-clean-architecture](https://github.com/pcah/python-clean-architecture)

### Configuration

- [Best Practices for Working with Configuration in Python Applications](https://tech.preferred.jp/en/blog/working-with-configuration-in-python/)
	- Use identifiers rather than string keys to access configuration values.
	- Use static typing
	- Validate early.
	- Declare close to where it is used.
- [Doing Python Configuration Right](https://whalesalad.com/blog/doing-python-configuration-right)
	- Static things that don't change often, or things that dramatically influence the behavior of the system should live in the code.
	- Dynamic things that change frequently, or things that should be kept secret (API keys/credentials) should live outside the code.

### Debugging

- General introduction: [Python debugging
  tools](http://blog.ionelmc.ro/2013/06/05/python-debugging-tools/)
- A better debugger: [pudb](http://heather.cs.ucdavis.edu/~matloff/pudb.html)
- [Debugging Python Like a Boss](https://zapier.com/engineering/debugging-python-boss/)

### Deployment

- [Production-ready Docker packaging for Python developers](https://pythonspeed.com/docker/)

### Design patterns

- [Design patterns explained](http://www.pysnap.com/design-patterns-explained/)
- [Python 3 Patterns, Recipes and Idioms](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/index.html)
- [Decorators in 12 steps](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)
- [Design pattern templates in Python](https://github.com/tylerlaberge/PyPattyrn) (Github)
- [Python Design Patterns Guide](https://www.toptal.com/python/python-design-patterns): a nice intro to design patterns in Python
- [faif/python-patterns](https://github.com/faif/python-patterns): a collection of design patterns and idioms in Python.

I maintain a [list of antipatterns](./python-antipatterns.md) on this repo.

### File organisation (monorepo, folders, etc.)

- [Our Python Monorepo](https://medium.com/opendoor-labs/our-python-monorepo-d34028f2b6fa), OpenDoor

### Functional code

- [Python Partials are Fun!](http://www.pydanny.com/python-partials-are-fun.html)
- [sfermigier/awesome-functional-python](https://github.com/sfermigier/awesome-functional-python)

### Internals

- [Why Python is Slow: Looking Under the Hood](http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/)
- [The internals of Python string interning](http://guilload.com/python-string-interning/)
- [Python Data structures](http://rhodesmill.org/brandon/slides/2014-04-pycon/data-structures/)

### Magic methods

- [A Guide to Python's Magic Methods](http://www.rafekettler.com/magicmethods.html)

### Open source Python apps

It's often a good idea to read the Python source code of well-written applications:

- [mahmoud/awesome-python-applications](https://github.com/mahmoud/awesome-python-applications): free software that works great, and also happens to be open-source Python

### Packages (finding them)

- [Awesome Python](https://github.com/vinta/awesome-python) provides a great list of third party libraries.

### Packaging & pip

- [Packaging guide](https://packaging.python.org/)
- [setup.py vs. requirements.txt](https://caremad.io/2013/07/setup-vs-requirement/): this is an important gotcha for any library developer.
- [Open Sourcing a Python Project the Right Way](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)
- [Pipfile](https://github.com/pypa/pipfile): a `Pipfile`, and its related `Pipfile.lock`, are a new (and much better!) replacement for pip's requirements.txt files.
- [Overview of python dependency management tools](https://modelpredict.com/python-dependency-management-tools)
- [Virtual Environments Demystified](https://meribold.org/python/2018/02/13/virtual-environments-9487/)

### Performance optimization

- [Profiling Python using cProfile: a concrete
  case](https://julien.danjou.info/blog/2015/guide-to-python-profiling-cprofile-concrete-case-carbonara)
- [cProfile module documentation](https://docs.python.org/3/library/profile.html)
- [Example cProfile session](https://ymichael.com/2014/03/08/profiling-python-with-cprofile.html)
- [A guide to analyzing Python performance](http://www.huyng.com/posts/python-performance-analysis/)
- [RunSnakeRun](http://www.vrplumber.com/programming/runsnakerun/) is a small
  GUI utility that allows you to view (Python) cProfile or Profile profiler
  dumps in a sortable GUI view.
- [SnakeViz](http://jiffyclub.github.io/snakeviz/) is a browser based graphical
  viewer for the output of Python’s cProfile module.
- [Using qcachegrind to visualize profiling data](http://blog.d3in.org/post/51022123117/using-qcachegrind-to-visualize-python-profiling)

### Python and beyond

- [27 languages to improve your Python](http://www.curiousefficiency.org/posts/2015/10/languages-to-improve-your-python.html)
- [List of languages that compile to Python](https://github.com/vindarel/languages-that-compile-to-python)

### Quirks and gotchas

- [Hidden features of Python](http://stackoverflow.com/questions/101268/hidden-features-of-python)
- [30 Python Language Features and Tricks You May Not Know About](http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html)
- [A collection of Python "wat" moments](http://www.b-list.org/weblog/2015/oct/13/wats-doc/)
- [satwikkansal/wtfpython: a collection of interesting, subtle, and tricky Python snippets](https://github.com/satwikkansal/wtfpython)
- Ned Batchelder, [Facts and myths about Python names and values](https://nedbatchelder.com/text/names.html)

### SQLAlchemy

SQLAlchemy is the de facto standard ORM for Python. It has a unique approach:
contrary to most ORM, it tries very hard not to hide the SQL implementation
details from you. This is great because it forces you to really understand the
underlying DB.

Here is some slightly outdated content that is super useful to fully leverage
the library:

- Watch the [SQLAlchemy introduction
  video](https://www.youtube.com/watch?v=P141KRbxVKc). It lasts 3 hours but is
  extremely insightful, and introduces to some great object oriented patterns.
- [Handcoded application with SQLAlchemy](http://pyvideo.org/video/665/hand-coded-applications-with-sqlalchemy)
- [Alembic](http://alembic.readthedocs.org/en/latest/) is a lightweight
  database migration tool for usage with the SQLAlchemy Database Toolkit for
  Python.

### Static analysis of code

- [Essential python tools - Quality](http://aboumrad.info/essential-python-tools-quality.html)

### Tests

Half of coding time is usually spent writing tests. Yet how to write tests
efficiently is very rarely taught at school - even though it came make a huge
difference in engineering productivity and quality.

First, make sure you're familiar with the different kind of testing strategies
laid out in [Testing Strategies in a Microservices
Architecture](http://martinfowler.com/articles/microservice-testing/) (Martin
Fowler).

Then, read some of those articles:

- [Mock yourself, not your
  tests](http://hernantz.github.io/mock-yourself-not-your-tests.html): great
  articles about the danger of mocking, and better unit testing strategies.
- [Building Good Tests](https://salmonmode.github.io//2019/03/29/building-good-tests.html), Chris NeJame
  - 1 assert per test function/method and nothing else
  - Use standard assert statements, instead of the unittest.TestCase assert methods
  - Test behavior, not implementation
  - Only verify state-changing method calls
  - Test the result, not the process
  - Every test should be able to be run in parallel with any other test
  - A test should never be flaky
  - Try to avoid mocking things whenever possible.
  - Test coverage is not a metric for what was tested; it’s a metric for what code your tests managed to hit
  - The code should be easy to test \* Make your test code succinct and idiomatic
- [pytest](http://pytest.org/latest/) is a test framework. It's very elegant
  and allows to quickly write very maintainable tests.

### Types

- [The state of type hints in Python](https://www.bernat.tech/the-state-of-type-hints-in-python/): a good summary of typing in Python and its gotchas.

### Unicode

- [Solving Unicode Problems in Python 2.7](http://www.azavea.com/blogs/labs/2014/03/solving-unicode-problems-in-python-2-7/)
- [Unicode Howto in Python 3](https://docs.python.org/3/howto/unicode.html) (official Python documentation).
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](http://www.joelonsoftware.com/articles/Unicode.html)

## Reference and other lists

- [Best Python Resources](http://www.fullstackpython.com/best-python-resources.html)
- [Awesome Python](https://github.com/vinta/awesome-python)
- [PyCon 2015](https://www.youtube.com/channel/UCgxzjK6GuOHVKR_08TT4hJQ)
- Invent With Python, [Further Reading: Intermediate Python Resources](http://inventwithpython.com/blog/2015/09/01/further-reading-intermediate-python-resources/)

## Staying up to date

There are two main newsletters for Python, which mostly cover the same things:

- [Pycoder's Weekly](http://www.pycoders.com/)
- [Python Weekly](http://www.pythonweekly.com/)

You can also checkout the [Python subreddit](https://www.reddit.com/r/Python/).

## Non-Python professional coding education

Read this up on my [professional programming doc](https://github.com/charlax/professional-programming).

If you want to get in touch, checkout [my website](http://www.d3in.org/).
