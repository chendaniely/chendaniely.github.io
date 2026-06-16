---
layout: post
title:  "From VMs to LXC Containers to Docker Containers"
date:   2017-07-07

#categories: SDAL

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

Since I've joined [SDAL][1],
the lab has undergone a few infrastructure related changes,
mainly how applications are run on the servers.
From what I remember, we started using [Virtual Box][2] virtual machines,
then moved to [LXC][3] Linux containers, and we are now rebuilding our entire infrastructure
using [Docker][4] containers.

<!-- more -->

# How we got here

The whole point of using these visualization and container technologies is so
we did not want to install anything directly on the server.
There are many benefits to this

1.  If the server goes down, we should be able to redeploy our infrastructure on a backup server
2.  If an installation goes wrong, it will not crash the underlying server
    - If an installation goes wrong, we should be able to swap out or roll back to a working state
3.  This gives us the ability to test out updates before rolling them out on a production server
4.  If something happens with one part of the system, it should not affect another

## Virtual Box Virtual Machines

We ([Aaron][5]) started with Virtual Box Virtual Machines,
because it's a very logical first step.
If you wanted the same thing on your own computer/laptop,
you'd use a virtual machine.
This meant that it was relatively easy to get started because
we already had experience with VB.

Our main reasons for looking into other solutions were

1. **performance**: since we are using these VMs to run data analytics,
  we needed performant system.
  The fact we needed to install an entire OS made it clunky
2. **size**: Since we wanted multiple containers, one for each application,
  the fact that an entire OS needed to be installed for each application
  meant that a lot of OS information was replicated and
  used a large amount of space
3. `VBoxManage`: since we had to run our VMs in `headless` mode,
  the only way to make changes to the VMs was with the VB command line tool,
  `VBoxManage`, which is less than ideal in terms of simplicity and
  documentation.

## LXC Containers

When looking to move away from VirtualBox,
we started with LXC because at the time Docker just started and
didn't seem to be developed enough.
During the early days of Docker,
the documentation was lacking (one might argue that it still is),
and the API/interface was cumbersome
(How do I get into my container? why can't I just SSH?).
We went with LXC since docker was an extension of it.
We later also looked into LXD,
since it extended LXC with more and better security, group, and
permission features.

LXC got us pretty far,
we had a lighter set of applications running on the servers,
since each container was based on the host operating system
(in our case this was CenOS 7).



The main issue was that it was hard to quickly tear down and redeploy containers.
Or have container dependencies to build applications.

1. **support**: support for LXC was lacking, mainly a lack of documentation
2. **permissions**: permissions from the host were not being carried over into the container
3. **host os**: each container was limited to whatever the host OS was on.

These limitations had us looking at LXD, LXC successor.
LXD did not run as root, so each container was not privileged.
It also mapped permissions from the host OS,
and we had the ability to install an image using Ubuntu, if needed.

However, after a year we transitioned into Docker, and solved the LXC limitations.

## Docker Containers

I'm sure a lot of the issues from LXC could've been worked out with enough blood, sweat, and tears, it is linux after all.
The popularity of Docker over the year was hard to ignore and worth trying again.

The best part about docker is how it forces you to fully document the setup process,
using the `Dockerfile`.
This not only meant that we can readily tear down and spin up the container if
something goes wrong.
Additionally, we can just as easily start up multiple containers running the same application.
This is particularly useful when trying to get RStudio to see newly mounted and mapped drives
or permission changes.
Instead of restarting the image, which requires nobody to be using it,
we can spin up a new container and have the people who needed new data partitions or
permission to have a temporary new container without disrupting other users.

# What's next?

We'll probably look into container orchestration tools such as docker-swarm or kubernetes.
While we could use the current `docker-compose` file and function to create multiple RStudio Servers,
there's a lot of copying and pasting involved.

We'd like everyone to have his/her own RStudio instance, so if there is a permission change,
we can simply restart the individual user's container instance, rather than finding workarounds in the middle of the day because we can't do a restart.
Relying on zero usage on a server (especially in the middle of a work day) to do maintenance is almost never a good idea.
Having a orchestrator will allow us to spin up as many instances without conflicting ports and username-appended container names with a single script.

It would also be nice to have a single entry page, so users can pick the service they need,
rather than remembering port numbers to connect to (since those can change at any given time).

Finally, on a recent server hiccup, we were having issues around dead containers.

Here's the error message when we tried to stop and remove the containers:

```
$ docker-compose down
Stopping adminer ... done
Stopping mro ... done
Stopping postgresql ... done
Stopping dokuwiki ... done
Stopping rpkgs ... done
Stopping rstudio ... done
Stopping shiny ... done
Removing adminer ... error
Removing mro ... error
Removing postgresql ... error
Removing dokuwiki ... error
Removing rpkgs ... error
Removing rstudio ... error
Removing shiny ... error

ERROR: for postgresql  driver "overlay" failed to remove root filesystem for b91b18c144d40801b1782789ffe3a9352509b720b368947cefd9e443d02edf01: remove /home/vms/docker/overlay/014f942314a693d1984155ded44a30f50b27b67fce62f7ed60233028f998379c/merged: device or resource busy

ERROR: for dokuwiki  driver "overlay" failed to remove root filesystem for f228cc35d050d8654cc1eb4e424feb111a2b826b3a4bd35d42aa4ff38dcc5524: remove /home/vms/docker/overlay/6dc15c5116a0290bc42bdae7fafdcbdcf718951c8ebcbfbc63eb56d18fd07c23/merged: device or resource busy

ERROR: for adminer  driver "overlay" failed to remove root filesystem for fb7f33ed5a10a843b9855ffa3aa83c0b68ecfeb793a89274e0277add2bc08262: remove /home/vms/docker/overlay/58c311625ca5d6288359489d36c4653107fd710e3700298cf8400cf85d4c4523/merged: device or resource busy

ERROR: for rpkgs  driver "overlay" failed to remove root filesystem for 14c0516130623640ebace03e89478b17efb2e802232ddc22a524f42e4fcaef02: remove /home/vms/docker/overlay/d083c1fb3046605fe3a9eaa8e19111b00473c38bebe23f222bfd0cfa81802c6f/merged: device or resource busy

ERROR: for mro  driver "overlay" failed to remove root filesystem for 7c75a0cc6ba4f80bdb47df37d0aeab38681e621a5052507a5cc8da2a4eac332c: remove /home/vms/docker/overlay/cd7e50fe0e95feca8ced590c0ecd373290fa6710656db75286c1ce8900ff09d1/merged: device or resource busy

ERROR: for rstudio  driver "overlay" failed to remove root filesystem for 8f90d16c8da45c59519203e582917b24a4249fdfa9a35f5043782320d6d6b2d4: remove /home/vms/docker/overlay/408a938c07d53d5b4cf79376a15f1bf3ffc5cc54eb0c1d2f7f95215764e010b5/merged: device or resource busy

ERROR: for shiny  driver "overlay" failed to remove root filesystem for dc85077a54862940c0a17906b66d7670d1dbb95f5006083871c36c20586483f3: remove /home/vms/docker/overlay/08e22f468c2f5aa0ca4823a2aa5d9cb400167c49aa21a06f3538a9fa943c4dba/merged: device or resource busy
Removing network dockerimages_default
Removing network dockerimages_dspg
```

We got around this error by restart the server, which is far from an ideal solution,

There was a promising explanation [here][6] and [here][7].
Here's an excerpt from Anusha Ragunathan's post about what's going on 

```
Dug up some history:

daemon flags changed to default "shared" mount propagation in 2aee081 in an effort to help volume mounts to ensure shared. This change made it to 1.12, which is probably why there's more reports since then.

Prior to this, the flags were indeed set to "slave" in eb76cb2 to avoid EBUSY errors on container remove. There's a blog post on why this was done. Although it mentions devicemapper, the problem exists across graphdrivers. http://blog.hashbangbash.com/2014/11/docker-devicemapper-fix-for-device-or-resource-busy-ebusy/
```

```
Overview:
While this is issue not exclusive to devicemapper, the mechanics currently involved in this driver cause it to be affected by this.

A couple of the more commons issues seen when using the ‘devicemapper’ storage driver is when trying to stop and/or remove a contianer.
In the docker daemon logs, you may see output like:

[error] deviceset.go:792 Warning: error waiting for device ac05cffda663a01cbc37879bc146fcd68d0f95b5b141f60da2b64579add1f4ef to close: Timeout while waiting for device ac05cffda663a01cbc37879bc146fcd68d0f95b5b141f60da2b64579add1f4ef to close

or more likely:

Cannot destroy container ac05cffda663: Driver devicemapper failed to remove root filesystem ac05cffda663a01cbc37879bc146fcd68d0f95b5b141f60da2b64579add1f4ef: Device is Busy
[8ad069f7] -job rm(ac05cffda663) = ERR (1)
[error] server.go:1207 Handler for DELETE /containers/{name:.*} returned error: Cannot destroy container ac05cffda663: Driver devicemapper failed to remove root filesystem ac05cffda663a01cbc37879bc146fcd68d0f95b5b141f60da2b64579add1f4ef: Device is Busy
[error] server.go:110 HTTP Error: statusCode=500 Cannot destroy container ac05cffda663: Driver devicemapper failed to remove root filesystem ac05cffda663a01cbc37879bc146fcd68d0f95b5b141f60da2b64579add1f4ef: Device is Busy

Diagnosis:
What’s happening behind the scenes is that devicemapper has established a new thin snapshot device to mount then container on.
Sometime during the life of that container another PID on the host, unrelated to docker, has likely started and unshared some namespaces from the root namespace, namely the mount namespace (CLONE_NEWNS). In the mounts referenced in this unshared host PID, it includes the thin snapshot device and its mount for the container runtime.

When the container goes to stop and unmount, while it may unmount the device from the root namespace, that umount does not propogate to the unshared host PID.
When the container is removed, devicemapper attempts to remove the thin snapshot device, but since the unshared host PID includes a reference to the device in its mountinfo, the kernel sees the device as still busy (EBUSY). Despite the fact the mounts of the root mount namespace may no longer show this device and mount.
```

Maybe these problems can be fixed with a different container orchestration system like docker swarm
or kubernetes, who knows.

[1]: https://www.bi.vt.edu/sdal
[2]: https://www.virtualbox.org/
[3]: https://linuxcontainers.org/
[4]: https://www.docker.com/
[5]: https://www.bi.vt.edu/sdal/people/Aaron-Schroeder
[6]: https://github.com/moby/moby/issues/25718#issuecomment-250356570
[7]: http://blog.hashbangbash.com/2014/11/docker-devicemapper-fix-for-device-or-resource-busy-ebusy/