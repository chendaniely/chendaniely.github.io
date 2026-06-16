---
layout: post
title:  "A 'Simple' Neural-Network Model"
date:   2017-03-30 00:10:00

# categories: Research

tags:
  - research
  - complexity science
  - network science
  - notes
  - mann
  - watts model
---

My previous [blog post][1] summarized the main points of the [Watts 2002 paper][2].
At the very end of the post I mentioned ways we can extend the Watts model with neural-networks.
Here I outline the steps of the neural-network simulation.

<!-- more -->

Generally the model goes though an initiation step, a simulation step, and a cleanup step.
In the initiation step, the agents are created and connected in a network.
Then selected agents are seeded with a value before continuing onto the simulation step.
In the simulation step, 'steps' for each time tick are performed.
This includes picking agents to be updated, making the necessary calculations for an update,
and updating agents in a simultaneous or sequential manner.
Agent states in teach time tick is saved to be written to a (CSV) file.
The cleanup step is mainly there when programming the model.
It saves any unwritten states to the file, and
any other related tasks of that nature.

# MANN

The neural networks used in MANN use the ["the light, efficient network simulator" (LENS)][3].
I created a (inefficient) python wrapper around LENS, [pylens][4].
This mainly stems from the fact my advisor used LENS for his work in the past,
and interface with it via the command line with input files.
The inefficient stems from the fact that I am having python write our the necessary input files for the neural network,
and making command-line `subprocess` calls to LENS.

## Initiation

$n$ agents are created for the model.
When an agent is created, a feed-forward neural network with randomized weights to represent its state.
A prototype that will be used to train the neural network is assigned to the agent.

The agent's will all be connected to a network.
For example in the `networkx` list of graph generators,
the [`fast_gnp_random_graph`][5] takes the number of agents, $n$,
and a probability, $p$, of an edge being created.

To train the neural network, it needs a set of example files to train.
The example file consists of $k$ (50) examples.
Each example is a randomized form of the prototype.
The amount of randomization is determined by parameter $\delta$.
To incorporate heterogeneity in the model,
we also mutate the prototype that is used to create the example files.
This mutation rate is designated as $\epsilon$.

How well the agent gets trained is parameterized with the *criterion* variable.
It is analogous to the amount of error the neural network can make before it finishes training.
That is, the smaller the criterion, the smaller the error, the more accurate it can represent the training set.
All agents stop training after 1000 epochs (training cycles for the neural network).

Once the neural network is trained, its weights are output to a file to be loaded during the simulation step.

All agents begin with a state of 0.
That is the first layer of the neural network all have values of 0.
We then select agents to be seeded.
The seeded agent is presented (via an example file) the non-$\epsilon$-mutated prototype.
We cycle this value through the neural network with one epoch,
and the output of the neural network is assigned to the agent's state.

We then begin the simulation part of the model.

## Simulation

The simulation runs in *steps*.
These steps designate the amount of *time ticks* the simulation runs for.
The same process occurs during each time tick until the simulation ends.

All agents will be randomly selected (without replacement) to undergo an update process.
The update process looks at all the agent's neighbors with a directed edge coming *into* the selected agent
(i.e., neighbors or predecessors),
and randomly selects one of the agents to be the *influencer*.

The influencer writes our its current state as an example file.
This example file is used by the agent's neural network and the output is assigned as the agent's new state.

In a sequential update process,
the agent's new state is assigned as described above.
However, during simultaneous updating,
the new state will be stored into a temporary state value,
so that if the agent is used as an influencer to another agent,
the original agent state value will be written out to the example file.
In simultaneous updating, only after all agents have undergone the update process will they
assign the temporary state as their new state.

The agent states are saved to a file at the end of the initiation step and the
end of each simulation time tick.

[1]: http://chendaniely.github.io/research/2016/09/29/expanding_watts_to_lens/
[2]: https://www.ncbi.nlm.nih.gov/pubmed/16578874
[3]: http://web.stanford.edu/group/mbc/LENSManual/
[4]: https://github.com/chendaniely/pylens
