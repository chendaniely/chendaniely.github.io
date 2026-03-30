---
title: Setting Up Repast Simphony 2.1 in Linux
author: Daniel
layout: post
# permalink: /2014/02/04/setting-up-repast-simphony-2-1-in-linux/
date: 2014-02-04

# categories: Tutorials
tags:
  - tutorials
  - Linux
  - Repast Simphony
  - Setup
---

[Repast Simphony](http://repast.sourceforge.net/) is a Java based collection of agent-based modeling and simulation software.

<!-- more -->

Repast Simphony 2.1 installs its library files into `~/.eclipse/ECLIPSEVERSION/plugins/` and `features/`

when you create the model it looks for these files in `/opt/eclipse/plugins/` and `/features`

This issue has been brought up and added to the issue tracker as of 2013-09-30

User mijael posted a solution to the Repast Interest Mailing list about creating symlinks to the /opt directory:

```
cd .eclipse/org.eclipse.platform_4.3.0_1473617060_linux_gtk_x86_64/plugins/
ls | xargs -I targ sudo ln -s ~/.eclipse/org.eclipse.platform_4.3.0_1473617060_linux_gtk_x86_64/plugins/targ /opt/eclipse/plugins/targ
```

repeat the same for the features directory:

```
cd .eclipse/org.eclipse.platform_4.3.0_1473617060_linux_gtk_x86_64/features/
ls | xargs -I targ sudo ln -s ~/.eclipse/org.eclipse.platform_4.3.0_1473617060_linux_gtk_x86_64/features/targ /opt/eclipse/features/targ
```