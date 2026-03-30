---
layout: post
title:  "Open Source A Python Project I"
date:   2015-02-05

# categories: Tutorials

tags:
  - tutorials
  - opensource
  - python
  - nosetests
  - pip install

---

I started my
[first](https://github.com/chendaniely/multi-agent-neural-network)
open source project towards the end of summer 2014 I began working at
the [Social Decision Analytics Laboratory](http://vbi.vt.edu/sdal) at
the [Virginia Informatics Institutee](http://www.vbi.vt.edu/).  The
project involves creating a simulation environment where we can
observe how an idea or belief spreads within a social network.  The
initial thought was to look for and extend an
[agent-based model](http://en.wikipedia.org/wiki/Agent-based_model)
package in Python.  I did manage to find the
[pyabm](https://github.com/azvoleff/pyabm) package by
[Alex Zvoleff](http://azvoleff.com/), but for simplicity's sake I
wrote my own package instead of extending his existing code base.

I took it as an opportunity to learn and 'do things right':

- Write a module that contains all program logic
- Write functions that only do only one thing, but does it well
- Unit test everything
- Test builds on different versions of Python
- Document your code
- Get it on [PyPI](https://pypi.python.org/pypi)
- [PEP8](https://www.python.org/dev/peps/pep-0008/)

This series of posts are essentially notes to myself, and to other
programmers who are starting out from where I was.  In this post I
discuss the background, rational, and inital steps in my open source
struggles.  In
[part II](https://github.com/chendaniely/chendaniely.github.io/blob/draft-os-python2/_posts/2015-02-05-open-sourcing-a-python-project-II.md)
I discuss automatic project and code documentation.

<!-- more -->

# Background

I had already been involved with
[Software Carpentry (SWC)](http://software-carpentry.org/) for about 8
months when I started the project, so many of the concepts I just
listed were not entirely foreign, just a matter of implementation.
Thanks to a workshop by
[Gabriel Perez-Giz](http://www.ccpp.nyu.edu/gabriel_perez-giz.html) at
NYU earlier that summer, I took it upon myself to practice my EMACS
and setup [elpy](https://github.com/jorgenschaefer/elpy) as my IDE.  A
development environment that can be used within a terminal was
especially important, because the simulations I would be running would
all be on a remote server.

For git, it was getting into the habit of not committing directly to
master.  For Python, I'd write a suite of unit tests for the first
time, and I figured if I write some comments and docstrings I can get
a nice document from it (I was wrong about that).  Finally, I wanted
to get those cool little badges people have on their github repo about
build status, coverage, etc.  That's when I found an awesome blog post
by [Jeff Knupp](http://www.jeffknupp.com/) titled
'[Open Sourcing a Python Project the Right Way](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)'.

It's an amazing read if you are ready to take your programming
practices to the next step.  Jeff references a
[cookie-cutter](https://github.com/audreyr/cookiecutter-pypackage)
that will setup the python project boilerplate, but I opted to just
follow the blog post and do everything manually so I can have a better
understanding as to what is going on in the background.  Plus, this
lets me slowly add features, rather than have an entire repo loaded
with unknown files.  More important, I added a few other things to
make my project 'better':

- Use the
[git](https://www.atlassian.com/git/tutorials/comparing-workflows/centralized-workflow)-[flow](http://nvie.com/posts/a-successful-git-branching-model/)
paradigm to add new features
- Continuous integration (with
  [TravisCI](https://travis-ci.org/recent))
- Test your package with other versions of Python (using
  [Tox](https://tox.readthedocs.org/en/latest/))
- Code documentation with [Sphinx](http://sphinx-doc.org/) and
  [Read the Docs](https://readthedocs.org/)

I opted not to use Tox locally (at least not yet).  TravisCI is
handling my Python compatibility since I was working with Python 3.4,
and was not going to have Python 2 support.  I added a build for
Python 3.4 and 3.3, and called it a day.  Also I opted to use
[nosetests](https://nose.readthedocs.org/en/latest/) instead of
[pytest](http://pytest.org/latest/) since that's what I was shown when
I helped out at the
[MIT SWC workshop](http://geocarpentry.github.io/2014-01-30-mit/).
That, plus there was SWC
[material](http://software-carpentry.org/v4/test/index.html), and
other [big](https://github.com/numpy/numpy) open source projects use
it, was my rational to stick with `nosetests`.

<hr>

# My project

The original
[Multi-Agent Neural Network (MANN)](https://github.com/chendaniely/multi-agent-neural-network)
project had a `main.py` script that loaded in my modules for the
individual agents and the network structure.  Everything was placed
under the `mann` folder in the repo, with no subfolders.  When I
eventually realized that I wanted the project to be PyPI ready, I
wanted to separate the main program logic (the MANN code) from the
actual script that sets up the simulation.  I eventually moved the
`main.py` script (and all required files) into the
[Multidisciplinary Diffusion Model Experiments (MDME)](https://github.com/chendaniely/multidisciplinary-diffusion-model-experiments)
repo.

# Prerequisites

I've realized the more I program in python, the more invaluable
virtual environments are when developing packages.  A Virtual
Environment is a tool to keep dependencies required by different
projects in separate places while simultaneously keeping your base
python distribution clean and working should something go awry.  They
also allow you to flip between Python 2 and Python 3 depending on what
version a piece of code you are trying to run was written in.  Pretty
cool stuff.

The Python distribution I use is called
[Anaconda](http://continuum.io/downloads).

Setting up virtual environments using `conda`:

`conda create -n VIRTUAL_ENV_NAME python=3.4`

You can specify different versions of python and/or pre-create
environments with a set of modules if needed.

Switching between environments: `source activate VIRTUAL_ENV_NAME`

To exit out of an environment: `source deactivate`.

You can read up more about creating environments on the conda
documentation

- [Createing Python 2/3 environments](http://conda.pydata.org/docs/intro.html#creating-python-3-4-or-python-2-6-environments)
- [`conda create`](http://conda.pydata.org/docs/examples/create.html)
- [Python Packages and Environments with conda](http://www.continuum.io/blog/conda)

# Issues

Turning a current python project into a 'module' can break a few
things.  It is as simple as putting a `__init__.py` into a directory
to signify that the contents of the folder is now a Python module, but
there can be some weird side-effects.

# Unit tests

When you turn your project into a package, you will find that if you
run nosetests it will start running the unit tests for all the modules
you load (if they have any).

For example I was initially using

`nosetests --cover-branches --with-coverage`

to test my code, but I had to add the `--cover-package=MODULE_NAME` to
get it to only test the code in my module:

`nosetests --cover-branches --with-coverage --cover-erase
--cover-package=mann`

# Importing Modules

Since I've moved out my simulation code from the code that defines
that MANN module, I had to install the MANN module.  One way to do it
is to upload the code to PyPI and `pip install` the package.  The
problem is when you want to load a module to PyPI you essentially need
to have a git tag associated with the version you want.  This is
problematic when you are rapidly prototyping since you'll need to
either delete tags, or constantly increment the tag.  You'll end up
with a v.0.314.0 very quickly.  You can do a local install of your
module by going to where you have the setup.py file and doing:

`python setup.py install`

This is why virtual environments are really helpful.

1. You won't have to worry about cluttering the base Python
distribution and modules with your 'test' code.
1. You can test your code before uploading it to PyPI (or anywhere
   else).  This is really helpful becuase PyPI requires you to have a
   `tag`.  Doing a local install allows you to workout any potential
   bugs before submitting a release so you won't have to have 15
   release numbers for your first release.
