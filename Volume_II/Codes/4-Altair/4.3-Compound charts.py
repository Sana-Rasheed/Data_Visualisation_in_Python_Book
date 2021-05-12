#!/usr/bin/env python
# coding: utf-8

# ## Compound Charts: Layer, HConcat, VConcat, Repeat, Facet
# 

# ### Layered Charts
# 

# In[1]:


import altair as alt
from altair.expr import datum

from vega_datasets import data
stocks = data.stocks.url

base = alt.Chart(stocks).encode(
    x='date:T',
    y='price:Q',
    color='symbol:N'
).transform_filter(
    datum.symbol == 'GOOG'
)

base.mark_line() + base.mark_point()


# In[2]:


alt.layer(
  base.mark_line(),
  base.mark_point(),
  base.mark_rule()
).interactive()


# ### Order of Layers
# 

# In[3]:


import altair as alt
from vega_datasets import data

source = data.movies.url

heatmap = alt.Chart(source).mark_rect().encode(
    alt.X('IMDB_Rating:Q', bin=True),
    alt.Y('Rotten_Tomatoes_Rating:Q', bin=True),
    alt.Color('count()', scale=alt.Scale(scheme='greenblue'))
)

points = alt.Chart(source).mark_circle(
    color='black',
    size=5,
).encode(
    x='IMDB_Rating:Q',
    y='Rotten_Tomatoes_Rating:Q',
)

heatmap + points


# In[4]:


points + heatmap


# ### Horizontal Concatenation
# 

# In[5]:


import altair as alt
from vega_datasets import data

iris = data.iris.url

chart1 = alt.Chart(iris).mark_point().encode(
    x='petalLength:Q',
    y='petalWidth:Q',
    color='species:N'
).properties(
    height=300,
    width=300
)

chart2 = alt.Chart(iris).mark_bar().encode(
    x='count()',
    y=alt.Y('petalWidth:Q', bin=alt.Bin(maxbins=30)),
    color='species:N'
).properties(
    height=300,
    width=100
)

chart1 | chart2


# In[6]:


alt.hconcat(chart1, chart2)


# ### Vertical Concatenation
# 

# In[7]:


import altair as alt
from vega_datasets import data

source = data.sp500.url

brush = alt.selection(type='interval', encodings=['x'])

base = alt.Chart(source).mark_area().encode(
    x = 'date:T',
    y = 'price:Q'
).properties(
    width=600,
    height=200
)

upper = base.encode(
    alt.X('date:T', scale=alt.Scale(domain=brush))
)

lower = base.properties(
    height=60
).add_selection(brush)

alt.vconcat(upper, lower)


# ### Repeated Charts
# 

# In[9]:


import altair as alt
from vega_datasets import data

iris = data.iris.url

base = alt.Chart().mark_point().encode(
    color='species:N'
).properties(
    width=200,
    height=200
).interactive()

chart = alt.vconcat(data=iris)
for y_encoding in ['petalLength:Q', 'petalWidth:Q']:
    row = alt.hconcat()
    for x_encoding in ['sepalLength:Q', 'sepalWidth:Q']:
        row |= base.encode(x=x_encoding, y=y_encoding)
    chart &= row
chart


# In[10]:


import altair as alt
from vega_datasets import data
iris = data.iris.url

alt.Chart(iris).mark_point().encode(
    alt.X(alt.repeat("column"), type='quantitative'),
    alt.Y(alt.repeat("row"), type='quantitative'),
    color='species:N'
).properties(
    width=200,
    height=200
).repeat(
    row=['petalLength', 'petalWidth'],
    column=['sepalLength', 'sepalWidth']
).interactive()


# ### Faceted Charts
# 

# In[11]:


import altair as alt
from altair.expr import datum
from vega_datasets import data
iris = data.iris.url

base = alt.Chart(iris).mark_point().encode(
    x='petalLength:Q',
    y='petalWidth:Q',
    color='species:N'
).properties(
    width=160,
    height=160
)

chart = alt.hconcat()
for species in ['setosa', 'versicolor', 'virginica']:
    chart |= base.transform_filter(datum.species == species)
chart


# In[12]:


alt.Chart(iris).mark_point().encode(
    x='petalLength:Q',
    y='petalWidth:Q',
    color='species:N'
).properties(
    width=180,
    height=180
).facet(
    column='species:N'
)


# In[13]:


alt.Chart(iris).mark_point().encode(
    x='petalLength:Q',
    y='petalWidth:Q',
    color='species:N',
    column='species:N'
).properties(
    width=180,
    height=180
)


# In[15]:


hover = alt.selection_single(on='mouseover', nearest=True, empty='none')

base = alt.Chart(iris).encode(
    x='petalLength:Q',
    y='petalWidth:Q',
    color=alt.condition(hover, 'species:N', alt.value('black'))
).properties(
    width=180,
    height=180,
)

points = base.mark_point().add_selection(
    hover
)

text = base.mark_text(dy=-5).encode(
    text = 'species:N',
    opacity = alt.condition(hover, alt.value(1), alt.value(0))
)

alt.layer(points, text).facet(
    'species:N',
)


# ## Scale and Guide Resolution

# In[16]:


import altair as alt
from vega_datasets import data

source = data.cars()

base = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
).properties(
    width=200,
    height=200
)

alt.concat(
    base.encode(color='Origin:N'),
    base.encode(color='Cylinders:O')
)


# In[17]:


alt.concat(
    base.encode(color='Origin:N'),
    base.encode(color='Cylinders:O')
).resolve_scale(
    color='independent'
)


# ### Dual Y Axis
# 

# In[18]:


import altair as alt
from vega_datasets import data

source = data.cars()

base = alt.Chart(source).encode(
        alt.X('year(Year):T')
)

line_A = base.mark_line(color='#5276A7').encode(
    alt.Y('average(Horsepower):Q', axis=alt.Axis(titleColor='#5276A7'))
)

line_B = base.mark_line(color='#F18727').encode(
    alt.Y('average(Miles_per_Gallon):Q', axis=alt.Axis(titleColor='#F18727'))
)

alt.layer(line_A, line_B).resolve_scale(y='independent')


# In[19]:


base = alt.Chart(source).mark_line().transform_fold(
    ['Horsepower', 'Miles_per_Gallon'],
    as_=['Measure', 'Value']
).encode(
    alt.Color('Measure:N'),
    alt.X('year(Year):T')
)

line_A = base.transform_filter(
    alt.datum.Measure == 'Horsepower'
).encode(
    alt.Y('average(Value):Q', axis=alt.Axis(title='Horsepower')),
)

line_B = base.transform_filter(
    alt.datum.Measure == 'Miles_per_Gallon'
).encode(
    alt.Y('average(Value):Q',axis=alt.Axis(title='Miles_per_Gallon'))
)

alt.layer(line_A, line_B).resolve_scale(y='independent')


# In[ ]:




