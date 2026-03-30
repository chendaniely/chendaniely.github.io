---
layout: post
title:  "A Simple Model of Global Cascades on Random Networks"
date:   2016-08-31

# categories: Research

tags:
  - research
  - complexity science
  - network science
  - scientific paper
  - notes
  - paper review
---

[Duncan J Watts](https://twitter.com/duncanjwatts) wrote a paper that
was published in 2002 titled ["A simple model of global
cascades on random networks"][1] in the Proceedings of the National Academy of Sciences (PNAS).
It's a seminal paper in my current
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
[first](http://chendaniely.github.io/tutorials/2015/02/05/open-sourcing-a-python-project/)
open source project; the code can be found in two parts:

1. [The Python module](https://github.com/chendaniely/multi-agent-neural-network)
2. [The simulation code](https://github.com/chendaniely/multidisciplinary-diffusion-model-experiments)

I'm currently working on a refactoring a lot of the old code here:

1. [MANN2 Python module](https://github.com/chendaniely/mann2)
2. [MANN2 simulation code](https://github.com/chendaniely/mann2_simulations)

# The paper

<hr>

*These are my notes on the paper.  In no way shape or form am I claiming the content below as my own work, it all comes from [the paper][1]*

<hr>

*Binary decisions with externalities* is a general class of problems
that can be used to model a wide variety of real-world problems.

1.  Cascades limited by connectivity
	- Connectivity can play a role in global cascades.
	Fewer connections mean a lesser chance of information spreading within a network.
	The abstract references
		- power law
		- cluster size distribution in standard percolation theory
		- avalanches in self-organized criticality

2.  Cascades limited by local stability
	- When a network is highly connected, cascades will occur when a
	threshold number of connected nodes incorporate the information.
	Additionally, these types of networks have a bimodal distribution
	of a global cascade, either one will happen or it will not.
	- When the *threshold* of agent's to incorporate a bit of
	information is heterogeneous, the entire system has a higher
	chance of a global information cascade.
		- When the agent's threshold is heterogeneous, the ones who
		  have a lower threshold are *more* *vulnerable*.
	- Conversely, when the *degree* distribution is heterogeneous, the
	system is less likely to have a information cascade.
		- When an agent's degree centrality is heterogeneous, the ones
		  who have a higher degree will be *less* vulnerable.

The model Watts outlines has 3 unique features:

10. local dependencies
20. fractional thresholds
30. heterogeneity

Network heterogeneity and threshold heterogeneity are not equivalent.

Goals of the paper:

10. Probability of a global cascade from a single node

# Definitions

- **cascade**: event of any size triggered by an initial seed
- **global cascades**: a cascade that occupies a finite fraction of an infinite network.  A sufficiently large cascade.  More than a fixed fraction of a large, but finite network.
- **diffusion**
- **random network**
- **agents**: nodes of a network
- **neighbors**: all relevant incoming signals to an agent (usually other agents who have a directed edge to the agent in question)
- **connectivity**
- **power law distribution**
- **cluster size**
- **local stability**
- **$\phi$**: threshold
	- **$f(\phi)$**: distribution where $\phi$ is drawn from
		- unit interval and normalized such that the area under the distribution is 1
- **$n$**: number of agents in the network
- **$k$**: number of neighbors each agent is connected to
	- **$p_k$**: probability of an agent being connected to $k$ neighbors (degree distribution)
	- **$z$**: average number of neighbors $\langle k \rangle$ (coordination number)
- **$\phi_0$**: the number of agents that are seeded with 1 at the start of the simulation
	- $\phi_0 \ll 1$
	- See definition on *small seed*
- **vulnerable vertex**:  an agent that has a small threshold ($\phi \le \frac{1}{k}$) or has a degree, $k$ such that $k \le K = [\frac{1}{\phi}]$
	- $\rho_k$: probability that an agent with degree $k$ is vulnerable
		- $\rho_k = P[\phi \le \frac{1}{k}]$
- **stable vertex**: one that is not vulnerable. Stable vertices do not flip states at the start of a simulation
- **small seed**: three orders of magnitude less than the system size, $n$
- **innovator**: an agent that is seeded
- **early adopter**: a vulnerable agent
- **early and late majority**: agents who can be influenced if exposed to multiple early adopters

# Model Specification

## How the Simulation runs

10. $n$ agents in a network start off with a state of 0
20. Individual agents can only have a state that is either 0 or 1
30. Each agent has $k$ neighbors
40. An agent gets a new state of 1, if a fraction of its neighbors, $\phi$ are also 1.
	- Otherwise an agent gets a new state of 0.
50. During each time step, the population evolves:
	10. Update states in random, asynchronous order using the threshold rule
	20. Once an agent has a state of 1, it will stay at 1 for the remainder of the simulation

## How the model is parameterized

10. $\phi$ and $k$ *may* be heterogeneous
	- To simplify the simulations, the paper has a homogeneous threshold, $\phi$
		- $f(\phi) = \delta(\phi - \phi_*)$
20. The network is a uniform random graph
30. A small seed
40. Any pair of vertices is connected with probability $p = \frac{z}{n}$
	10. in uniform random graphs $p_k = \text{the Poisson distribution}$
50. $n = 10,000$
60. 100 random runs of each simulation

## Values used in figures

### Fig 1

<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC122850/figure/F1/>

Shows for a given threshold, $\phi$ and average number of neighbors, $z$,
where the cascade condition is satisfied.
This is an analytical solution, not a simulated solution

10. $\phi$: range from 0.10 to 0.25 in increments of 0.01
20. $z$: range from 0 to 15

### Fig 2

<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC122850/figure/F2/>

Looking at a specific threshold value, $\phi = 0.18$

- $n$ = 10,000
- 1,000 random realizations of the network and initial conditions

### Fig 3

<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC122850/figure/F3/>

a log-log plot of the cascade size vs cumulative distribution

### Fig 4

<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC122850/figure/F4/>




# References

<http://www.ncbi.nlm.nih.gov/pubmed/16578874>

[1]: http://www.ncbi.nlm.nih.gov/pubmed/16578874
