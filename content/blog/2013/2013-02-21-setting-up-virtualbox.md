---
title: Setting up VirtualBox
author: Daniel
layout: post
permalink: /2013/02/21/setting-up-virtualbox/
date: 2013-02-21

# categories: Tutorials
tags:
  - tutorials
  - Setup
  - Tutorial
  - VirtualBox
  - Windows XP
---

Edit: March 31, 2014: As an assignment for <a href="http://software-carpentry.org/" title="Software Carpentry" target="_blank">Software Carpentry</a> I made a screencast to follow along with these steps, <a href="https://www.youtube.com/watch?v=5q_K4sIwJ0E" title="here" target="_blank">here</a>

Installing Windows XP in VirtualBox:  
<!-- more -->
Files needed:  
1. VirtualBox (VB) Intaller [here:][1]  
[ https://www.virtualbox.org/wiki/Downloads][1]

1.  CD or ISO of OS (for my CUMC/CU friends you can find the windows XP ISO [here:][2]  
    [ http://cuit.columbia.edu/cuit/software-downloads/operating-system-software/windows-xp][2]

The VB version I am using is 4.2.6

After Installing VB. You want to click "New" in the toolbar. You will be given a setup dialogue.

Name and operating System:  
Give your virtual machine (VM) a name (i.e. Windows XP). Make sure Type is "Microsoft Windows" and Version is "Windows XP" (Note: you can install other operating systems and/or different version of windows, just set those dropdown menu's accordingly).

Memory size:  
By default, VB set my WinXP VM to have 192 MB. Depending on how much RAM (memory) your computer has and programs you want to run you can increase it. For the most part you can leave it as is.

Hard drive:  
Your VM is essentially a computer, and computers need hard drives!  
click the radio button for "create a virtual hard drive now"  
another setup window will popup. Just leave the Hard drive file type as VDI (VirtualBox Disk Image). Leave the storage on physical hard drive as "dynamically allocated". This will allow the VM to take up only enough space as needed and allow it to grow/shrink as needed. The file location and size should default the same as your VM name and 10.00GB. You can leave this at its defaults unless you know you will be saving and emulating a lot of programs in your VM. We will be setting up shared folders later so you can access your regular files on your computer without having copies in your VM. You just need enough space to install your OS and whatever programs you will be running. 10GB should be more than enough.

Your new VM will show up on the left panel in VB. Select it and click the Start button in the toolbar. Your VM will load and a dialogue box will appear telling you that when your VM is active it will capture your mouse so it can be used within the VM. Dismiss the message with "OK".  
Set up Start up Disk. On my computer it defaulted to G:, just hit OK and let your VM load. You will eventually run into a message saying "FATAL: No bootable medium found! System halted." In your VM go to Devices > CD/DVD Devices > "Choose a virtual CD/DVD disk file".  
[<img class="aligncenter size-medium wp-image-121" alt="01-pickISO" src="{{ site.baseurl }}/wp-content/uploads/2013/02/01-pickISO-300x195.png" width="300" height="195" />][3]  
Navigate to and select your OS ISO file you downloaded earlier. Then go to Machine > Reset. Your VM will restart and if you are installing Windows XP, The screen will Turn Blue and will begin the Windows XP installation process.

You will eventually end up on this screen:  
[<img class="aligncenter" alt="02-setup01" src="{{ site.baseurl }}/wp-content/uploads/2013/02/02-setup01-300x194.png" width="300" height="194" />][4]

On the bottom you will see the keyboard commands to navigate through the menus. Press "ENTER" to install. Then select the first option "Format the partition using the NTFS file system <Quick>" and hit ENTER. Windows will begin installing your VM. Sit tight. get some coffee. The system will restart on its own when it is ready to setup your OS. Eventually you will end up here:  
[<img class="aligncenter" alt="03-setup02" src="{{ site.baseurl }}/wp-content/uploads/2013/02/03-setup02-300x256.png" width="300" height="256" />][5]  
Click Next, and accept the agreement, and just keep clicking next (unless you know what you are doing). Give your name, you can give your VM a name, leave your administrator password blank, set up your time, and NEXT your way through the install. More coffee!

Eventually, you will go into the initial Windows user setup pages. You don't need automatic updating, skip the internet setup, and enter your username. Click Finish and windows will load up.

First think you may have noticed is that when you resize the VM window, it does not scale nicely. To fix this and also setup folder and USB access, and other things to make your VM integrate seamlessly, you have to install Guest Additions.

If you go to Devices > CD/DVD Devices (as you did earlier) your OS .ISO should be selected. Then go to Devices > "Install Guest Additions. Click next and install the files. When a dialogue box pops up saying that the software has not passed Windows Logo testing, just click "Continue Anyway". Click FINISH and reboot your VM afterwards.

When your VM reloads, go to View > Auto-resize Guest Display is checked. Your VM will now auto-resize.

Setting up Shared folders. This will allow you to access your main OS files and folders within your VM without having to use programs such as dropbox to sync files in your VM. This also saves you a lot of space since you do not need to have duplicated files taking up HDD space. To do this, go to Devices > Shared Folders...

[<img class="aligncenter" alt="04-VMsetup" src="{{ site.baseurl }}/wp-content/uploads/2013/02/04-VMsetup-300x162.png" width="300" height="162" />][6]

Click on the folder with a + icon. Select "Other..." in the Folder Path dropdown and navigate to a folder you want access to in your VM. I suggest you at least pick your main HDD folder (C:\ in windows). When you are done Click OK and make sure "Auto-mount" and "Make Permanent" check boxes are checked in your Add Share Window. This will automatically mount these folders every time you run your VM. Add as many folders as you need, especially folders that you commonly access.

Finally under Devices menu bar, make sure "Shared Clipboard" and "Drag'n'Drop" have "Bi-directional" checked. Finally Restart the VM to apply your settings. Your shared folders will appear as network drives after you restart when you open up "My Computer". You will also be able to move files around between VM easily, and things you copy will paste in your main OS. This is useful if you are running SAS in your VM and want to paste the output into your word document in your main OS.

If you want access to a USB drive that is plugged into your computer in your VM, go to Devices > USB Devices and select your drive. It will unmount from your main OS and mount it in your VM.

Finally, if you want you can go to View > Switch to seamless mode to just have the app you are running in your VM without having the rest of your VM. Just pay attention to the dialogue box that pops up after you do this, it will tell you how to get back to your regular VM window.

[1]: https://www.virtualbox.org/wiki/Downloads
[2]: http://cuit.columbia.edu/cuit/software-downloads/operating-system-software/windows-xp
[3]: {{ site.baseurl }}/wp-content/uploads/2013/02/01-pickISO.png
[4]: {{ site.baseurl }}/wp-content/uploads/2013/02/02-setup01.png
[5]: {{ site.baseurl }}/wp-content/uploads/2013/02/03-setup02.png
[6]: {{ site.baseurl }}/wp-content/uploads/2013/02/04-VMsetup.png