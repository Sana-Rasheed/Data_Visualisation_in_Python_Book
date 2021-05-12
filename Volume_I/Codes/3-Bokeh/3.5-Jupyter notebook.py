#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bokeh.io import push_notebook,show, output_notebook
from bokeh.layouts import row
from bokeh.plotting import figure
output_notebook()


# In[2]:


p1 = figure(plot_width=250, plot_height= 250)
r1 = p1.circle([1,2,3],[4,5,6],size=20)

p2 = figure(plot_width=250, plot_height= 250)
r2 = p2.circle([1,2,3],[4,5,6],size=20)

# get a handle to update the shown cell with
t= show(row(p1,p2),notebook_handle=True)


# In[3]:


# the common handle repr show what cell it can be used to update
t


# In[4]:


r1.glyph.fill_color="white"
push_notebook(handle=t)


# In[5]:


p1 = figure(plot_width=250, plot_height= 250)
r1 = p1.circle([1,2,3],[4,5,6],size=20)

p2 = figure(plot_width=250, plot_height= 250)
r2 = p2.circle([1,2,3],[4,5,6],size=20)

# get a handle to update the shown cell with
t= show(row(p1,p2),notebook_handle=True)


# In[ ]:




