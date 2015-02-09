---
layout: post
title:  "Open Source A Python Project II: Documentation"
date:   2015-02-07
categories: Tutorials

tags:
  - opensource
  - python
  - sphinx
  - read the docs
---

- In [part I]() I introduced my [project]() and some of the initial hurdles.
- In this section I describe documenting your code using [sphinx]() and
publishing the documentation on to [Read the Docs]().
- In [part III]() I describe how to setup a package for PyPI.

tl;dr:

` sphinx-apidoc -F -o docs NAME_OF_FOLDER`.

Thanks to [Jeff Knupp](http://www.jeffknupp.com/) and his
'[Open Sourcing a Python Project the Right Way](http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)'.
post.

Don't make the mistake I did when
I was kinkering with a throwaway [example]() -- I put hyphens in the folder
name.  It will cause a lot of [problems](), use under_scores instead (or
better yet, pick a one-word module name).
If you tried to import a Python module with a hyphen,
it will cause problems within Python that will prompt you to use underscores,
so in practice, you shouldn't have the same problems as I did.

Take a look at the Python Sphinx [example](), and use it as a reference
on how to write a docstring.  Essentially there are two ways you can write them:

like this:

```python
def my_function(arg1 arg2):
	pass
```

or like this:
```python
def my_function(arg1 arg2):
	pass
```

# Sphinx

Once you have your code ready, you have to actully 'install' the module (I
discuss this at [Part I Importing Modules]()), otherwise sphinx won't really
see the actual code in the module, you'll end up with a list of module names
with no function definitions or documentation.

When you have the module installed you run:

` sphinx-apidoc -F -o docs NAME_OF_FOLDER`

It will create a `docs` folder in the root project directory.  At this point
you should be ready for [Read the Docs](), but if you want to view it locally,
go into the `docs` folder, and build the documentation by typing:

`make html`

if you want an html documentation.  There are other formats if you look at the
`makefile`, if you type `make` it will prompt you for a format as well.

The output of the `make` will be under the `_build/` and, in this case `html/`.
There will be an `index.html` file that will show you what the documentation
will look like in Sphinx or if you upload it to PyPI.

# Read the Docs
Once you see Sphinx is building correctly, you should be ready to point your
repository to [Read the Docs]().  The official setup documentation is
[here](),
but esseentailly, create an account, link it to your
[github]() account,
and have RTD track the repository that you are working on.
Make sure when you are setting up the RTD, under advanced settings, be sure
to use to dropdown menu and select `Sphinx HTML`.  I believe the
default would be something along the lines of `Automatically Choose`.
After that is all set, every push you make will cause RTD to rebuild the
documentation.

Select `Python` under Programming Language
