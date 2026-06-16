---
title: Absolute and Relative Directories in Python
author: Daniel
layout: post
#permalink: /2014/05/16/absolute-and-relative-directories-in-python/
date: 2014-05-16

# categories: Tips
tags:
  - tutorial
  - tips
  - python
---
One of the most common tasks (for me at least) is saving or getting data from another directory from where the current python script is running. However, for many of the file I/O functions, it assumes the current directory or you need to give it an absolute directory. Using something like `../other_directory` will not work.

<!-- more -->

Here is one way you can get the current script directory, and then append to the string the relative paths.

Adapted from user Al Cramer: http://stackoverflow.com/questions/4934806/python-how-to-find-scripts-directory

In this example I have a pandas dataframe I want to save to another folder

```python
abs_dir = os.path.dirname(__file__)
print abs_dir

rel_dir = os.path.join(abs_dir, '../data')
print rel_dir

data = ''.join([rel_dir, '/nhtsa.csv'])
print data

df.to_csv(data, sep=',', encoding='utf-8')
```
