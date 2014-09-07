---
title: Installing Eclipse in Ubuntu 13.10
author: Daniel
layout: post
permalink: /2014/02/04/installing-eclipse-in-ubuntu-13-10/
categories:
  - Tutorials
tags:
  - Eclipse
  - Install
  - Linux
  - Setup
---
Adapted from Shubhmay and TimD from: <a href="http://askubuntu.com/questions/26632/how-to-install-eclipse" title="http://askubuntu.com/questions/26632/how-to-install-eclipse" target="_blank">http://askubuntu.com/questions/26632/how-to-install-eclipse</a>

1.  Extract the eclipse.XX.YY.tar.gz file <pre class="brush: bash; title: ; notranslate" title="">tar -zxvf eclipse.XX.YY.tar.gz
</pre></p> 

2.  Copy the extracted folder to /opt
    
    <pre class="brush: bash; title: ; notranslate" title="">sudo cp -r eclipse /opt
</pre></p> 

3a. Create a desktop file and install it:

<pre class="brush: bash; title: ; notranslate" title="">gedit eclipse.desktop
</pre>

3b.  
and copy the following to the eclipse.desktop file.

<pre class="brush: bash; title: ; notranslate" title="">[Desktop Entry]
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
</pre>

3c. then execute the following command to automatically install it in the unity:

<pre class="brush: bash; title: ; notranslate" title="">sudo desktop-file-install eclipse.desktop
</pre>

1.  Create a symlink in /usr/local/bin using
    
    <pre class="brush: bash; title: ; notranslate" title="">cd /usr/local/bin
ln -s /opt/eclipse/eclipse
</pre>
    
    according to user ortang: Use the eclipse version when creating a the symlink (eg: ln -s /opt/eclipse/eclipse /usr/local/bin/eclipse42), and use Exec=eclipse42 at the desktop entry. That way you will be able to install multiple different versions of eclipse

2.  For eclipse icon to be displayed in dash, eclipse icon can be added as
    
    <pre class="brush: bash; title: ; notranslate" title="">cp /opt/eclipse/icon.xpm /usr/share/pixmaps/eclipse.xpm
</pre></p>