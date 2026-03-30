---
layout: post
title:  "RStudio internship week 2"
subtitle: "I think I can make it through the summer"
date: "2019-06-18"

tags:
  - R
  - rstudio-internship
---

The main topics and events of last week were:

1. Much git.
2. Metaprogramming and non-standard evaluation (NSE) in R
3. Four 1-hour workshops by Allison Hill on the [summer-of-blogdown][summer-of-blogdown]
    - moving things over from jekyll will take some time

So many of the random things I've tinkered with in the past have come front and center.
As an educator,
I know seeing these things again make learning and understanding them easier.
You build on your previous knowledge to solidify, fix, and fill in gaps in your mental model.
The process repeats until you get an understanding about a topic.

For me, I'm getting a better foundation to how NSE works and how it all plays together within the Tidyverse.

<!-- more -->

### Git

I got some things merged!

The [pull-request][grader-pr-10] that was broken and merged on my first day finally was [fixed and merged][grader-pr-14].
I also got to work with the [lintr][lintr] package and [merged it into `grader`][grader-pr-17] too.

This week was probably the first time I've used `git amend` in a long time (if ever?).
I've typically always just made the commit, and run `git rebase -i` to squash and/or amend my commits.
I can see why common operations like making changes to the previous commit would have a shortcut.
I typically don't use these features because it's another thing to teach, and understanding `git rebase -i` is more general than `git commit --amend`.

What `--amend` allows you to do is replace the previous git commit with another one.
You can fix the commit message, or add/fix file you missed.
Theses are all ways to make the commit history cleaner.

The recipe looks like this:

```bash
git add <file>
git commit --amend

<Fix/modify the commit message>

git push -f origin master
```

The last line does a `-f` force `push`, because the commit is actually different from the one before you `--amend`ed.

### R package versions

There's a convention about version numbering adding a `.9000`+ after the patch (e.g., v0.1.4.9000) to show a
a development version number.
You can couple this with the `DESCRIPTION` file by forcing a particular version to make sure you and the team
all have access to the same development features.

[I came across this in `grader`][grader-description] that has a `Imports` for `learnr (>= 0.9.2.9001)`.

### `grader` progress

We're probably [going to change the name of the package][grader-is-18] to
`gradethis` because the package `gradeR` (note capital R) was submitted to CRAN right as I started.

Here's what I learned about the library I'm working on this week:

- `learnr` set's the `checker` function
    - In the knitr chunk `exercise.checker` specifies the `checker` function
        - `tutorial_options(exercise.timelimit = 60, exercise.checker = grade_learnr)`
    - In this example, `grade_learnr` is the main entrypoint from `learnr` to `grader` and my work starts with this function.
- `checker` is called on [line 129 in `exercise.R` in `learnr`][checker-call]
    - the `checker` function (i.e., `grade_learnr`) returns a value depending on what is passed into it
        - if missing: returns a `list()` with `message`, `correct`, `type`, and `location` keys
        - if error: `graded` object (named `checked_result` of class `grader_graded`) with `correct` and `message`
        - or evaluated code

There's a bunch of stuff within the `exercise.R` function in `learnr` that captures information from shiny,
sets up the `knitr` environment, and inserts the output and results into the correct place in the DOM.
That'll be a separate writeup when I leave the `grader` world.

