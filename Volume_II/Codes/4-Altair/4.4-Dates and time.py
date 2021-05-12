#!/usr/bin/env python
# coding: utf-8

# ### Browser Compliance

# In[1]:


import altair as alt
import pandas as pd

df = pd.DataFrame({'local': ['2018-01-01T00:00:00'],
                   'utc': ['2018-01-01T00:00:00Z']})

alt.Chart(df).transform_calculate(
    compliant="hours(datum.local) != hours(datum.utc) ? true : false",
).mark_text(size=20, baseline='middle').encode(
    text=alt.condition('datum.compliant', alt.value('OK'), alt.value('not OK')),
    color=alt.condition('datum.compliant', alt.value('green'), alt.value('red'))
).properties(width=80, height=50)


# ### Altair and Pandas Datetimes
# 

# In[2]:


import altair as alt
from vega_datasets import data

temps = data.seattle_temps()
temps.head()


# In[3]:


temps.dtypes


# In[4]:


temps = temps[temps.date < '2010-01-15']

alt.Chart(temps).mark_line().encode(
    x='date:T',
    y='temp:Q'
)


# In[5]:


alt.Chart(temps).mark_rect().encode(
    alt.X('hoursminutes(date):O', title='hour of day'),
    alt.Y('monthdate(date):O', title='date'),
    alt.Color('temp:Q', title='temperature (F)')
)


# ### Specifying Time Zones
# 

# In[6]:


temps['date_pacific'] = temps['date'].dt.tz_localize('US/Pacific')
temps.dtypes


# In[7]:


alt.Chart(temps).mark_rect().encode(
    alt.X('hoursminutes(date_pacific):O', title='hour of day'),
    alt.Y('monthdate(date_pacific):O', title='date'),
    alt.Color('temp:Q', title='temperature (F)')
)


# ### Using UTC Time
# 

# In[8]:


alt.Chart(temps).mark_rect().encode(
    alt.X('utchoursminutes(date_pacific):O', title='UTC hour of day'),
    alt.Y('utcmonthdate(date_pacific):O', title='UTC date'),
    alt.Color('temp:Q', title='temperature (F)')
)


# In[9]:


temps['date_utc'] = temps['date'].dt.tz_localize('UTC')

alt.Chart(temps).mark_rect().encode(
    alt.X('utchoursminutes(date_utc):O', title='hour of day'),
    alt.Y('utcmonthdate(date_utc):O', title='date'),
    alt.Color('temp:Q', title='temperature (F)')
)


# In[ ]:




