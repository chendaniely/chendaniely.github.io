---
layout: post
title:  "Open Source A Python Project I"
date:   2014-09-29 20:40:00
categories: opensource python
---

I started my [first](https://github.com/chendaniely/multi-agent-neural-network) 
open source project towards the end of summer 2014 I began working 
at the [Social Decision Analytics Laboratory](http://vbi.vt.edu/sdal) at 
the [Virginia Informatics Institutee](http://www.vbi.vt.edu/).
The project involves creating a simulation environment where we can observe how an idea or 
belief spreads within a social network.  The initial thought was to look for and extend
an [agent-based model]() package in Python.  I did manage to find the 
[pyabm](https://github.com/azvoleff/pyabm) package
by [Alex Zvoleff](http://azvoleff.com/), but for simplicity's sake I wrote
my own package instead of extending his existing code base.

I took it as an opportunity to learn and 'do things right':

- Write a module that contains all program logic
- Write functions that only do only one thing, but does it well
- Unit test everything
- Test builds on different versions of Python
- Document your code
- Get it on [PyPI](https://pypi.python.org/pypi)
- [PEP8](https://www.python.org/dev/peps/pep-0008/)

This series of posts are essentially notes to myself, and to other programmers
who are starting out from where I was.

<hr>

# Background

I had already been involved with [Software Carpentry (SWC)](http://software-carpentry.org/)
for about 8 months,
so many of the concepts I just listed were not entirely foreign, just a matter
of implementation.  Thanks to a workshop by [Gabriel Perez-Giz](http://www.ccpp.nyu.edu/gabriel_perez-giz.html)
at NYU earlier that summer,
I took it upon myself to practice my EMACS and setup [elpy](https://github.com/jorgenschaefer/elpy) for my IDE.
A development environment that can be used within a terminal was especially important, because
the simulations I would be running would all be on a remote server.

For git, it was getting into the habit of not committing directly to master.
For Python, I'd write a suite of unit tests for the first time, and I figured
if I write some comments and docstrings I can get a nice document from it (I was wrong about that).
Finally, I wanted to get those cool little badges people have on their github repo
about build status, coverage, etc.  That's when I found an awesome blog post
by [Jeff Knupp](http://www.jeffknupp.com/) titled 
'[Open Sourcing a Python Project the Right Way](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)'.

It's an amazing read if you are ready to take your programming practices to the next step.
Jeff references a [cookie-cutter](https://github.com/audreyr/cookiecutter-pypackage)
that will setup the python project boilerplate, but I
opted to just follow the blog post and do everything manually so I can have a better
understanding as to what is going on in the background.  Plus, this lets me slowly add features,
rather than have an entire repo loaded with unknown files.  More important, I added a few other
things to make my project 'better':

- Use the [git-flow]() paradigm to add new features
- Continuous integration (with [TravisCI]())
- Test your package with other versions of Python (using [Tox]())
- Code documentation with [Sphinx]() and [Read the Docs]()

I opted not to use Tox locally (at least not yet).
TravisCI is handling my Python compatibility since I was working with Python 3.4, and was not going to
have Python 2 support.  I added a build for Python 3.4 and 3.3, and called it a day.
Also I opted to use `nosetests` instead of `pytest__________` since that's what I was shown when I
helped out at the [MIT SWC workshop]().  That, plus there was
SWC [material](http://software-carpentry.org/v4/test/index.html),
and other [big](https://github.com/numpy/numpy)
open source projects use it, was my rational to stick with `nosetests`.

<hr>

# My project

The original
[Multi-Agent Neural Network (MANN)](https://github.com/chendaniely/multi-agent-neural-network)
project had a `main.py` script that
loaded in my modules for the individual agents and the network structure.
Everything was placed under the `mann` folder in the repo, with no subfolders.
When I eventually realized that I wanted the project to be PyPI ready, I wanted
to separate the main program logic (the MANN code) from the actual script that
sets up the simulation.  I eventually moved the `main.py` script (and all required files)
into the
[Multidisciplinary Diffusion Model Experiments (MDME)](https://github.com/chendaniely/multidisciplinary-diffusion-model-experiments)
repo.