For the next week or so the goal is to update the [`check_result` API][grader-is-11],
which got me down the rabbit hole of non-standard evaluation in R (I'll talk about it in a separate set of posts).

### Non-standard Evaluation (NSE)

I gave [a talk][satRday-function] about writing functions in R which touched on NSE but it was pretty superficial.
Since NSE is so crucial to `grader` I'll write a series of posts about this topic and eventually turn it into a talk.

In the meantime, here are the materials (in no particular order) I'll be reading to:

- [https://dplyr.tidyverse.org/articles/programming.html](https://dplyr.tidyverse.org/articles/programming.html)
- [https://tidyeval.tidyverse.org/](https://tidyeval.tidyverse.org/)
- [https://ggplot2.tidyverse.org/dev/articles/ggplot2-in-packages.html#using-aes-and-vars-in-a-package-function](https://ggplot2.tidyverse.org/dev/articles/ggplot2-in-packages.html#using-aes-and-vars-in-a-package-function)
- [https://adv-r.hadley.nz/](https://adv-r.hadley.nz/)


### Misc

Other random things I've discovered this week

#### `dplyr::count` vs `dplyr::tally`

From the docs:

> tally() is a convenient wrapper for summarise that will either call n() or sum(n) depending on whether you're tallying for the first time, or re-tallying.
> count() is similar but calls group_by() before and ungroup() after. If the data is already grouped, count() adds an additional group that is removed afterwards.

`dplyr::count` can count observations with 0 counts (useful for group_by operations) with the `.drop` argument

#### `pryr::standarise_call`

Manipulating the function call is black magic NSE voodoo.
This is the stuff that is happening within `grader` that gets student code, solution code, `learnr` and `grader` arguments
that are all passed into `grade_learnr`.

```r
# code below was copy/pasted from the console

my_add <- function(x, y) {
  x + y
}

# pass in part of an expression
call <- pryr::standardise_call(quote(my_add(x = 3)))

# on the fly add more parameters!
call$y <- 10 

# evaluate the thing
eval(call) 

## [1] 13
```

This all uses the global environment,
but `grader` will be doing this type of thing with separate environments for each exercise that will be checked.

Also, this is all how `match.call` works in base R.

#### `checkmate` package

There is a [package called `checkmate`][pkg-checkmate] that is unit testing (e.g., `testthat`) on steroids.
It allows you to more specific type and argument checking in R.
I haven't work with the package personally yet, but it does seem to be like [type hints in Python][python-type-hints]
and allows more specific checks into what objects in R contain.


#### Credentials

One of the coolest things about being an intern at RStudio is being on the slack channel!
I try to keep my questions reserved but one of the things that have always bothered me was how store and access credentials for R.
Putting in API keys in `.Renviron` are common practice, but I piggy-backed on another intern's question by asking about
storing passwords more securely than in a plain text file.

I've used the [`rstudioapi`][pkg-rstudioapi], [`secret`][pkg-secret], and [`getPass`][pkg-getPass] libraries [before][pkg-sdalr],
but as [Raymond Hettinger][raymondh] always says: There must be a better way.

The resource I was given was to look at how database credentials are stored: https://db.rstudio.com/best-practices/managing-credentials/

### Summer of blog down

Lastly,
the great Allison Hill hosted a series of blogdown workshops for people who were interested, [summer-of-blogdown][summer-of-blogdown].
It was a total of 4 days and we covered
the basics of blogdown,
how to pick (the [academic][hugo-academic]) themes,
[deploying it on netlify][netlify-chendaniely],
and best ways to maintain the site.

I didn't realize how amazingly flexible the [academic][hugo-academic] theme was until this workshop.
I'll be sure to move [my own website][jekyll-chendaniely] over to blogdown + academic one of these days.

I'm currently trying to find out how to save urls in a common location so they can be maintained in one place and be used in links throughout the site.
The ongoing search for how to use variables in an `md` document (tl;dr: you can't, but you might still be able to do what I want):
https://discourse.gohugo.io/t/variables-in-markdown/7113/12.
It almost seemed that [site variables](https://gohugo.io/variables/site/)
were going to be the way to go, but that ended up in a dead end.

What I'm most excited about is the ability to write posts in `Rmd` and `jupyter notebooks` for R and Python posts.

Things I've learned the 4 days:

- Each folder in content is a "section" and each "section" has a "page"
- `/content/home/` contain widgets
- [Learn x in y minutes](https://learnxinyminutes.com) website for [TOML](https://learnxinyminutes.com/docs/toml/)
- From Greg Wilson: Put a `LICENSE` and `CITATION` + [orcid](https://orcid.org/0000-0003-3857-1741) on your website. Make the librarians happy.


[summer-of-blogdown]: https://summer-of-blogdown.netlify.com
[work-effectively]: https://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052
[grader-pr-10]: https://github.com/rstudio-education/grader/pull/10
[grader-pr-14]: https://github.com/rstudio-education/grader/pull/14
[grader-pr-17]: https://github.com/rstudio-education/grader/pull/17
[lintr]: https://github.com/jimhester/lintr
[grader-is-18]: [https://github.com/rstudio-education/grader/issues/18]
[checker-call]: https://github.com/rstudio/learnr/blob/master/R/exercise.R#L129
[grader-is-11]: https://github.com/rstudio-education/grader/issues/11
[satRday-function]: https://github.com/chendaniely/satRdays-dc2018-functions
[grader-description]: https://github.com/rstudio-education/grader/blob/master/DESCRIPTION
[python-type-hints]: https://docs.python.org/3/library/typing.html
[pkg-checkmate]: https://mllg.github.io/checkmate/index.html
[pkg-secret]: https://cran.r-project.org/web/packages/secret/vignettes/secrets.html
[pkg-getPass]: https://cran.r-project.org/web/packages/getPass/index.html
[raymondh]: https://twitter.com/raymondh
[pkg-rstudioapi]: https://cran.rstudio.com/web/packages/rstudioapi/index.html
[pkg-sdalr]: https://github.com/bi-sdal/sdalr
[netlify-chendaniely]: https://chendaniely.netlify.com/
[hugo-academic]: https://themes.gohugo.io/academic/
[jekyll-chendaniely]: https://chendaniely.github.io/
