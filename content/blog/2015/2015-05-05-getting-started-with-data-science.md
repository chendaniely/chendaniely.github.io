---
layout: post
title:  "Getting Started with Data Science and Analysis"
date:   2015-05-05

# categories: Tutorials

tags:
  - tutorials
  - opensource
  - python
  - r
  - data analysis
  - data science
---

I've been an instructor for [Software-Carpentry (SWC)](http://software-carpentry.org) over a year now.
It's been a facinating experience and I'm proud to be a part of an open source movement promoting best practices.
Typically when looking to start learing data science/analysis the first things people look up is something along the lines of: "learn python", "free online r course", "data science python", "r jobs", etc.
Or scan through the coursera offerings.
I'm a bit biased, but I think the SWC material is one of the best ways to just get familiar with the basics.
This isn't a blog post about SWC per se, but how one might go about learing and navigating some of the material on your own without attending a workshop.

<!-- more -->

# Software Carptentry Material

SWC has a page of [lessons](http://software-carpentry.org/lessons.html) that link to the various lessons taught during workshops.
The core material covers:

1. [Unix](http://swcarpentry.github.io/shell-novice/)
2. Some programming language like [Python](http://swcarpentry.github.io/python-novice-inflammation/), [R](http://swcarpentry.github.io/r-novice-inflammation/), [MATLAB](http://swcarpentry.github.io/matlab-novice-inflammation/), etc
3. Version control using [Git](https://github.com/swcarpentry/git-novice) or [Mercurial](https://github.com/swcarpentry/hg-novice)
4. Databases and [SQL](http://swcarpentry.github.io/sql-novice-survey/)

If you take a look and listen (there is sound) to the [introductory browsercase](http://swcarpentry.github.io/slideshows/introducing-software-carpentry/index.html#slide-3).
You will see that we say we teach the above material, but in essense we try to convey:

1. Automation of repetitive tasks
2. Tracking and sharing work
3. Building modular code
4. Manage data

It's a little bait-and-switch :)

# Installing Things

For each SWC workshop is accompanied by a [website](http://chendaniely.github.io/workshop-template-empty/).
The website Contains information about location, instructors, helpers, syllabus, etc.
For people reading this post, the most important part may be the installation instructions towards the middle/bottom of the page.
There are separate instructions depending on your operating system.

Essentially:

 - Python: [Anaconda](http://continuum.io/downloads)
 - R: [R](http://cran.rstudio.com/) and [RStudio](http://www.rstudio.com/products/rstudio/download/)

# Navigating the Material

For people who have not been to a workshop trying to navigate the lesson material can be tricky.
And I would highly suggest going through at least the first 3 [Unix](http://swcarpentry.github.io/shell-novice/) lessons.
This is mainly because loading files in a programming language uses the concept of relative and absolute paths, and it's important to know where your data is and how to load it.

Using the R material as an example.  The instructors typically teach from the [Novice R Inflammation](http://swcarpentry.github.io/r-novice-inflammation/) lessons.  There has been some [discussion](https://github.com/swcarpentry/r-novice-inflammation/pull/65#issuecomment-93483536) and plans to use the [Gapminder](http://www.gapminder.org/) data to teach lessons.  The beta can be found in the [R Novice Gapminder](https://github.com/swcarpentry/r-novice-gapminder) lesson.

Once you're on the github page of the lesson, there are a few ways to get the lessons plan

1. If you know your way around git, you can clone the repository
2. Otherwise, you will see an option to "Download ZIP" on the right panel.
3. View them in the browser

The first 2 methods get you do the same place -- have the lessons on your computer.
In order to view the lessons, open up the folder and all the lessons are numbered and end in `.html`.
Click, read, and code through them in order.

If you want to view the lessons online, you can click the `.Rmd` documents, and github should be able to render the lesson for you in the browser.  For Python and other materials, use the `.md` documents.
The caveat with viewing the `.Rmd` and `.md` (aka R markdown, and markdown respectively) is that it does not render the documently exactly the same way as the `.html` files.
There is a potential for things to be rendered incorrectly, and you'll see some bizzare (YAML) header on the top.
It's great for a quick reference when you're not at your computer, but I would suggest using one of the `.html` methods.


# Data Carpentry Material

Software Carpentry's sister organization, [Data Carpentry](http://datacarpentry.org/) also has a set of [lesson plans](http://datacarpentry.org/lesson-dev.html).
From their [about us](http://datacarpentry.org/about.html) page:

> Data Carpentry is a sister organization of Software Carpentry designed to teach basic concepts, skills and tools for working more effectively with data.
We develop curricula and run workshops that are 1) domain specific; 2) target fundamental data analysis and data management challenges; and 3) require little or no prior programming experience.
In many domains of research the rapid generation of large amounts of data is fundamentally changing how research is done. The deluge of data presents great opportunities, but also many challenges in managing, analyzing and sharing data. Data Carpentry aims to teach the data skills that will enable researchers to be more effective and productive.

Pick a language you want to do the lesson with.  `clone` or `Download ZIP`, and go through the lessons using the `.html`, `.Rmd`, or `.md` as mentioned above.

# Happy Learning!
Hopefully this has been clear enough.  If not, post a comment, and I'll respond and update this post accordinly.
