---
layout: post
title:  "And we're off! RStudio internship week 1, complete."
subtitle: "First week of internship is over and I can't believe this is actually happening"
date: "2019-06-10"

tags:
  - R
  - rstudio-internship
---

I'm still pinching myself about being one of the [RStudio interns this year][1].
It's an unbelievable opportunity and I've been half panicked and fighting imposter syndrome since the [announcement was made in March][1].
My meeting with [Greg Wilson][4] on Friday (2019-06-07) went something like this:

```
Greg Wilson: How's the internship going?
Me: I'm panicked, but really excited.
Greg Wilson: Good. That's how interns should feel.
```

I'm working on the [grader][2] package (with [Garrett Grolemund][garrett] and [Barret Schloerke][barret]) which aims to check code against a solution.
This package integrates with the [learnr][7] package, that allows an RMarkdown document to be run as an interactive tutorial (more on this after the break).

My internship began with a [broken pull request][5] that needs to [be fixed][6].

<!-- more -->

### The `learnr`/`grader` packages

`learnr` allows users to write interactive tutorials/lessons (using [RMarkdown][8]) that give instructors to write interactive tutorials (using [shiny][9]).
Learners will be able to follow the tutorial write and execute R code that will be graded.
Under the hood, `learnr` is an [RMarkdown document][8] with [runtime: shiny][9].
This allows the user (e.g., instructor) to write tutorials using markdown and provide solutions using code chunks and all the magic of capturing and checking the answer with `shiny` and `grader`.

There are two main ways code can be graded.

- Comparing results
- Comparing the provided student code with the solution code (i.e., strict checking).
    - One way this can be done is by looking at the [abstract syntax tree][3].
    - Another way would be some fancy set of string matching / regular expressions.

When I started, there were some [API changes][5] that were made and I've spent my first week going down various rabbit holes [fixing tests and getting `R CMD check` to pass][6].
Barret has been super helpful and supportive by walking me through the code base and helping me fix the broken things.
I'm pretty sure he did all the work in [my PR][6].

### General goals for the summer

This will be a moving target, but it seems like after the first week these may be good goals for the summer:

- A ([pkgdown][pkgdown]) vignette for the `grader` user API and a separate one for the developer API.
- Blog post of how learnr works, and what order to expect error messages (see [use-case maps][use-case_maps]).
- Put together a `grader` example without the use of `learnr`
    - An example would be to pass `grader` 2 R scripts (the student code and the solution code).
    - This came up while I was talking to Greg and he brought up "Working Effectively with Legacy Code" by Michael Feathers
        - This will help me find the entry points to the package, write isolated tests, and have a clearer goal of the project.
        - Along with [use-case maps][use-case_maps], this will help me be a better software developer and understand what's actually going on (did I mention I'm half panicked and fighting imposter syndrome?)

Other goals would be to have:

- Virtual coffee meetings with other people in the company (there's a channel called "virtual-donut" that has a scheduler bot)
- See if I can draft up and hunt down the people for a PhD topic.
    - Greg really planted a seed in my head a few months ago about putting together materials to help "front-line health practitioners (e.g., nurse and general practitioners) use and understand data".
    - I think I can... I think I can... I think I can...

### Random things I've learned so far

- I think I really like this 100% remote work schedule, I've been up way earlier than usual finishing things before a morning meeting and then taking my time the rest of the day planning and implementing things.
    - I also feel like a teenager in chatrooms talking to everyone (thanks Slack!)
- [Using Templates with Roxygen2][10]: allows [roxygen2][roxygen2] docstrings to be reused by using a `@template` Rd keyword
- [Use-case maps][use-case_maps]: document and show the various components of an application,
but also show what components are used for a given action
    - This would be great for `learnr` and `grader` since I'll pretty much be doing this for myself just to figure out all the moving parts of the system and how each component works in the full application.
- [lintr][lintr]: is a way to do static code analysis in R.
    - You can use this to check for (potential) errors before runtime
    - Pretty sure I can take the same idea and apply it to `grader`
- All these years practicing my Git-fu seems to be paying off.
- My mentor, Garrett Grolemund, is RStudio employee number *insert number that can be represented with 1 hand* :O
- There's an "emoji-psa" channel at RStudio. It's active. People really know their emojis. owo

### Misc

- I've given up trying to sync the GSuite with Thunderbird and having a unified calendar.
    - I'm using [openWMail][openWMail] again for my RStudio calendar/drive.
    - Still have all my emails in Thunderbird.
- Not all the interns started on the same date. Most of us started June 3rd, but some started earlier and others will start later.
    - Us interns have our own slack **workspace**!
    - We had our first interns-only coffee chat on Friday.
        - Malcolm Barrett, Julia Blum, Joyce Cahoon, Desiree De Leon, Dewey Dunnington, and Maya Gans all met this week.
        - We're planning to have an intern "host" one each week so everyone gets a chance to meet some (if not all) of us.
- [Allison Hill][allison] is hosing a ["Summer of blogdown"][summer-blogdown] this week, so I'll probably be doing another website update.

[1]: https://blog.rstudio.com/2019/03/25/summer-interns-2019/
[2]: https://github.com/rstudio-education/grader
[3]: https://adv-r.hadley.nz/expressions.html
[4]: http://third-bit.com/
[5]: https://github.com/rstudio-education/grader/pull/10
[6]: https://github.com/rstudio-education/grader/pull/14
[7]: https://github.com/rstudio/learnr
[8]: https://rmarkdown.rstudio.com/
[9]: https://bookdown.org/yihui/rmarkdown/shiny-documents.html
[pkgdown]: https://pkgdown.r-lib.org/
[use-case_maps]: http://third-bit.com/2018/12/27/use-case-maps.html
[10]: https://stackoverflow.com/questions/15100129/using-roxygen2-template-tags/15143507#15143507
[roxygen2]: https://cran.r-project.org/web/packages/roxygen2/index.html
[openWMail]: https://github.com/openWMail/openWMail
[lintr]: https://github.com/jimhester/lintr
[allison]: https://alison.rbind.io/
[summer-blogdown]: https://summer-of-blogdown.netlify.com/
[garrett]: https://twitter.com/statgarrett?lang=en
[barret]: https://twitter.com/schloerke
