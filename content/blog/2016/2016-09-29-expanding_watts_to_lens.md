---
layout: post
title:  "Expanding the Watts Model"
date:   2016-09-29

# categories: Research

tags:
  - research
  - complexity science
  - network science
  - notes
  - mann
  - watts model
---

I wrote a [blog post][1] and
gave a [seminar talk][2] about the [Watts 2002 paper][3].
The next step is thinking about expanding the *binary decisions with externalities* model to a
*psychological plausible decisions with externalities* model.
This has been the goal of the [multi-agent neural-network (MANN) project][4].

<!-- more -->

# Context from the Watts model

From an information diffusion perspective,
a cascade is the spread of information from an initial set (seed) of individuals (nodes).
Watts talks about features of a network that create a *global cascade*,
which is simply a cascade of 'sufficient' size.
The ability for a node to receive and pass on a bit of information is it's *vulnerability*.

Cascades are triggered by the interaction between 2 properties --
a network property (degree centrality) and a node property (threshold).
If we look at these 2 properties as mutually exclusive from one another,
then nodes with smaller degree centrality will be less vulnerable compared to nodes with higher degree centrality,
and nodes with lower threshold values will be more vulnerable than nodes with higher threshold values.
This is because nodes with fewer connections have a smaller probability of getting information passed onto it,
and nodes with lower thresholds need fewer bits of information to propagate a signal.

Although degree centrality (*local dependencies*) and *(fractional) thresholds* are integral parts of
the binary decisions with externalities model,
another key aspect is *heterogeneity*.
For a given network, not every node will have the same degree centrality,
and not every node will have the same fractional threshold value.
As a matter of fact, any combination of high/low degree centrality and high/low fractional threshold is possible,
and each combination has an effect on a particular node's vulnerability.

| Degree (k) | Threshold ($\phi$) | Vulnerability |
|------------|--------------------|---------------|
| High       | High               | Low           |
| High       | Low                | High          |
| Low        | High               | Low           |
| Low        | Low                | High          |

# Expanding the Watts model with neural networks

The next step is to explore ways the Watts model can be expanded.
The rationale being decisions, and similarly, behaviors, are binary,
but the process of making a decision and performing an action are not.
[Mark Orr, Roxanne Thrush, and David C. Plaut][5]
suggest incorporating the [Theory of Reasoned Action (TRA)][6] as the
theoretical framework to describe how behaviors emerge and an
[auto][7]-[associator][8] [neural-network][11]
as the computational framework to simulate nodes.

A neural network allows for a multi-dimensional node, not just a simple binary node.
The key feature of an *auto associative neural network* is its ability to learn and reproduce an identity (a.k.a, prototype) given a portion of inputs.
From the Wikipedia [page][9], if we are presented the quote "I came, I saw...",
we should be able to complete the rest of the quote: "... I conquered".

If we re-conceptualize the Watts model, the prototype is the bit of information each node can pass to its neighbors (i.e., a state of 1).
Since this is a binary model, then each node can be thought to be trained to have an output of 1,
but has a state of 0 until the proper inputs are met (local dependencies and fractional thresholds), and the node has a state of 1.

From the neural network perspective, every node is trained to a particular prototype (e.g., the vector: `[1, 1, 1, 0, 0, 0]`),
and has a state of 0 (e.g., the vector: `[0, 0, 0, 0, 0, 0]`)
until proper inputs are met, the neural network will output the prototype (e.g., the vector: `[1, 1, 1, 0, 0, 0]`).
Additionally, the same output should be returned, if only a portion of the prototype vector is presented.

## Creating a neural network model analogous to the Watts model

While there are many questions and solutions on how to relate the Watts model to this newly defined neural-network model,
two immediately come to mind.

1. How do we measure if information has been passed from one node to another?
1. How do we map fractional thresholds between the two models?

Since we know the trained/learned prototype for each node,
one way to know if information passed from the seed node (and subsequent nodes) to a new node is to look at how 'similar'
the output of the new node is to the prototype.
Similarity can be measured in many ways, one such way is to use [cosine similarity][10].
Once the similarity is calculated, we can apply another threshold, $\theta$,
that signals the propagation of information.
This new threshold can be used to calculate a binary state, $S_1$ that is analogous to the Watts model state, $S_0$.
We can use $\theta$ to calculate how many nodes are different from the node of interest
(this can also be thought of as some function of $S_1$),
and use the same threshold, $\phi$, from the Watts model to determine whether the node of interest will propagate our signal in the network.

However, since our definition of 'similarity' and 'information propagation' relies on the *output* of our neural network,
we need to give the neural network a set of *inputs*.
This leads to anther question:

1. How do we provide inputs to nodes that have been designated to carry and propagate information in the network?

We can do this a few ways.
For each node that will propagate information we can assign the input as

1. the prototype (e.g., the vector: `[1, 1, 1, 0, 0, 0]`)
2. the state (a.k.a output) of 1 of the 'different' connected nodes
3. the average state of all of the 'different' connected nodes
4. the average state of all connected nodes
5. present each 'different' node in a random order and have the neural network cycle though them
6. present all connected nodes in a random order and have the neural network cycle though them

Other than the first option of using the prototype,
the other methods will still preserve the differences in degree centrality between the nodes.
For example, if a node only has one neighbor and it will be updated with 1 neighbor,
it will always be presented with the same inputs.
However if a node has multiple neighbors, the probability of the same neighbor picked every time is proportional to the number neighbors.


## Creating a simpler neural-network model

A simpler approach would be to have each node in the network trained against the prototype.
Seed a single node with the prototype, and run the model without any additional thresholding rule ($\theta$),
and have each node use a random 1 neighbor's state (i.e., output) and its input.


[1]: http://chendaniely.github.io/research/2016/08/31/a_simple_model_of_global_cascades_on_random_networks/
[2]: www.google.com
[3]: https://www.ncbi.nlm.nih.gov/pubmed/16578874
[4]: https://github.com/chendaniely/mann2
[5]: http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0062490
[6]: https://en.wikipedia.org/wiki/Theory_of_reasoned_action
[7]: https://en.wikipedia.org/wiki/Autoassociative_memory
[8]: http://www.sciencedirect.com/science/article/pii/009813549280051A
[9]: https://en.wikipedia.org/wiki/Autoassociative_memory
[10]: https://en.wikipedia.org/wiki/Cosine_similarity
[11]: https://en.wikipedia.org/wiki/Artificial_neural_network