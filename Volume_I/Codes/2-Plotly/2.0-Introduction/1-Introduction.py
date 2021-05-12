#!/usr/bin/env python
# coding: utf-8

# ### Test Installation

# In[4]:


import plotly
print(plotly.__version__)


# ### Making a Simple Graph

# In[5]:


import plotly
from plotly.graph_objs import Scatter, Layout

plotly.offline.plot({
    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world")
})


# ## Basic Charts
# 

# ### Scatter Plot
# 

# In[6]:



import plotly
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)
data = [trace]

# Plot and embed in ipython notebook!
plotly.offline.plot(data, filename='basic-scatter')


# ### Line and Scatter Plot
# 

# In[9]:



import plotly
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5

# Create traces
trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'markers',
    name = 'markers'
)

trace1 = go.Scatter(
    x = random_x,
    y = random_y1,
    mode = 'lines+markers',
    name = 'lines+markers'
)

trace2 = go.Scatter(
    x = random_x,
    y = random_y2,
    mode = 'lines',
    name = 'lines'
)

data = [trace0, trace1, trace2]
plotly.offline.plot(data, filename='scatter-mode')


# ### Making plots using Graph Objects
# 

# In[2]:


import pandas as pd
df = pd.read_csv('uk-election-results.csv')


# In[3]:


# Import Plotly and our data
import plotly.graph_objects as go

# Get a convenient list of x-values
years = df['year']
x = list(range(len(years)))

# Specify the plots
bar_plots = [
    go.Bar(x=x, y=df['conservative'], name='Conservative', marker=go.bar.Marker(color='#0343df')),
    go.Bar(x=x, y=df['labour'], name='Labour', marker=go.bar.Marker(color='#e50000')),
    go.Bar(x=x, y=df['liberal'], name='Liberal', marker=go.bar.Marker(color='#ffff14')),
    go.Bar(x=x, y=df['others'], name='Others', marker=go.bar.Marker(color='#929591')),
]
   
# Specify the layout
layout = go.Layout(
    title=go.layout.Title(text="Election results", x=0.5),
    yaxis_title="Seats",
    xaxis_tickmode="array",
    xaxis_tickvals=list(range(27)),
    xaxis_ticktext=tuple(df['year'].values),
)
       
# Make the multi-bar plot
fig = go.Figure(data=bar_plots, layout=layout)

# Tell Plotly to render it
fig.show()


# ### Bar chart

# In[12]:


# import all required libraries 
import numpy as np 
import plotly 
import plotly.graph_objects as go 
import plotly.offline as pyo 
from plotly.offline import init_notebook_mode 

init_notebook_mode(connected = True) 

# countries on x-axis 
countries=['England', 'canada', 
		'Australia','Brazil', 
		'Mexico','Russia', 
		'Germany','Switzerland', 
		'Texas'] 

# plotting corresponding y for each 
# country in x 
fig = go.Figure([go.Bar(x=countries, 
						y=[80,70,60,50, 
						40,50,60,70,80])]) 

fig.show()


# ### Pie chart

# In[13]:


# import all required libraries 
import numpy as np 
import plotly 
import plotly.graph_objects as go 
import plotly.offline as pyo 
from plotly.offline import init_notebook_mode 

init_notebook_mode(connected = True) 

# different individual parts in 
# total chart 
countries=['England', 'canada', 
		'Australia','Brazil', 
		'Mexico','Russia', 
		'Germany','Switzerland', 
		'Texas'] 

# values corresponding to each 
# individual country present in 
# countries 
values = [4500, 2500, 1053, 500, 
		3200, 1500, 1253, 600, 3500] 

# plotting pie chart 
fig = go.Figure(data=[go.Pie(labels=countries, 
					values=values)]) 

fig.show()


# ### Histogram

# In[14]:


# import all required libraries 
import numpy as np 
import plotly 
import plotly.graph_objects as go 
import plotly.offline as pyo 
from plotly.offline import init_notebook_mode 

init_notebook_mode(connected = True) 

# save the state of random 
np.random.seed(42) 

# generating 250 random numbers 
x = np.random.randn(250) 

# plotting histogram for x 
fig = go.Figure(data=[go.Histogram(x=x)]) 

fig.show()


# ### Box plot
# 

# In[15]:


# import all required libraries 
import numpy as np 
import plotly 
import plotly.graph_objects as go 
import plotly.offline as pyo 
from plotly.offline import init_notebook_mode 

init_notebook_mode(connected = True) 

np.random.seed(42) 

# generating 50 random numbers 
y = np.random.randn(50) 

# generating 50 random numbers 
y1 = np.random.randn(50) 
fig = go.Figure() 

# updating the figure with y 
fig.add_trace(go.Box(y=y)) 

# updating the figure with y1 
fig.add_trace(go.Box(y=y1)) 

fig.show()


# ### Contour Plots

# In[16]:



from plotly import tools
import plotly
import plotly.graph_objs as go

trace0 = go.Contour(
    z=[[2, 4, 7, 12, 13, 14, 15, 16],
       [3, 1, 6, 11, 12, 13, 16, 17],
       [4, 2, 7, 7, 11, 14, 17, 18],
       [5, 3, 8, 8, 13, 15, 18, 19],
       [7, 4, 10, 9, 16, 18, 20, 19],
       [9, 10, 5, 27, 23, 21, 21, 21],
       [11, 14, 17, 26, 25, 24, 23, 22]],
    line=dict(smoothing=0),
)

trace1 = go.Contour(
    z=[[2, 4, 7, 12, 13, 14, 15, 16],
       [3, 1, 6, 11, 12, 13, 16, 17],
       [4, 2, 7, 7, 11, 14, 17, 18],
       [5, 3, 8, 8, 13, 15, 18, 19],
       [7, 4, 10, 9, 16, 18, 20, 19],
       [9, 10, 5, 27, 23, 21, 21, 21],
       [11, 14, 17, 26, 25, 24, 23, 22]],
    line=dict(smoothing=0.85),
)

data = tools.make_subplots(rows=1, cols=2,
                          subplot_titles=('Without Smoothing', 'With Smoothing'))

data.append_trace(trace0, 1, 1)
data.append_trace(trace1, 1, 2)

plotly.offline.plot(data)


# ## Financial Charts
# 

# ### Time Series Plot
# 

# In[1]:



import plotly
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("finance-charts-apple.csv")

data = [go.Scatter(
          x=df.Date,
          y=df['AAPL.Close'])]

plotly.offline.plot(data)


# ### OHLC Chart

# In[18]:



import plotly
import plotly.graph_objs as go
from datetime import datetime

open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
high_data = [33.1, 33.3, 33.6, 33.2, 34.8]
low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
close_data = [33.0, 32.9, 33.3, 33.1, 33.1]

dates = [datetime(year=2013, month=10, day=10),
         datetime(year=2013, month=11, day=10),
         datetime(year=2013, month=12, day=10),
         datetime(year=2014, month=1, day=10),
         datetime(year=2014, month=2, day=10)]

trace = go.Ohlc(x=dates,
                open=open_data,
                high=high_data,
                low=low_data,
                close=close_data)
data = [trace]

plotly.offline.plot(data, filename='ohlc_datetime')


# In[ ]:




