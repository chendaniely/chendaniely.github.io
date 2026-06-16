---
title: Installing Eclipse in Ubuntu 13.10
author: Daniel
layout: post
# permalink: /2014/02/04/installing-eclipse-in-ubuntu-13-10/
date: 2014-02-04

# categories: Tutorials
tags:
  - tutorials
  - Eclipse
  - Install
  - Linux
  - Setup
---


Adapted answer from Shubhmay and TimD on [askubuntu](http://askubuntu.com/questions/26632/how-to-install-eclipse) on installing Eclipse.

<!-- more -->

1.  Extract the eclipse.XX.YY.tar.gz file: `tar -zxvf eclipse.XX.YY.tar.gz`

2.  Copy the extracted folder to `/opt`: `sudo cp -r eclipse /opt`

3. Create a desktop file `gedit eclipse.desktop`

4. copy the following to the eclipse.desktop file

    
        [Desktop Entry]
        Name=Eclipse 
        Type=Application
        #Exec=eclipse
        Exec=env UBUNTU_MENUPROXY=0 eclipse # for menubar bug in 13.10
        Terminal=false
        Icon=eclipse
        Comment=Integrated Development Environment
        NoDisplay=false
        Categories=Development;IDE;
        Name[en]=Eclipse
    

5. Execute the following command to automatically install it in the unity: `sudo desktop-file-install eclipse.desktop`

6.  Create a symlink in `/usr/local/bin` using

        cd /usr/local/bin
        ln -s /opt/eclipse/eclipse

    
    according to user ortang:

    > Use the eclipse version when creating a the symlink
    > (eg: `ln -s /opt/eclipse/eclipse /usr/local/bin/eclipse42`),
    > and use `Exec=eclipse42` at the desktop entry.
    > That way you will be able to install multiple different versions of eclipse

2.  For eclipse icon to be displayed in dash, eclipse icon can be added with
    
    `cp /opt/eclipse/icon.xpm /usr/share/pixmaps/eclipse.xpm`