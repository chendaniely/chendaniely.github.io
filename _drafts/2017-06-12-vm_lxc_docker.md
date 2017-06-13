---
layout: post
title:  "From VMs to LXC Containers to Docker Containers"
date:   2017-06-12

categories: SDAL

tags:
  - infrastructure
  - dspg
  - dspg17
  - containers
  - sdal
  - docker
  - vms
  - lxc
  - devops
---

Since I've joined [SDAL][1], the lab has undergone a few infrastructure related changes,
mainly how applications are run on the servers.
From what I remember, we started using [Virtual Box][2] virtual machines,
then moved to [LXC][3] Linux containers, and we are now rebuilding our entire infrastructure
using [Docker][4] containers.

<!-- more -->

# How we got here

This just goes to show how fast technology can progress.
[Aaron][5], from my lab, originally used the VirtualBox VMs,
since it is a logical start.
The whole point of using these visualization and container technologies is so 
we did not want to install anything directly on the server.
There are many benefits to this

1. If the server goes down, we should be able to redeploy our infrastructure on a backup server
2. If an installation goes wrong, it will not crash the underlying server
    - If an installation goes wrong, we should be able to swap out or roll back to a working state
3. This gives us the ability to test out updates before rolling them out on a production server
4. If something happens with one part of the system, it should not affect another

## Virtual Box Virtual Machines

We started with Virtual Box Virtual Machines, because it's a very logical first step.
If you wanted the same thing on your own computer/laptop,
you'd use a virtual machine.

## LXC Containers

We started with LXC because at the time Docker just started.
During the early days of Docker, the documentation was lacking (one might argue that it still is),
and the API/interface was cumbersome (How do I get into my container? why can't I just SSH?).
We went with LXC since docker was an extension of it.

LXC got us pretty far, we had a lighter set of applications running on the servers.
The main issue was that it was hard to quickly tear down and redeploy containers.
Or have container dependencies to build applications.
We solved these issues with Docker.

## Docker Containers

I'm sure a lot of the issues from LXC could've been worked out with enough blood, sweat, and tears (it is Linux after all),
but the popularity of Docker over the year was hard to ignore and worth trying again.

The best part about docker is how it forces you to fully document the setup process (using the `Dockerfile`).



# What's next?

We'll probably look into container orchestration tools such as docker-swarm or kuberneties.
While we could use the current `docker-compose` file and function to create multiple RStudio Servers,
there's a lot of copying and pasting involved.

We'd like everyone to have his/her own RStudio instance, so if there is a permission change,
we can simply restart the individual user's container instance, rather than finding workarounds in the middle of the day because we can't do a restart.
Relying on zero usage on a server (especially in the middle of a work day) to do maintenance is almost never a good idea.
Having a orchestrator will allow us to spin up as many instances without conflicting ports and username-appended container names with a single script.

It would also be nice to have a single entry page, so users can pick the service they need,
rather than remembering port numbers to connect to (since those can change at any given time).


[1]: https://www.bi.vt.edu/sdal
[2]: https://www.virtualbox.org/
[3]: https://linuxcontainers.org/
[4]: https://www.docker.com/
[5]: https://www.bi.vt.edu/sdal/people/Aaron-Schroeder
