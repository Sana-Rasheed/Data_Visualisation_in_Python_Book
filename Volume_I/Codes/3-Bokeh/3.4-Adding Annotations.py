#!/usr/bin/env python
# coding: utf-8

# ## Adding Annotations
# ### Titles

# In[33]:


from bokeh.plotting import figure, output_file, show

p = figure(title="Basic Title", plot_width=300, plot_height=300)
p.circle([1,2], [3,4])

output_file("title.html")

show(p)


# In[34]:


from bokeh.plotting import figure, output_file, show

p = figure(title="Left Title", title_location="left",
           plot_width=300, plot_height=300)
p.circle([1,2], [3,4])

output_file("title.html")

show(p)


# In[35]:


from bokeh.plotting import figure, output_file, show

p = figure(plot_width=300, plot_height=300)
p.circle([1,2], [3,4])

# configure visual properties on a plot's title attribute
p.title.text = "Title With Options"
p.title.align = "right"
p.title.text_color = "orange"
p.title.text_font_size = "25px"
p.title.background_fill_color = "#aaaaee"

output_file("title.html")

show(p)


# In[36]:


from bokeh.models import Title
from bokeh.plotting import figure, output_file, show

p = figure(title="Left Title", title_location="left",
           plot_width=300, plot_height=300)
p.circle([1,2], [3,4])

# add extra titles with add_layout(...)
p.add_layout(Title(text="Bottom Centered Title", align="center"), "below")

output_file("title.html")

show(p)


# In[37]:


from bokeh.plotting import figure, output_file, show

p = figure(title="Top Title with Toolbar", toolbar_location="above",
           plot_width=600, plot_height=300)
p.circle([1,2], [3,4])

output_file("title.html")

show(p)


# ## Legends
# ### Basic Legend Label

# In[38]:


import numpy as np

from bokeh.plotting import figure, output_file, show

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

output_file("legend.html")

p = figure()

p.circle(x, y, legend_label="sin(x)")
p.line(x, y, legend_label="sin(x)")

p.line(x, 2*y, legend_label="2*sin(x)",
       line_dash=[4, 4], line_color="orange", line_width=2)

p.square(x, 3*y, legend_label="3*sin(x)", fill_color=None, line_color="green")
p.line(x, 3*y, legend_label="3*sin(x)", line_color="green")

show(p)


# ### Automatic Grouping

# In[39]:


from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.palettes import RdBu3
from bokeh.plotting import figure

c1 = RdBu3[2] # red
c2 = RdBu3[0] # blue
source = ColumnDataSource(dict(
    x=[1, 2, 3, 4, 5, 6],
    y=[2, 1, 2, 1, 2, 1],
    color=[c1, c2, c1, c2, c1, c2],
    label=['hi', 'lo', 'hi', 'lo', 'hi', 'lo']
))

p = figure(x_range=(0, 7), y_range=(0, 3), plot_height=300, tools='save')

# legend field matches the column in the source
p.circle( x='x', y='y', radius=0.5, color='color', legend_group='label', source=source)

show(p)


# ## Manual Legends
# ### Explicit Index

# In[40]:


from bokeh.models import Legend, LegendItem
from bokeh.plotting import figure, show

p = figure()
r = p.multi_line([[1,2,3], [1,2,3]], [[1,3,2], [3,4,3]],
                 color=["orange", "red"], line_width=4)

legend = Legend(items=[
    LegendItem(label="orange", renderers=[r], index=0),
    LegendItem(label="red", renderers=[r], index=1),
])
p.add_layout(legend)

show(p)


# ### Interactive Legends

# ### Arrows

# In[41]:


from bokeh.models import Arrow, NormalHead, OpenHead, VeeHead
from bokeh.plotting import figure, output_file, show

output_file("arrow.html", title="arrow.py example")

p = figure(plot_width=600, plot_height=600)

p.circle(x=[0, 1, 0.5], y=[0, 0, 0.7], radius=0.1,
         color=["navy", "yellow", "red"], fill_alpha=0.1)

p.add_layout(Arrow(end=OpenHead(line_color="firebrick", line_width=4),
                   x_start=0, y_start=0, x_end=1, y_end=0))

p.add_layout(Arrow(end=NormalHead(fill_color="orange"),
                   x_start=1, y_start=0, x_end=0.5, y_end=0.7))

p.add_layout(Arrow(end=VeeHead(size=35), line_color="red",
                   x_start=0.5, y_start=0.7, x_end=0, y_end=0))

show(p)


# ### Bands

# In[42]:


import numpy as np
import pandas as pd

from bokeh.models import Band, ColumnDataSource
from bokeh.plotting import figure, output_file, show

output_file("band.html", title="band.py example")

# Create some random data
x = np.random.random(2500) * 140 - 20
y = np.random.normal(size=2500) * 2 + 5

df = pd.DataFrame(data=dict(x=x, y=y)).sort_values(by="x")

sem = lambda x: x.std() / np.sqrt(x.size)
df2 = df.y.rolling(window=100).agg({"y_mean": np.mean, "y_std": np.std, "y_sem": sem})
df2 = df2.fillna(method='bfill')

df = pd.concat([df, df2], axis=1)
df['lower'] = df.y_mean - df.y_std
df['upper'] = df.y_mean + df.y_std

source = ColumnDataSource(df.reset_index())

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
p = figure(tools=TOOLS)

p.scatter(x='x', y='y', line_color=None, fill_alpha=0.3, size=5, source=source)

band = Band(base='x', lower='lower', upper='upper', source=source, level='underlay',
            fill_alpha=1.0, line_width=1, line_color='black')
p.add_layout(band)

p.title.text = "Rolling Standard Deviation"
p.xgrid[0].grid_line_color=None
p.ygrid[0].grid_line_alpha=0.5
p.xaxis.axis_label = 'X'
p.yaxis.axis_label = 'Y'

show(p)


# ### Labels

# In[43]:


from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d
from bokeh.plotting import figure, output_file, show

output_file("label.html", title="label.py example")

source = ColumnDataSource(data=dict(height=[66, 71, 72, 68, 58, 62],
                                    weight=[165, 189, 220, 141, 260, 174],
                                    names=['Mark', 'Amir', 'Matt', 'Greg',
                                           'Owen', 'Juan']))

p = figure(title='Dist. of 10th Grade Students at Lee High',
           x_range=Range1d(140, 275))
p.scatter(x='weight', y='height', size=8, source=source)
p.xaxis[0].axis_label = 'Weight (lbs)'
p.yaxis[0].axis_label = 'Height (in)'

labels = LabelSet(x='weight', y='height', text='names', level='glyph',
              x_offset=5, y_offset=5, source=source, render_mode='canvas')

citation = Label(x=70, y=70, x_units='screen', y_units='screen',
                 text='Collected by Luke C. 2016-04-01', render_mode='css',
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=1.0)

p.add_layout(labels)
p.add_layout(citation)

show(p)


# ### Slopes

# In[44]:


import numpy as np

from bokeh.models import Slope
from bokeh.plotting import figure, output_file, show

output_file("slope.html", title="slope.py example")

# linear equation parameters
gradient = 2
y_intercept = 10

# create random data
xpts = np.arange(0, 20)
ypts = gradient * xpts + y_intercept + np.random.normal(0, 4, 20)

p = figure(plot_width=450, plot_height=450, y_range=(0, 1.1 * max(ypts)))

p.circle(xpts, ypts, size=5, color="skyblue")

slope = Slope(gradient=gradient, y_intercept=y_intercept,
              line_color='orange', line_dash='dashed', line_width=3.5)

p.add_layout(slope)

p.yaxis.axis_label = 'y'
p.xaxis.axis_label = 'x'

show(p)


# ### Spans

# In[45]:


import time
from datetime import datetime as dt

from bokeh.models import Span
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.daylight import daylight_warsaw_2013

output_file("span.html", title="span.py example")

p = figure(x_axis_type="datetime", y_axis_type="datetime")

p.line(daylight_warsaw_2013.Date, daylight_warsaw_2013.Sunset,
       line_dash='solid', line_width=2, legend_label="Sunset")
p.line(daylight_warsaw_2013.Date, daylight_warsaw_2013.Sunrise,
       line_dash='dotted', line_width=2, legend_label="Sunrise")

start_date = time.mktime(dt(2013, 3, 31, 2, 0, 0).timetuple())*1000
daylight_savings_start = Span(location=start_date,
                              dimension='height', line_color='green',
                              line_dash='dashed', line_width=3)
p.add_layout(daylight_savings_start)

end_date = time.mktime(dt(2013, 10, 27, 3, 0, 0).timetuple())*1000
daylight_savings_end = Span(location=end_date,
                            dimension='height', line_color='red',
                            line_dash='dashed', line_width=3)
p.add_layout(daylight_savings_end)

p.title.text = "2013 Sunrise and Sunset times in Warsaw"
p.yaxis.axis_label = 'Time of Day'

show(p)


# ### Whiskers

# In[27]:


from bokeh.models import ColumnDataSource, Whisker
from bokeh.plotting import figure, show
from bokeh.sampledata.autompg import autompg as df

colors = ["red", "olive", "darkred", "goldenrod", "skyblue", "orange", "salmon"]

p = figure(plot_width=600, plot_height=300, title="Years vs mpg with Quartile Ranges")

base, lower, upper = [], [], []

for i, year in enumerate(list(df.yr.unique())):
    year_mpgs = df[df['yr'] == year]['mpg']
    mpgs_mean = year_mpgs.mean()
    mpgs_std = year_mpgs.std()
    lower.append(mpgs_mean - mpgs_std)
    upper.append(mpgs_mean + mpgs_std)
    base.append(year)

source_error = ColumnDataSource(data=dict(base=base, lower=lower, upper=upper))

p.add_layout(
    Whisker(source=source_error, base="base", upper="upper", lower="lower")
)

for i, year in enumerate(list(df.yr.unique())):
    y = df[df['yr'] == year]['mpg']
    color = colors[i % len(colors)]
    p.circle(x=year, y=y, color=color)

show(p)


# In[ ]:




