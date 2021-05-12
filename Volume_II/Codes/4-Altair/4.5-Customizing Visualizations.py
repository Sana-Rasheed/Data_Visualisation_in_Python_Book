#!/usr/bin/env python
# coding: utf-8

# ## Customizing Visualizations
# 

# ### Adjusting Axis Limits
# 

# In[1]:


import altair as alt
from vega_datasets import data

cars = data.cars.url

alt.Chart(cars).mark_point().encode(
    x='Acceleration:Q',
    y='Horsepower:Q'
)


# In[2]:


alt.Chart(cars).mark_point().encode(
    alt.X('Acceleration:Q',
        scale=alt.Scale(zero=False)
    ),
    y='Horsepower:Q'
)


# In[3]:


alt.Chart(cars).mark_point().encode(
    alt.X('Acceleration:Q',
        scale=alt.Scale(domain=(5, 20))
    ),
    y='Horsepower:Q'
)


# In[4]:


alt.Chart(cars).mark_point(clip=True).encode(
    alt.X('Acceleration:Q',
        scale=alt.Scale(domain=(5, 20))
    ),
    y='Horsepower:Q'
)


# In[5]:


alt.Chart(cars).mark_point().encode(
    alt.X('Acceleration:Q',
        scale=alt.Scale(
            domain=(5, 20),
            clamp=True
        )
    ),
    y='Horsepower:Q'
).interactive()


# ### Adjusting Axis Labels
# 

# In[6]:


import pandas as pd
df = pd.DataFrame({'x': [0.03, 0.04, 0.05, 0.12, 0.07, 0.15],
                   'y': [10, 35, 39, 50, 24, 35]})

alt.Chart(df).mark_circle().encode(
    x='x',
    y='y'
)


# In[7]:


alt.Chart(df).mark_circle().encode(
    x=alt.X('x', axis=alt.Axis(format='%', title='percentage')),
    y=alt.Y('y', axis=alt.Axis(format='$', title='dollar amount'))
)


# In[8]:


alt.Chart(df).mark_circle().encode(
    x=alt.X('x', axis=alt.Axis(labels=False)),
    y=alt.Y('y', axis=alt.Axis(labels=False))
)


# ### Adjusting the Legend
# 

# In[9]:


import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color='species'
)


# In[10]:


import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color=alt.Color('species', legend=alt.Legend(title="Species by color"))
)


# In[11]:


import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color=alt.Color('species', legend=alt.Legend(orient="left")),
)


# In[12]:


import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color=alt.Color('species', legend=None),
)


# ### Removing the Chart Border
# 

# In[13]:


import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color='species'
)


# In[14]:


import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color='species'
).configure_axis(
    grid=False
)


# In[15]:


import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color='species'
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
)


# In[16]:


import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    alt.X('petalWidth', axis=None),
    alt.Y('petalLength', axis=None),
    color='species'
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0
)


# ## Customizing Colors
# 

# ### Color Schemes
# 

# In[17]:


import altair as alt
from vega_datasets import data

iris = data.iris()

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color=alt.Color('species', scale=alt.Scale(scheme='dark2'))
)


# ### Color Domain and Range
# 

# In[18]:


import altair as alt
from vega_datasets import data

iris = data.iris()
domain = ['setosa', 'versicolor', 'virginica']
range_ = ['red', 'green', 'blue']

alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y='petalLength',
    color=alt.Color('species', scale=alt.Scale(domain=domain, range=range_))
)


# ### Raw Color Values
# 

# In[19]:


import pandas as pd
import altair as alt

data = pd.DataFrame({
    'x': range(6),
    'color': ['red', 'steelblue', 'chartreuse', '#F4D03F', '#D35400', '#7D3C98']
})

alt.Chart(data).mark_point(
    filled=True,
    size=100
).encode(
    x='x',
    color=alt.Color('color', scale=None)
)


# ### Adjusting the width of Bar Marks
# 

# In[20]:


import altair as alt
import pandas as pd

data = pd.DataFrame({'name': ['a', 'b'], 'value': [4, 10]})

alt.Chart(data).mark_bar(size=10).encode(
    x='name:O',
    y='value:Q'
)


# In[21]:


alt.Chart(data).mark_bar(size=30).encode(
    x='name:O',
    y='value:Q'
)


# In[22]:


alt.Chart(data).mark_bar(size=30).encode(
    x='name:O',
    y='value:Q'
).properties(width=200)


# In[23]:


alt.Chart(data).mark_bar(size=30).encode(
    x='name:N',
    y='value:Q'
).properties(width=alt.Step(100))


# ### Adjusting Chart Size
# 

# In[24]:


import altair as alt
from vega_datasets import data

cars = data.cars()

alt.Chart(cars).mark_bar().encode(
    x='Origin',
    y='count()'
).properties(
    width=200,
    height=150
)


# In[25]:


alt.Chart(cars).mark_bar().encode(
    x='Origin',
    y='count()',
    column='Cylinders:Q'
).properties(
    width=100,
    height=100
)


# In[ ]:




