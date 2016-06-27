---
layout: post
title:  "Example Jupyter Notebook to markdown"
date:   2016-06-24

categories: Tutorials

tags:
  - python
  - jupyter notebook
  - jekyll
  - blogging
---
This is an example of using converting a `jupyter notebooks` into a blog post using `jupyter nbconvert --to markdown`

<!-- more -->

The way to make this work is to put a `Raw NBConvert` cell at the very top.
This is where you place the `YAML` header that is used in the blog post.
The one I have for this post looks like this:

```
---
layout: post
title:  "Example Jupyter Notebook to markdown"
date:   2016-06-24

categories: Tutorials

tags:
  - python
  - jupyter notebook
  - jekyll
  - blogging
---
```

The rest of the post is regular `code` cells from the notebook. 


```python
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
df = pd.DataFrame({'a': [1, 2, 3],
                   'b': ['a', 'b', 'c']})
```

Tables get rendered in the `html` table format


```python
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>a</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>b</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>c</td>
    </tr>
  </tbody>
</table>
</div>




```python
x = [1,2,3,4,5]
y = [5,4,3,2,1]
```

Plots work as well, but they need a little more work.


```python
plt.plot(x,y)
```




    [<matplotlib.lines.Line2D at 0x7fb4337e55f8>]




![png](/notebooks/2016-06-24_jupyter_to_markdown_files/2016-06-24_jupyter_to_markdown_9_1.png)


Images from the notebook are exported to a folder that has the same name as the notebook.
