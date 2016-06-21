---
layout: post
title:  "A Simple Model of Global Cascades on Random Networks"
date:   2016-03-14

categories: Research

tags:
  - complexity science
  - network science
  - scientific paper
  - notes
  - paper review
---

[Duncan J Watts](https://twitter.com/duncanjwatts) wrote a paper that
was published in 2002 in PNAS titled ["A simple model of global
cascades on random networks"][1].  It's a seminal paper in my current
work on information diffusion in (social) networks.  Watts shows how
the interactions between local dependencies, fractional threshold, and
heterogeneity relate to information cascades in networks.  My work
builds on these ideas, so it's important to have a strong
understanding of the terms and model specifications outlined in the
paper.

<!-- more -->

I've been working with my Masters and Doctoral advisor,
[Mark Orr](http://mark-orr.github.io/) on a simulation platform that
incorporates artificial neural networks within an agent-based
simulation.  The project is called "Multi-Agent Neural Network" (MANN)
and it was my
[first](http://chendaniely.github.io/blog/2015/02/05/open-sourcing-a-python-project)
open source project; the code can be found in two parts:

1. [The Python module](https://github.com/chendaniely/multi-agent-neural-network)
2. [The simulation code](https://github.com/chendaniely/multidisciplinary-diffusion-model-experiments)

I'm currently working on a refactoring a lot of the old code here:

1. [MANN2 Python module](https://github.com/chendaniely/mann2)
2. [MANN2 simulation code](https://github.com/chendaniely/mann2_simulations)

# The paper

1.  Cascades limited by connectivity
	- Connectivity can play a role in global cascades.
	Fewer connections mean a lesser chance of information spreading within a network.
	The abstract references
		- power law
		- cluster size distribution in standard percolation theory
		- avalanches in self-organized criticality

2.  Cascades limited by local stability
	-

# Definitions

- cascades
- diffusion
- random network
- agents
- neighbors
- global cascades: a large cascade
- connectivity
- power law distribution
- cluster size
- local stability

# Model Specification

[1]: http://www.ncbi.nlm.nih.gov/pubmed/16578874
