---
layout: post
title:  "Analysis-Based Project Templates"
date:   2018-01-23

#category: Data Engineer

tags:
  - sdal
  - data science
  - dspg
  - dspg17
  - programming practices
  - sdal-post
---

One of the most annoying things you hear people say when they are working with some common code base is
"It works on my machine...".
Conversely, one of the more satisfying things is running a script that you are not actively working on and
have it run without problems.

[Project Templates]({% post_url 2017-05-30-project_templates %}) are one way to address this problem.
The [original post]({% post_url 2017-05-30-project_templates %}) about project templates mainly talks about the folder structure but not so much as the rationale behind why things are the way they are.
Also the original post used a user-based subfolder structure under `src`,
which caused some problems when we ended up doing code reviews.

Why do we even want to use "projects"?
[Software Carpentry](https://software-carpentry.org/) has a good set of [explanations](https://swcarpentry.github.io/r-novice-gapminder/02-project-intro/).
When dealing with [working directories and workspaces](https://support.rstudio.com/hc/en-us/articles/200711843-Working-Directories-and-Workspaces) within R and RStudio,
even RStudio suggests [using projects](https://support.rstudio.com/hc/en-us/articles/200526207).

<!-- more -->

Hopefully the links above are convincing enough to use projects and some standardized folder structure within projects.
Below are some of the issues we've encountered while working on various projects, and hopefully
we can slowly migrate to a standardization for all projects and analysis moving forward. 
Some of the problems and solutions are already mentioned from the Software-Carpentry and RStudio links above.

# Problems

1.  **Manually setting a working directory in a script.**
    - Reduces the reproducibility by hard-coding a path specific to each user.
    - When sharing code, each person needs to manually edit at least one line within the file to set the working directory.
    - Results and other saved outputs from code are also tied to the working directory
2.  **Sharing code within a project by copy/pasting from another script.**
    - Redundant routines in code should always be encapsulated into a function so they can be re-used within a script and shared across scripts.
    - Since duplication of code is minimized, a fix in one location should provide the same fix in other locations.
    - We've had situations where code was copy/pasted into multiple scripts and multiple bugs were introduced/fixed in multiple places but neither set of duplicated code contained all the bug fixes.
3.  **Username subfolders in the `src` folder**
    - Promoted code duplication and made it hard to find a particular analysis.
    - Originally set up this way to minimize merge conflicts
    - Individuals can quickly find his/her own work
    - Became a problem because instead of sharing code that needed to be reused, people started copy/pasting code into scripts
    - See duplication of code problem from the previous point
    - During the code review process, finding code that did a certain task was difficult since it was organized by
    who did a task, versus the task itself.
4.  **Manually setting working directories while under a version control systems (VCS)**
    - VCS keep track of changes from files.
    - Even if there is a general understanding of manually setting a working directory among collaborators,
every time someone changes the working directory to run on their machine,
the version control system will report a change in the file.
    - While the changes can be reverted by the VCS, it's an unnecessary step in the work flow,
and can lead to unwanted changes in the code if a file was reverted unexpectedly.
    - Or you will end up with the same lines and files being changed over and over, cluttering the log and history.

# Solutions

Many of these problems can be solved with using [RStudio Projects](https://support.rstudio.com/hc/en-us/articles/200526207).

1. **Prevents scripts from setting a working directory (`setwd()`)**
    - The working directory will be the root of the project.
    - Since the starting point for each script is deterministic, we can implement a folder structure within the project in a way
where data has a common access point (e.g., `./data/path/to/data`) and code that needs to be run will also have a common access point (e.g., `./src/path/to/script.R`)
2. **Code and scripts can be easily be referenced from the root working directory of the project**
    - When someone wants to create a script to hold functions, it has a consistent path to be `source`d in another R script
    - This would provide a place for common code bases to be shared without copy/pasting into multiple scripts and
without having to be put into a proper R package.
3. **The structure of the project template needs to account for multiple people entering and leaving a project at various points during the lifetime of a project**
    - We have a `src` folder so people knew where to put his/her `R` scripts
    - needed a way to organize the folder so we don't have 10s or 100s of files in a single directory.
    - We initially settled on using user name sub-folders.
        - This prevented a lot of potential merge conflicts, since people are more likely to just work in their own directory
        - but it also caused people to copy/paste from other people's folders.
        - It also made it difficult to find out later on how to find a particular piece of analytics.
        - We would have to know who worked on it to find the script, versus looking up the analysis itself.
    - Thus, we are moving to a naming system not under user names.
        - This also will prevent copy/pasting of common code bases.
        - One thing that can happen is more merge conflicts (editing the same line of a file at the same time) while working
            - but even that can be minimized by coordinating efforts.
4. **Reduces the Git history clutter**
    - Version control systems (VCS) keep track of changes within a file.
    - When we have working directories manually being set on a user-by-user basis, each user will have to set his/her own working directory
to get the script to run.
    - This requires commenting out the current working directory set in the code,
and either replacing or uncommenting out the 'correct' working directory.
    - This will cause the VCS to note there is a change in a file where the user either needs to `commit` or `revert` for each person who is running the script.
    - While this may be a 'harmless' change, it clutters the `log` and history of the file, when bigger changes need to be reverted or bugs need to be tracked down.
    - The project template should also fix this problem since the working directory no longer needs to be set in the file.

# Changes to mindset

*Section taken from feedback from Ian*

### Git
The major change from using username `src` subfolders to analysis-based subfolders is how to navigate the initial hierarchies of the folder.
While the most technical hurdle to overcome is the potential of increased Git merge conflicts,
it can be minimized by coordinating efforts.
We have a system that distinguishes code from data, where code is stored on a Git server (e.g., GitLab) and data is stored on an encrypted LUKS volume.
This means learning and using Git will have to be part of everyone's toolkit.
It's a technical solution to solve a very complex problem, sharing and version controlling files,
but it does offer solutions for project management, if you choose to use it.

### Code structure


> The most appealing part of using usernames as folders is that it allows users to think of their code however they like, and never need to reconcile that with other people's understanding of project structure. For instance, Alice can organize folders by the work she did on a month to month basis. Bob can organize scripts into data processing/data loading/plots/misc. Chris can structure code based on who asked her to do whatever. Each person has a system that works for them and doesn't have to work for anyone else.
> But even in this small example, the three code bases are conceptually incompatible. How do you reconcile folders called 'June2017', 'get ACS stuff', and 'For Sallie'? In a project-centered folder structure, everyone needs to be on more or less the same page regarding the structure of the project and what goes on in it. Personally I think this is a good thing, and something we should be doing anyway, but it will certainly be a challenge especially if people don't think to think of it.
```
