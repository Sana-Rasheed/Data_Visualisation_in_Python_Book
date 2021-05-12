#!/usr/bin/env python
# coding: utf-8

# ## Specifying Data in Altair
# 

# In[2]:


import altair as alt
import pandas as pd

data = pd.DataFrame({'x': ['A', 'B', 'C', 'D', 'E'],
                     'y': [5, 3, 6, 7, 2]})
alt.Chart(data).mark_bar().encode(
    x='x',
    y='y',
)


# In[3]:


import altair as alt

data = alt.Data(values=[{'x': 'A', 'y': 5},
                        {'x': 'B', 'y': 3},
                        {'x': 'C', 'y': 6},
                        {'x': 'D', 'y': 7},
                        {'x': 'E', 'y': 2}])
alt.Chart(data).mark_bar().encode(
    x='x:O',  # specify ordinal data
    y='y:Q',  # specify quantitative data
)


# In[4]:


import altair as alt
from vega_datasets import data
url = data.cars.url

alt.Chart(url).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
)


# ## Including Index Data
# 

# In[5]:


import numpy as np
rand = np.random.RandomState(0)

data = pd.DataFrame({'value': rand.randn(100).cumsum()},
                    index=pd.date_range('2018', freq='D', periods=100))
data.head()


# In[6]:


alt.Chart(data.reset_index()).mark_line().encode(
    x='index:T',
    y='value:Q'
)


# ## Long-form vs. Wide-form Data
# 

# In[7]:


wide_form = pd.DataFrame({'Date': ['2007-10-01', '2007-11-01', '2007-12-01'],
                          'AAPL': [189.95, 182.22, 198.08],
                          'AMZN': [89.15, 90.56, 92.64],
                          'GOOG': [707.00, 693.00, 691.48]})
print(wide_form)


# In[8]:


long_form = pd.DataFrame({'Date': ['2007-10-01', '2007-11-01', '2007-12-01',
                                   '2007-10-01', '2007-11-01', '2007-12-01',
                                   '2007-10-01', '2007-11-01', '2007-12-01'],
                          'company': ['AAPL', 'AAPL', 'AAPL',
                                      'AMZN', 'AMZN', 'AMZN',
                                      'GOOG', 'GOOG', 'GOOG'],
                          'price': [189.95, 182.22, 198.08,
                                     89.15,  90.56,  92.64,
                                    707.00, 693.00, 691.48]})
print(long_form)


# In[9]:


alt.Chart(long_form).mark_line().encode(
  x='Date:T',
  y='price:Q',
  color='company:N'
)


# ### Converting Between Long-form and Wide-form: Pandas
# 

# In[10]:


wide_form.melt('Date', var_name='company', value_name='price')


# In[11]:


long_form.pivot(index='Date', columns='company', values='price').reset_index()


# ### Converting Between Long-form and Wide-form: Fold Transform
# 

# In[12]:


alt.Chart(wide_form).transform_fold(
    ['AAPL', 'AMZN', 'GOOG'],
    as_=['company', 'price']
).mark_line().encode(
    x='Date:T',
    y='price:Q',
    color='company:N'
)


# ## Generated Data
# 

# ### Sequence Generator
# 

# In[13]:


import altair as alt

# Note that the following generator is functionally similar to
# data = pd.DataFrame({'x': np.arange(0, 10, 0.1)})
data = alt.sequence(0, 10, 0.1, as_='x')

alt.Chart(data).transform_calculate(
    y='sin(datum.x)'
).mark_line().encode(
    x='x:Q',
    y='y:Q',
)


# ### Graticule Generator
# 

# In[14]:


import altair as alt

data = alt.graticule(step=[15, 15])

alt.Chart(data).mark_geoshape(stroke='black').project(
    'orthographic',
    rotate=[0, -45, 0]
)


# ### Sphere Generator
# 

# In[2]:


import altair as alt

sphere_data = alt.sphere()
grat_data = alt.graticule(step=[15, 15])

background = alt.Chart(sphere_data).mark_geoshape(fill='aliceblue')
lines = alt.Chart(grat_data).mark_geoshape(stroke='black')

alt.layer(background, lines).project('naturalEarth1')


# ### Geospatial Data
# 

# In[16]:


{
    "type": "Feature",
    "geometry": {
        "coordinates": [[
            [0, 0],
            [0, 2],
            [2, 2],
            [2, 0],
            [0, 0]
        ]],
        "type": "Polygon"
    }
}


# In[ ]:




