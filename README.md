<!--TOC-->

- [About this list](#about-this-list)
- [Learning the language](#learning-the-language)
  - [Why learn Python?](#why-learn-python)
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
  - [Beyond Python (other programming languages)](#beyond-python-other-programming-languages)
  - [Boilerplate](#boilerplate)
  - [Celery](#celery)
  - [CLI](#cli)
  - [Code Architecture](#code-architecture)
  - [Concurrency](#concurrency)
  - [Configuration](#configuration)
  - [Debugging](#debugging)
  - [Deployment](#deployment)
  - [Design patterns](#design-patterns)
  - [Documentation](#documentation)
  - [Example, inspiration and template packages](#example-inspiration-and-template-packages)
  - [Exception](#exception)
  - [File organisation (monorepo, folders, etc.)](#file-organisation-monorepo-folders-etc)
  - [Functional programming](#functional-programming)
  - [Internals](#internals)
  - [Magic methods](#magic-methods)
  - [Open source Python apps](#open-source-python-apps)
  - [Packages (finding and using them)](#packages-finding-and-using-them)
  - [Packages (opinionated list)](#packages-opinionated-list)
  - [Packaging (creating your own package)](#packaging-creating-your-own-package)
  - [Parsing](#parsing)
  - [Performance](#performance)
  - [Preparing for interviews](#preparing-for-interviews)
  - [Quirks and gotchas](#quirks-and-gotchas)
  - [Regular expressions (regex)](#regular-expressions-regex)
  - [Security](#security)
  - [SQLAlchemy](#sqlalchemy)
  - [Standard library modules](#standard-library-modules)
  - [Static analysis of code](#static-analysis-of-code)
  - [Tests](#tests)
  - [Tools built with Python](#tools-built-with-python)
  - [Types](#types)
  - [Unicode](#unicode)
- [Reference and other lists](#reference-and-other-lists)
- [Staying up to date](#staying-up-to-date)
- [Non-Python professional coding education](#non-python-professional-coding-education)
- [My other lists](#my-other-lists)

<!--TOC-->

## About this list

Items:

- 🧰 : list of resources
- 📖 : book
- 🎞 : video/movie extract/movie
- 🎤 : slides/presentation
- 🎧 : podcast
- 🔧 : tool
- ⭐️ : must-read

The goal of this documentation is to help you become a productive Python developer.

It assumes that those skills will be used in a professional environment. It includes concrete exercises, because the best way to learn is by doing. It focuses on real-world, applied documentation that will help your programming on a day-to-day basis.

This doc assumes programming knowledge and experience.

If you're also interested in generic programming best practices, I've compiled a list of [professional programming](https://github.com/charlax/professional-programming) resources.

## Learning the language

### Why learn Python?

- [Why Beginners Should Learn Python](http://stackabuse.com/why-beginners-should-learn-python/)
- [Why Python keeps growing, explained | The GitHub Blog](https://github.blog/2023-03-02-why-python-keeps-growing-explained/)

### Beginner

Here are some free books:

- [Official Tutorial](https://docs.python.org/3/tutorial/index.html): Python's official doc is really good, highly recommended read.
- [Dive Into Python](https://diveintopython3.problemsolving.io/): much faster
  introduction to Python, a bit outdated but will get you ramped up really fast, especially if you've learned a number of programming language in the past.

[The Python Guide](http://docs.python-guide.org/en/latest/intro/learning/) has some other good resources.

If you're coming from another language, read this article about the [ten myths of enterprise Python](https://medium.com/paypal-engineering/10-myths-of-enterprise-python-8302b8f21f82).

If you want to review algorithms at the same time, you can use [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/ns/books/published/pythonds/index.html) by Bradley N. Miller, David L. Ranum.

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
- [How to Use Python: Your First Steps](https://realpython.com/python-first-steps/) (RealPython)
- [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python)

### Intermediate

I wrote some introductory material to advanced Python:

- [Introduction to advanced Python](advanced-python/README.md) (article).
- [Advanced Python presentation](http://www.slideshare.net/charlax/introduction-to-advanced-python) (Slideshare).

Some other resources:

- [The power of Python descriptors](https://piccolo-orm.com/blog/the-power-of-python-descriptors/)
- [dabeaz-course/python-mastery](https://github.com/dabeaz-course/python-mastery)
- [DjangoEx/awesome-python-roadmaps: Awesome Python roadmaps](https://github.com/DjangoEx/awesome-python-roadmaps)

#### Articles, videos and presentations

- 🎞 [py-must-watch](https://github.com/s16h/py-must-watch)
- 🎞 [calmcode.io](https://calmcode.io/)

#### Books

- Muhammad Yasoob Ullah Khalid, [Intermediate Python](http://book.pythontips.com/en/latest/)
- Luciano Ramalho, [Fluent Python](https://www.amazon.com/gp/product/1492056359/)
- Dusty Phillips, [Python 3 Object-Oriented Programming](http://www.amazon.com/gp/product/1784398780/)
- Brett Slatkin, [Effective Python: 59 Specific Ways to Write Better Python](http://www.amazon.com/gp/product/0134034287/)

Lists of books:

- [Legally Free Python Books List](https://www.pythonkitchen.com/legally-free-python-books-list/)

#### Podcasts

- [Talk Python To Me podcast](https://talkpython.fm/) In-depth interviews and topics.
- [Python Bytes](https://pythonbytes.fm/) Weekly python news and discussion
- [Podcast.init](https://www.pythonpodcast.com/) Data engineering, data science and DevOps
- [Real Python Podcast](https://realpython.com/podcasts/rpp/) Python news and education

## Writing idiomatic Python

First things first, let's get **code style** out of the way. Make sure you've read and memorized [PEP8](https://www.python.org/dev/peps/pep-0008/) (code style, [more readable version here](http://pep8.org/)) and [PEP257](https://www.python.org/dev/peps/pep-0257/) (docstring style). Those two code styles are applied by almost all major Python applications and libraries. Use flake8, pydocstyle and black to ensure they are applied (check other linters and autofixers below).

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
- [3 Tips For Writing Pythonic Code](https://davidamos.dev/3-tips-for-writing-pythonic-code/)

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
- [spandanb/learndb-py](https://github.com/spandanb/learndb-py): learn database internals by implementing it from scratch.

Reddit's [dailyprogrammer subreddit](https://www.reddit.com/r/dailyprogrammer)
has some good exercises as well.

Another great way to learn Python is by contributing to one of the numerous open source libraries. Coding is not something that is to be learn in isolation, and you'll learn great valuable insights from the code review you'll get from those communities. You can look for tickets (e.g. Github issues) for Python libraries you're using, or find some in the list below, or pick one of the libraries listed in [Awesome Python](https://github.com/vinta/awesome-python).

Make sure you pick a library where the tickets are not too involved, and where the community is still alive (i.e. there's recent merged pull requests).

### My exercises

- Check [intro-to-python/exercises](./intro-to-python/exercises/).
- Check [advanced-python/exercises](./advanced-python/exercises/).

## Topics

### Algorithms

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python): all algorithms implemented in Python
- [Python Big O: the time complexities of different data structures in Python](https://www.pythonmorsels.com/time-complexities/)

### Best Practices

- [The Best of the Best Practices (BOBP) Guide for Python](https://gist.github.com/sloria/7001839)
- [When Python Practices Go Wrong](https://rhodesmill.org/brandon/slides/2019-11-codedive/): a pretty opinionated presentation that can be too concise at times, but nonetheless very interesting for somebody looking to constrain their creativity with Python constructs.
- [Stop naming your python modules "utils"](https://breadcrumbscollector.tech/stop-naming-your-python-modules-utils/)
- [zedr/clean-code-python](https://github.com/zedr/clean-code-python): Clean Code concepts adapted for Python
- [Django for Startup Founders: A better software architecture for SaaS startups and consumer apps](https://alexkrupp.typepad.com/sensemaking/2021/06/django-for-startup-founders-a-better-software-architecture-for-saas-startups-and-consumer-apps.html): I strongly disagree with some of the points, but there's definitely some inspiration to take.
  - Keep business logic in services
  - Make services the locus of reusability
  - Use functions, not classes
  - There are exactly 4 types of errors
  - Use serializers responsibly, or not at all
  - Write admin functionality as API endpoints
  - Keep logic out of the front end
- [Boring Python: code quality](https://www.b-list.org/weblog/2022/dec/19/boring-python-code-quality/)
- [Modern Good Practices for Python Development](https://www.stuartellis.name/articles/python-modern-practices/), 2024

### Beyond Python (other programming languages)

- [27 languages to improve your Python](http://www.curiousefficiency.org/posts/2015/10/languages-to-improve-your-python.html)
- [List of languages that compile to Python](https://github.com/vindarel/languages-that-compile-to-python)
- [Rust for Python Programmers](https://lucumr.pocoo.org/2015/5/27/rust-for-pythonistas/), Armin Ronacher
- [What learning APL taught me about Python](https://mathspp.com/blog/what-learning-apl-taught-me-about-python)
- [The Hy programming language](https://hylang.org/): a Lisp dialect in Python

### Boilerplate

- [An opinionated Python boilerplate](https://duarteocarmo.com/blog/opinionated-python-boilerplate)
  - `pip-tools`
  - `Makefile`
  - `ruff`
- [A Python project checklist](https://www.dein.fr/posts/2021-01-28-python-project-checklist)

### Celery

Celery is a distributed async tasks runner.

- [Celery best practices](https://blog.balthazar-rouberol.com/celery-best-practices), Balthazar

### CLI

Building command line interfaces.

- [Building an authenticated Python CLI](https://www.notia.ai/articles/building-an-authenticated-python-cli)

### Code Architecture

- [The clean architecture](http://rhodesmill.org/brandon/slides/2014-07-pyohio/clean-architecture/)
- [python-clean-architecture](https://github.com/pcah/python-clean-architecture)
- 📖 [Cosmic Python](https://www.cosmicpython.com/): simple patterns for building complex Python application (free)
  - Domain modeling and DDD
  - Repository, Service Layer, and Unit of Work patterns
  - Event-driven architecture
  - Command-query responsibility segregation
- [Arc Note: Datasette](https://architecturenotes.co/datasette-simon-willison/)

### Concurrency

- [Concurrency with Python](https://bytes.yingw787.com/posts/2019/01/11/concurrency_with_python_why/): a pretty complete series of articles that goes into threads, functional programming, actor models, CSP, coroutines and data intensive architectures.

### Configuration

- [Best Practices for Working with Configuration in Python Applications](https://tech.preferred.jp/en/blog/working-with-configuration-in-python/)
	- Use identifiers rather than string keys to access configuration values.
	- Use static typing
	- Validate early.
	- Declare close to where it is used.
- [Doing Python Configuration Right](https://whalesalad.com/blog/doing-python-configuration-right)
	- Static things that don't change often, or things that dramatically influence the behavior of the system should live in the code.
	- Dynamic things that change frequently, or things that should be kept secret (API keys/credentials) should live outside the code.
- [Use TOML for `.env` files?](https://snarky.ca/use-toml-for-env-files/)

### Debugging

- General introduction: [Python debugging
  tools](http://blog.ionelmc.ro/2013/06/05/python-debugging-tools/)
- A better debugger: [pudb](http://heather.cs.ucdavis.edu/~matloff/pudb.html)
- [Debugging Python Like a Boss](https://zapier.com/engineering/debugging-python-boss/)
- [Syntax Error #11: Debugging Python](https://www.syntaxerror.tech/syntax-error-11-debugging-python/)

### Deployment

See also the more generic Docker section in [charlax/professional-programming](https://github.com/charlax/professional-programming#docker).

- [Production-ready Docker packaging for Python developers](https://pythonspeed.com/docker/)

### Design patterns

- [Python 3 Patterns, Recipes and Idioms](http://python-3-patterns-idioms-test.readthedocs.org/en/latest/index.html)
- [Decorators in 12 steps](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)
- [Design pattern templates in Python](https://github.com/tylerlaberge/PyPattyrn) (Github)
- [Python Design Patterns Guide](https://www.toptal.com/python/python-design-patterns): a nice intro to design patterns in Python
- [faif/python-patterns](https://github.com/faif/python-patterns): a collection of design patterns and idioms in Python.
- [Python Design Patterns](https://python-patterns.guide/)
  - [The Composition Over Inheritance Principle](https://python-patterns.guide/gang-of-four/composition-over-inheritance/)
- [Design Patterns in Machine Learning Code and Systems](https://eugeneyan.com/writing/design-patterns/)

I maintain a [list of antipatterns](./python-antipatterns.md) on this repo.

### Documentation

- [pandas](https://github.com/pandas-dev/pandas/blob/main/doc) is a great example to follow (using Sphinx, separating into quickstart, user guide, API reference).
- [Example NumPy Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html)
- [Why you should still read the docs](https://death.andgravity.com/output)

### Example, inspiration and template packages

- [charlax/cookiecutter-python-api: a cookiecutter template for an HTTP API](https://github.com/charlax/cookiecutter-python-api) with lots of best practices: mypy, flake8, isort, black, Makefile, fastapi, DDD pattern, file organization, etc.

By topics:

- Authorization: [holinnn/deny](https://github.com/holinnn/deny)

### Exception

- [The Most Diabolical Python Antipattern](https://realpython.com/the-most-diabolical-python-antipattern/)
- [The Ultimate Guide to Error Handling in Python](https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-error-handling-in-python)

### File organisation (monorepo, folders, etc.)

- [OpenDoor's Python Monorepo](https://medium.com/opendoor-labs/our-python-monorepo-d34028f2b6fa)
- [Atlas: Our journey from a Python monolith to a managed platform](https://dropbox.tech/infrastructure/atlas--our-journey-from-a-python-monolith-to-a-managed-platform) (Dropbox)
- [From Chaos to Cohesion: Architecting Your Own Monorepo](https://monadical.com/posts/from-chaos-to-cohesion.html)

### Functional programming

Consider checking out the same section on my [charlax/professional-programming](https://github.com/charlax/professional-programming#functional-programming-fp) repo.

- [Python Partials are Fun!](http://www.pydanny.com/python-partials-are-fun.html)
- [sfermigier/awesome-functional-python](https://github.com/sfermigier/awesome-functional-python)
- [Functools - The Power of Higher-Order Functions in Python](https://martinheinz.dev/blog/52)
- [Functors, Applicatives, And Monads In Pictures](https://github.com/dbrattli/OSlash/wiki/Functors,-Applicatives,-And-Monads-In-Pictures)
- [Monads in 15 minutes](https://nikgrozev.com/2013/12/10/monads-in-15-minutes/)
- [more-itertools/more-itertools](https://github.com/more-itertools/more-itertools): more routines for operating on iterables, beyond itertools
- [jmesyou/functional-programming-jargon.py](https://github.com/jmesyou/functional-programming-jargon.py): jargon from the functional programming world in simple terms

### Internals

- [Why Python is Slow: Looking Under the Hood](http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/)
- [The internals of Python string interning](http://guilload.com/python-string-interning/)
- [Python Data structures](http://rhodesmill.org/brandon/slides/2014-04-pycon/data-structures/)
- [Python’s Innards: Introduction](https://tech.blog.aknin.name/2010/04/02/pythons-innards-introduction/)
- [15. Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)
- [Behind "Hello World" on Linux](https://jvns.ca/blog/2023/08/03/behind--hello-world/), Julia Evans

Python behind the scenes series:

- [Python behind the scenes #11: how the Python import system works](https://tenthousandmeters.com/blog/python-behind-the-scenes-11-how-the-python-import-system-works/)
- [Python behind the scenes #10: how Python dictionaries work](https://tenthousandmeters.com/blog/python-behind-the-scenes-10-how-python-dictionaries-work/)
- [Python behind the scenes #13: the GIL and its effects on Python multithreading](https://tenthousandmeters.com/blog/python-behind-the-scenes-13-the-gil-and-its-effects-on-python-multithreading/)

### Magic methods

- [A Guide to Python's Magic Methods](http://www.rafekettler.com/magicmethods.html)

### Open source Python apps

It's often a good idea to read the Python source code of well-written applications:

- [mahmoud/awesome-python-applications](https://github.com/mahmoud/awesome-python-applications): free software that works great, and also happens to be open-source Python

### Packages (finding and using them)

How to use:

- [setup.py vs. requirements.txt](https://caremad.io/2013/07/setup-vs-requirement/): this is an important gotcha for any library developer.
- [Overview of python dependency management tools](https://modelpredict.com/python-dependency-management-tools)
- [Virtual Environments Demystified](https://meribold.org/python/2018/02/13/virtual-environments-9487/)
- [Commit your `poetry.lock` file to version control](https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control)
- [How virtual environments work](https://snarky.ca/how-virtual-environments-work/)

Lists:

- [Awesome Python](https://github.com/vinta/awesome-python) provides a great list of third party libraries.
- [ml-tooling/best-of-web-python](https://github.com/ml-tooling/best-of-web-python): awesome Python libraries for web development

### Packages (opinionated list)

Here's a short list of great packages:

- 🔧 [willmcgugan/rich](https://github.com/willmcgugan/rich): rich text and beautiful formatting in the terminal
- 🔧 [tqdm](https://tqdm.github.io/): wrap any iterable and show a smart progress meter
- 🔧 [tomerfiliba/plumbum](https://github.com/tomerfiliba/plumbum): shell combinators

Some other cool packages:

- [Acreom/quickadd: parse natural language time and date expressions](https://github.com/Acreom/quickadd)

### Packaging (creating your own package)

- [Packaging guide](https://packaging.python.org/)
- [Open Sourcing a Python Project the Right Way](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)
- [Tips for your Makefile with Python](https://blog.mathieu-leplatre.info/tips-for-your-makefile-with-python.html)
  - Environment variables with default
  - Full Example with Poetry
- 🔧 [commitizen-tools/commitizen](https://github.com/commitizen-tools/commitizen): create committing rules for projects, auto bump versions and auto changelog generation
- 🔧 [nedbat/scriv](https://github.com/nedbat/scriv): changelog management tool
- [Makefile tricks for Python projects](https://ricardoanderegg.com/posts/makefile-python-project-tricks/)

### Parsing

- [Learn Python ASTs, by building your own linter](https://sadh.life/post/ast/)

### Performance

- ⭐️ [Process large datasets without running out of memory](https://pythonspeed.com/memory/)
  - [Measuring memory usage in Python: it’s tricky!](https://pythonspeed.com/articles/measuring-memory-python/)
- [A guide to analyzing Python performance](http://www.huyng.com/posts/python-performance-analysis/)
- [cProfile module documentation](https://docs.python.org/3/library/profile.html)
- [Using qcachegrind to visualize profiling data](https://www.dein.fr/posts/2013-05-22-using-qcachegrind-to-visualize-python-profiling)
- [How vectorization speeds up your Python code](https://pythonspeed.com/articles/vectorization-python/)
- [You Should Compile Your Python And Here’s Why](https://glyph.twistedmatrix.com/2022/04/you-should-compile-your-python-and-heres-why.html)
- [When Python can’t thread: a deep-dive into the GIL’s impact](https://pythonspeed.com/articles/python-gil/), PythonSpeed
  - When does a Python thread need to hold the GIL?
  - The parallelism implications of the GIL
  - The good scenario: Long-running C APIs that release the GIL
  - Bad scenario #1: “pure” Python code
  - Bad scenario #2: Long-running C/Rust APIs, but author forgot to release GIL
  - Bad scenario #3: Low-level code with pervasive Python C API usage
- [CI for performance: Reliable benchmarking in noisy environments](https://pythonspeed.com/articles/consistent-benchmarking-in-ci/), PythonSpeed
  - Problem #1: Inconsistent results on a single machine
  - Problem #2: Inconsistent results across machines
  - Use Cachegrind

Stories:

- [Profiling Python using cProfile: a concrete case](https://julien.danjou.info/blog/2015/guide-to-python-profiling-cprofile-concrete-case-carbonara)
- [Example cProfile session](https://ymichael.com/2014/03/08/profiling-python-with-cprofile.html)
- [How we optimized Python API server code 100x](https://towardsdatascience.com/how-we-optimized-python-api-server-code-100x-9da94aa883c5)
- [An optimization story](https://tinkering.xyz/fmo-optimization-story/)

Tools:

- 🔧 [SnakeViz](http://jiffyclub.github.io/snakeviz/) is a browser based graphical viewer for the output of Python’s cProfile module.
- 🔧 [RunSnakeRun](http://www.vrplumber.com/programming/runsnakerun/) is a small GUI utility that allows you to view (Python) cProfile or Profile profiler dumps in a sortable GUI view.
- 🔧 [plasma-umass/scalene](https://github.com/plasma-umass/scalene): a high-performance, high-precision CPU, GPU, and memory profiler
- 🔧 [pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/stable/)
- 🔧 [benfred/py-spy](https://github.com/benfred/py-spy): sampling CPU profiler written in Rust for low overhead
- 🔧 [pythonspeed/filprofiler](https://github.com/pythonspeed/filprofiler): memory profiler for data processing and scientific computing applications

### Preparing for interviews

- [donnemartin/interactive-coding-challenges](https://github.com/donnemartin/interactive-coding-challenges): 120+ interactive Python coding interview challenges (algorithms and data structures). Includes Anki flashcards.

### Quirks and gotchas

- [Hidden features of Python](http://stackoverflow.com/questions/101268/hidden-features-of-python)
- [30 Python Language Features and Tricks You May Not Know About](http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html)
- [A collection of Python "wat" moments](http://www.b-list.org/weblog/2015/oct/13/wats-doc/)
- [satwikkansal/wtfpython: a collection of interesting, subtle, and tricky Python snippets](https://github.com/satwikkansal/wtfpython)
- Ned Batchelder, [Facts and myths about Python names and values](https://nedbatchelder.com/text/names.html)
- [Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html), Python Docs

### Regular expressions (regex)

- [Interactive regex exercises](https://github.com/learnbyexample/py_regular_expressions/tree/master/interactive_exercises)
- [The unreasonable effectiveness of f-strings and re.VERBOSE](https://death.andgravity.com/f-re)

### Security

- [Never Run ‘python’ In Your Downloads Folder](https://glyph.twistedmatrix.com/2020/08/never-run-python-in-your-downloads-folder.html)
- [ossillate-inc/packj: The vetting tool 🚀 behind our large-scale security analysis platform to detect malicious/risky open-source packages](https://github.com/ossillate-inc/packj)

### SQLAlchemy

SQLAlchemy is the de facto standard ORM for Python. It has a unique approach: contrary to most ORM, it tries very hard not to hide the SQL implementation details from you. This is great because it forces you to really understand the underlying DB.

Here is some slightly outdated content that is super useful to fully leverage the library:

- Watch the [SQLAlchemy introduction video](https://www.youtube.com/watch?v=sO7FFPNvX2s&ab_channel=SixFeetUpCorp). It lasts 3 hours but is extremely insightful, and introduces to some great object oriented patterns.
- [Handcoded application with SQLAlchemy](http://pyvideo.org/video/665/hand-coded-applications-with-sqlalchemy)
- [Alembic](http://alembic.readthedocs.org/en/latest/) is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.

### Standard library modules

- [Python built-in functions to know](https://treyhunner.com/2019/05/python-builtins-worth-learning/)
- [Understanding all of Python, through its builtins](https://sadh.life/post/builtins/)

Some little known standard library modules:

- [shelve](https://docs.python.org/3/library/shelve.html): Python object persistence

### Static analysis of code

- [Essential python tools - Quality](http://aboumrad.info/essential-python-tools-quality.html)

### Tests

Half of coding time is usually spent writing tests. Yet how to write tests efficiently is very rarely taught at school - even though it came make a huge difference in engineering productivity and quality.

First, make sure you're familiar with the different kind of testing strategies laid out in [Testing Strategies in a Microservices Architecture](http://martinfowler.com/articles/microservice-testing/) (Martin Fowler).

Then, read some of those articles:

- [Mock yourself, not your tests](http://hernantz.github.io/mock-yourself-not-your-tests.html): great articles about the danger of mocking, and better unit testing strategies.
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
- [pytest](http://pytest.org/latest/) is a test framework. It's very elegant and allows to quickly write very maintainable tests.
- [My Python testing style guide](https://blog.thea.codes/my-python-testing-style-guide/)
  - Assert results and outcome, not the steps needed to get there
  - Use real objects for collaborators whenever possible
  - A mock must always have a spec
  - Consider using a stub or fake
  - Consider using a spy
  - Don't give mock/stubs/fakes special names
  - Use factory helpers to create complex collaborators
  - Use fixtures sparingly

### Tools built with Python

- [pz](https://github.com/CZ-NIC/pz): easily handle day to day CLI operation via Python instead of regular Bash programs.

### Types

- [The state of type hints in Python](https://www.bernat.tech/the-state-of-type-hints-in-python/): a good summary of typing in Python and its gotchas.
- [Static Typing Python Decorators](https://rednafi.github.io/reflections/static-typing-python-decorators.html)
- [Static Duck Typing in Python with Protocols](https://www.daan.fyi/writings/python-protocols)
- [Writing Python like it’s Rust](https://kobzol.github.io/rust/python/2023/05/20/writing-python-like-its-rust.html)

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

If you want to get in touch, checkout [my website](https://www.dein.fr/).

## My other lists

- [engineering-management](https://github.com/charlax/engineering-management/)
- [entrepreneurship-resources](https://github.com/charlax/entrepreneurship-resources)
- [professional-programming](https://github.com/charlax/professional-programming)
- [python-education](https://github.com/charlax/python-education)
