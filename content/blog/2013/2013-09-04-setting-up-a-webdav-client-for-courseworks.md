---
title: Setting up a WebDAV Client for Courseworks
author: Daniel
layout: post
permalink: /2013/09/04/setting-up-a-webdav-client-for-courseworks/
date: 2013-09-04

# categories: Tutorials
tags:
  - tutorials
  - Client
  - Linux
  - Mac
  - Setup
  - WebDAV
  - Windows
---
Columbia University's Courseworks website allows you to download files for a registered class.  A problem arises when multiple files needed to be downloaded simultaneously.  One simply cannot just select the files and bulk download them.  Courseworks have instructions to circumvent this limitation in the web interface by implementing a [WebDAV][1] client.  However, other than Cyberduck under their Mac instructions, the Windows suggestion is quite limited.

In this post I discuss setting up a WebDAV Client for Windows and Mac.  If you are on Linux, I've only used [AnyClient][2], which is Java based but is not as comprehensive as the Windows/Mac alternatives suggested in this post (and this is the one suggested by Courseworks).  If anyone knows of a good Linux WebDAV client, let me know!

This post shows how to setup [BitKinex ][3]and [Cyberduck ][4]in Windows.  You can also use the Cyberduck instructions for Mac.

<!-- more -->

Courseworks also has instructions on setting up Cyberduck under their Mac section; the same instructions can also be used for the Windows version of Cyberduck.

*Be careful when accessing a directory that you do not own.  There is the potential that you may be able to upload files to the directory, or worse, change, overwrite, or delete the files.*

**Step 1:  Accessing your Courseworks files and resources links.**

What you have to do first is log into your Coureworks, click on the course number for your class and then in the left frame of the page click "Files & Resources".  On the top of the page you will see a link for "upload-download multiple resources", see figure 1.1

<p style="text-align: center;">
  <a href="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav01.png"><img alt="webdav01" src="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav01-300x52.png" width="300" height="52" /></a>
</p>

<p style="text-align: center;">
  Figure 1.1: Upload-Download Multiple Resources Link
</p>

It will direct you do a link to copy in "step 1" and directions to set up WebDAV in "step 2".  In "step 2" you will find the instructions for setting up Cyberduck for Mac, which is the same for windows (like I mentioned above).

The link that you need essentially has 2 parts, the part that is highlighted in Figure 1.2 is what you will need when you are using BitKinex, the entire link is needed for Cyberduck,

<p style="text-align: center;">
  <a href="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav02.png"><img alt="webdav02" src="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav02-300x35.png" width="300" height="35" /></a>
</p>

<p style="text-align: center;">
  Figure 1.2: components of your WebDAV directory
</p>

**Step 2a Windows:**

For Windows I use Bitkinex.  You can also use Cyberduck (which I describe in the Mac section below).

You can download BitKinex [here][3].  At the time of this post Current Version: **3.2.3 **Release Date: **07/11/2010**. Do not worry about the 'older' release date.

After you have BitKinex installed, you will right click "Http/WebDAV" and go to New > Http/WebDav, See figure 2.1 (sorry my mouse is highlighted over the wrong option).

[<img class="aligncenter" alt="webdav03" src="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav03-300x272.png" width="300" height="272" />][5]

<p style="text-align: center;">
  Figure 2.1:  Creating a new WebDAV connection in BitKinex
</p>

A popup window will appear for a name, you can simply put "Columbia" or "newcourseworks.columbia.edu" or "courseworks.columbia.edu".

Next, it should direct you to a settings menu under the "Server" option on the left, See Figure 2.2.  for server address enter "courseworks.columbia.edu", I used "newcourseworks.columbia.edu", but I believe the two should be the same, and the former may be preferred.  You can also refer to Step 1 and copy the text I showed that was not highlighted in blue (Figure 1.2).  Under Authentication, enter your UNI for "User" and password for "Password"

[<img class="aligncenter" alt="webdav04" src="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav04-300x191.png" width="300" height="191" />][6]

<p style="text-align: center;">
  Figure 2.2: WebDAV Setup
</p>

<p style="text-align: left;">
  Now go back to the Step 1, and Figure 1.2, and select the part of the link that I have selected in blue.  It should start with a "/dav/...".  On the left hand panel under "Server" there should be a section called "Site Map".  Paste the text you just copied into the textfild and select "Directory (WebDAV complient)" and click Add.  Repeat this process for all your courses.  See figure 2.3 for more details.
</p>

<p style="text-align: center;">
  <a href="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav05.png"><img alt="webdav05" src="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav05-300x191.png" width="300" height="191" /></a>
</p>

<p style="text-align: center;">
  Figure 2.3: Course Folder Directory Setup
</p>

<p style="text-align: left;">
  Here is what BitKinex looks like after you double click on "newcourseworks.columbia.edu" under the "Http/WebDAV" section of the initial main application screen (See figure 2.4).  The application has 3 main panels.  The one on the far left shows a directory tree to everything you input shown in Figure 2.3.  The middle shows the file contents as you navigate the folders,  you can double click the folder with two dots ".." to move up to the parent folder (the folder you just came from).  The right panel shows contents on your computer.  There is a small area with green and blue buttons that may/may not be greyed out.  These let you move files to your computer or upload to the server.  You can hover over them for more details.
</p>

<p style="text-align: center;">
  <a href="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav06.png"><img alt="webdav06" src="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav06-300x168.png" width="300" height="168" /></a>
</p>

<p style="text-align: center;">
  Figure 2.4: Using BitKinex
</p>

<p style="text-align: left;">
  Now you should be able to go to your course's files and select everything (or everything you need) and just click the green button, and it will automatically download everything over.  Just take note that sometimes professors have very long names for their PDF's and depending where on your computer you are downloading the file to, it may not save.  Most of the time it is because the entire file path and name is over 256 characters.  What you have to do then is just navigate to your desktop on the right panel, download the file there, and then rename it before moving it to the directory of your choice.
</p>

<p style="text-align: left;">
  On the top of the window you can also set folder favorites, so you can easily navigate, to say, your "Columbia" folder quicker.
</p>

**Step 2b Mac:**

Cyberduck can be found [here][4].  I am using the Windows version of Cyberduck, the Mac should look almost the same.

Courseworks have the following instructions on their site:

1.  Click the **Open Connection** button.
2.  In the *Server* dialog box, type (or copy and paste) the path as shown above.
3.  Type in your Sakai username and password and click **OK**.

You will now see a window on your Mac screen that represents the resources that are in your site. Simply drag and drop between this window and other Finder windows on your Mac to transfer files to and from your Sakai site's resources folder.

I will be showing a different method, all have the same results.

On the bottom left of the application, click on the "+" sign (Figure 3.1)

<p style="text-align: center;">
  <a href="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav07.png"><img alt="webdav07" src="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav07.png" width="122" height="83" /></a>
</p>

<p style="text-align: center;">
  Figure 3.1: Adding a bookmark
</p>

<p style="text-align: left;">
  Next, choose "WebDAV(HTTP/SSL)" from the drop down menu, then give your course a name in "Nickname" and you can paste everything from the Courseworks link under "Server".  Not everything will paste, but click the little arrow on the bottom left and the menu will expand and the remaining of the pasted text will be shown under "Path",  if not you can manually paste the non-highlighted text I showed in Figure 1.2 to "Server", and the highlighted text to "Path".  Your results should look similar to figure 3.2 below.
</p>

<p style="text-align: center;">
  <a href="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav08.png"><img class="aligncenter" alt="webdav08" src="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav08-251x300.png" width="251" height="300" /></a>
</p>

<p style="text-align: center;">
  Figure 3.2: Setting up Cyberduck Connections
</p>

<p style="text-align: left;">
  Finally, just close that window and you should see your class listed in the Bookmarks section, figure 3.3.  You can now double click the "drive" and it will open up the Courseworks files and you can click and drag to your folders on your computer.
</p>

<p style="text-align: center;">
  <a href="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav061.png"><img class="aligncenter size-medium wp-image-148" alt="webdav061" src="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav061-300x185.png" width="300" height="185" /></a>
</p>

<p style="text-align: center;">
  Figure 3.3: Bookmarks View<a href="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav08.png"><br /> </a> <a href="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav07.png"><br /> </a> <a href="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav06.png"><br /> </a> <a href="{{ site.baseurl }}/wp-content/uploads/2013/09/webdav02.png"><br /> </a>
</p>

[1]: http://en.wikipedia.org/wiki/WebDAV
[2]: http://www.jscape.com/products/file-transfer-clients/anyclient/
[3]: http://www.bitkinex.com/download
[4]: http://cyberduck.ch/
[5]: {{ site.baseurl }}/wp-content/uploads/2013/09/webdav03.png
[6]: {{ site.baseurl }}/wp-content/uploads/2013/09/webdav04.png