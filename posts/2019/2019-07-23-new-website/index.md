---
title: New Website a la Blogdown!
author: Daniel Chen
date: '2019-07-23'
slug: []
categories: []
tags:
  - rstudio-internship
  - r
  - hugo
  - blogdown
  - website
subtitle: 'At least I accomplished something this internship! xD'
summary: ''
authors: []
lastmod: '2019-07-23T20:22:45-04:00'
featured: no
projects: []
---

I finally got everything moved over to [blogdown](https://bookdown.org/yihui/blogdown/)
with the [Hugo](https://gohugo.io/) [Academic](https://github.com/gcushen/hugo-academic) theme.
Thanks so much to [Allison Hill](https://alison.rbind.io/), who ran the [summer-of-blogdown](https://summer-of-blogdown.netlify.com)
tutorial for us [RStudio interns](https://blog.rstudio.com/2019/03/25/summer-interns-2019/).

<!-- more -->

The transition was pretty seamless. Mainly because I didn't really have that much content to move over.
The biggest change was I had to commout my `categories` tag in my YAML post headers becuase they were causing the
site to not build.

While writing this post, I just realized that the way categories and tags are specified in hugo
are not the same as jekyll.

In jekyll I could write categories as

```yaml
categories: R
```

or

```yaml
categories:
  - R
```

But in hugo it seems it's a list written as

```yaml
categories: ['R']
```

Anyway, it was fun going through and enabling/disabling different widgets.
I'll keep it simple for now, and build on the site accordinly.
I'm just happy I can maintain my website without worrying how I had Jekyll setup to properly `serve` the site.
The folks at RStudio truely make things easy for us end users.

The other change I did was to make my old repository, `chendaniely.github.io` a submodule of my blogdown site repo
and change the target folder the published contents will be from the default `public` by addding this
to my main `config.toml` file

```toml
publishDir = "chendaniely.github.io"
```

This way my old url will still work (I'm really attached to the `.github.io` domain),
but I can still have netlify deploy everything and have my `rbind.io` domain as well.
Everything will look the same, and I'll work on redirecting everything to a single domain sometime later.

I also needed to change the `[build]` section in my `netlify.toml` file to point to the new build location

```toml
[build]
  # publish = "public"
  publish = "chendaniely.github.io"
```

Netlify is a little wonky when you have SSH keys enabled with the submodule.
I get an error message because when Netlify tries to clone the submodule I get a permission error

```
fatal: clone of 'git@github.com:chendaniely/chendaniely.github.io.git' into submodule path '/opt/build/repo/chendaniely.github.io' failed
```

That makes sense, the Netlify servers do not have SSH keys setup on my GitHub account.
I haven't figured out how to do this yet, so I switched my `.gitmodule` url to the https link.
However, that means, for the time being, I created another remote with my SSH url (`git remote add originssh ...`)
and I have to push using that remote instead of the `origin` url (which is the https link).

Now to start that massive backlog of things I've been doing this summer ( :
