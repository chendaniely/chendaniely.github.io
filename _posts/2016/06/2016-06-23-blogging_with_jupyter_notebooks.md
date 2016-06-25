---
layout: post
title:  "Blogging with Jupyter Notebooks"
date:   2016-06-23

categories: Tutorials

tags:
  - python
  - jupyter notebook
  - jekyll
  - blogging
---

I'm trying to get into a habbit of writing regularly.
I've noticed over the past few years,
my ability to write a coherent English sentence is rapidly deteriorating;
I wasn't a great writer to begin with either.

Since I do a lot of programming already,
it would greatly help my cause if I could easily incorporate [Jupyter Notebooks](http://jupyter.org/)
into my [Jekyll](https://jekyllrb.com/) blog posts.

<!-- more -->

I've also wrote a mini notebook simulation about the Watts model in a [previous post]() that I'd like to publish.

[There][10] [are][9] [a][1] [lot][2] [of][3] [blog][4] [posts][5] [that][6] [describe][7] [what][8] [I][11] am trying to accomplish.
Luckily, I've [google-fu](http://www.urbandictionary.com/define.php?term=google-fu)'ed my way to better tutorials:

- [http://christop.club/2014/02/21/blogging-with-ipython-and-jekyll/][7]
- [http://mcwitt.github.io/2015/04/29/jekyll_blogging_with_ipython3/][6]
- [http://briancaffey.github.io/2016/03/14/ipynb-with-jekyll.html][8]

# Method 1: `jupyter nbconvert --to markdown`

`jupyter nbconvert` has gotten much better since I've last tried to do this.
An example of exporting an existing `jupyter notebook` as a `markdown` file can be found [here]().

Brian Caffey describes the process in [his post](http://briancaffey.github.io/2016/03/14/ipynb-with-jekyll.html),
but it requires a bit of post processing to get images to render properly.
This is beacuase `nbconvert` will create images in a subfolder, so you need to link to them accordinly.

Luckily, something like this could be delt with in a `makefile`, or a really simple python script.

# Method 2: custom jekyll templates and python parser

The second method uses the existing `jupyter nbconvert` infrastructure to create 



[1]: http://predictablynoisy.com/blogging-in-wordpress-with-ipython-jupyter-notebooks/
[2]: http://www.southampton.ac.uk/~fangohr/blog/blogging-with-the-ipython-notebook.html
[3]: https://gist.github.com/cscorley/9144544
[4]: https://github.com/cscorley/cscorley.github.io/blob/master/notebooks/Blogging%20with%20IPython%20and%20Jekyll.ipynb
[5]: http://www.davidketcheson.info/2012/10/11/blogging_ipython_notebooks_with_jekyll.html
[6]: http://mcwitt.github.io/2015/04/29/jekyll_blogging_with_ipython3/
[7]: http://christop.club/2014/02/21/blogging-with-ipython-and-jekyll/
[8]: http://briancaffey.github.io/2016/03/14/ipynb-with-jekyll.html
[9]: http://blog.fperez.org/2012/09/blogging-with-ipython-notebook.html
[10]: http://www.damian.oquanta.info/posts/deploy-your-nikola-powered-blog-content-from-the-ipython-notebook.html
[11]: https://adamj.eu/tech/2014/09/21/using-ipython-notebook-to-write-jekyll-blog-posts/