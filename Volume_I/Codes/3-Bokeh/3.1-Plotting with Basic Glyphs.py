#!/usr/bin/env python
# coding: utf-8

# ## Scatter Markers

# In[1]:


from bokeh.plotting import figure, output_file, show

# output to static HTML file
output_file("line.html")

p = figure(plot_width=400, plot_height=400)

# add a circle renderer with a size, color, and alpha
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

# show the results
show(p)


# In[2]:


from bokeh.plotting import figure, output_file, show

# output to static HTML file
output_file("square.html")

p = figure(plot_width=400, plot_height=400)

# add a square renderer with a size, color, and alpha
p.square([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="olive", alpha=0.5)

# show the results
show(p)


# ## Line Glyphs
# ### Single Lines

# In[3]:


from bokeh.plotting import figure, output_file, show

output_file("line.html")

p = figure(plot_width=400, plot_height=400)

# add a line renderer
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

show(p)


# ### Step Lines
# 

# In[4]:


from bokeh.plotting import figure, output_file, show

output_file("line.html")

p = figure(plot_width=400, plot_height=400)

# add a steps renderer
p.step([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2, mode="center")

show(p)


# ### Multiple Lines

# In[5]:


from bokeh.plotting import figure, output_file, show

output_file("patch.html")

p = figure(plot_width=400, plot_height=400)

p.multi_line([[1, 3, 2], [3, 4, 6, 6]], [[2, 1, 4], [4, 7, 8, 5]],
             color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=4)

show(p)


# ### Missing Points

# In[6]:


from bokeh.plotting import figure, output_file, show

output_file("line.html")

p = figure(plot_width=400, plot_height=400)

# add a line renderer with a NaN
nan = float('nan')
p.line([1, 2, 3, nan, 4, 5], [6, 7, 2, 4, 4, 5], line_width=2)

show(p)


# ### Stacked Lines

# In[7]:


from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show

output_file("vline_stack.html")

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y1=[1, 2, 4, 3, 4],
    y2=[1, 4, 2, 2, 3],
))
p = figure(plot_width=400, plot_height=400)

p.vline_stack(['y1', 'y2'], x='x', source=source)

show(p)


# ## Bars and Rectangles
# ### Bars

# In[8]:


from bokeh.plotting import figure, output_file, show

output_file('vbar.html')

p = figure(plot_width=400, plot_height=400)
p.vbar(x=[1, 2, 3], width=0.5, bottom=0,
       top=[1.2, 2.5, 3.7], color="firebrick")

show(p)


# In[9]:


from bokeh.plotting import figure, output_file, show

output_file('hbar.html')

p = figure(plot_width=400, plot_height=400)
p.hbar(y=[1, 2, 3], height=0.5, left=0,
       right=[1.2, 2.5, 3.7], color="navy")

show(p)


# ### Stacked Bars

# In[11]:


from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show

output_file("hbar_stack.html")

source = ColumnDataSource(data=dict(
    y=[1, 2, 3, 4, 5],
    x1=[1, 2, 4, 3, 4],
    x2=[1, 4, 2, 2, 3],
))
p = figure(plot_width=400, plot_height=400)

p.hbar_stack(['x1', 'x2'], y='y', height=0.8, color=("red", "blue"), source=source)

show(p)


# ### Rectangles

# In[12]:


from bokeh.plotting import figure, output_file, show

output_file('rectangles.html')

p = figure(plot_width=400, plot_height=400)
p.quad(top=[2, 3, 4], bottom=[1, 2, 3], left=[1, 2, 3],
       right=[1.2, 2.5, 3.7], color="#B3DE69")

show(p)


# In[13]:


from math import pi

from bokeh.plotting import figure, output_file, show

output_file('rectangles_rotated.html')

p = figure(plot_width=400, plot_height=400)
p.rect(x=[1, 2, 3], y=[1, 2, 3], width=0.2, height=40, color="#CAB2D6",
       angle=pi/3, height_units="screen")

show(p)


# ### Hex Tiles

# In[1]:


import numpy as np

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.util.hex import axial_to_cartesian

output_file("hex_coords.html")

q = np.array([0,  0, 0, -1, -1,  1, 1])
r = np.array([0, -1, 1,  0,  1, -1, 0])

p = figure(plot_width=400, plot_height=400, toolbar_location=None)
p.grid.visible = False

p.hex_tile(q, r, size=1, fill_color=["firebrick"]*3 + ["navy"]*4,
           line_color="white", alpha=0.5)

x, y = axial_to_cartesian(q, r, 1, "pointytop")

p.text(x, y, text=["(%d, %d)" % (q,r) for (q, r) in zip(q, r)],
       text_baseline="middle", text_align="center")

show(p)


# In[2]:


import numpy as np

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin

n = 50000
x = np.random.standard_normal(n)
y = np.random.standard_normal(n)

bins = hexbin(x, y, 0.1)

p = figure(tools="wheel_zoom,reset", match_aspect=True, background_fill_color='#440154')
p.grid.visible = False

p.hex_tile(q="q", r="r", size=0.1, line_color=None, source=bins,
           fill_color=linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))

output_file("hex_tile.html")

show(p)


# ## Directed Areas
# ### Single Areas

# In[2]:


from bokeh.plotting import figure, output_file, show

output_file("varea.html")

p = figure(plot_width=400, plot_height=400)

p.varea(x=[1, 2, 3, 4, 5],
        y1=[2, 6, 4, 3, 5],
        y2=[1, 4, 2, 2, 3])

show(p)


# ### Stacked Areas

# In[4]:


from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show

output_file("varea_stack.html")

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y1=[1, 2, 4, 3, 4],
    y2=[1, 4, 2, 2, 3],
))
p = figure(plot_width=400, plot_height=400)

p.varea_stack(['y1', 'y2'], x='x', color=("blue", "red"), source=source)

show(p)


# ## Patches and Polygons
# ### Single Patches

# In[6]:


from bokeh.plotting import figure, output_file, show

output_file("patch.html")

p = figure(plot_width=400, plot_height=400)

# add a patch renderer with an alpha and line width
p.patch([1, 2, 3, 4, 5], [6, 7, 8, 7, 3], alpha=0.5, line_width=2)

show(p)


# ### Multiple Patches

# In[7]:


from bokeh.plotting import figure, output_file, show

output_file("patch.html")

p = figure(plot_width=400, plot_height=400)

p.patches([[1, 3, 2], [3, 4, 6, 6]], [[2, 1, 4], [4, 7, 8, 5]],
          color=["firebrick", "navy"], alpha=[0.8, 0.3], line_width=2)

show(p)


# ### Missing Points

# In[8]:


from bokeh.plotting import figure, output_file, show

output_file("patch.html")

p = figure(plot_width=400, plot_height=400)

# add a patch renderer with a NaN value
nan = float('nan')
p.patch([1, 2, 3, nan, 4, 5, 6], [6, 7, 5, nan, 7, 3, 6], alpha=0.5, line_width=2)

show(p)


# ## Polygons with Holes
# ### Simple Polygon

# In[9]:


from bokeh.plotting import figure, output_file, show

output_file('multipolygon_simple.html')

p = figure(plot_width=400, plot_height=400)
p.multi_polygons(xs=[[[[1, 1, 2, 2]]]],
                 ys=[[[[3, 4, 4, 3]]]])

show(p)


# ### Polygon with Holes

# In[10]:


from bokeh.plotting import figure, output_file, show

output_file('multipolygon_with_holes.html')

p = figure(plot_width=400, plot_height=400)
p.multi_polygons(xs=[[[ [1, 2, 2, 1], [1.2, 1.6, 1.6], [1.8, 1.8, 1.6] ]]],
                 ys=[[[ [3, 3, 4, 4], [3.2, 3.6, 3.2], [3.4, 3.8, 3.8] ]]])

show(p)


# ### MultiPolygon with Separate Parts

# In[11]:


from bokeh.plotting import figure, output_file, show

output_file('multipolygon_with_separate_parts.html')

p = figure(plot_width=400, plot_height=400)
p.multi_polygons(xs=[[[ [1, 1, 2, 2], [1.2, 1.6, 1.6], [1.8, 1.8, 1.6] ], [ [3, 4, 3] ]]],
                 ys=[[[ [4, 3, 3, 4], [3.2, 3.2, 3.6], [3.4, 3.8, 3.8] ], [ [1, 1, 3] ]]])

show(p)


# ### Multiple MultiPolygons

# In[12]:


from bokeh.plotting import figure, output_file, show

output_file('multipolygons.html')

p = figure(plot_width=400, plot_height=400)
p.multi_polygons(
    xs=[
        [[ [1, 1, 2, 2], [1.2, 1.6, 1.6], [1.8, 1.8, 1.6] ], [ [3, 3, 4] ]],
        [[ [1, 2, 2, 1], [1.3, 1.3, 1.7, 1.7] ]]],
    ys=[
        [[ [4, 3, 3, 4], [3.2, 3.2, 3.6], [3.4, 3.8, 3.8] ], [ [1, 3, 1] ]],
        [[ [1, 1, 2, 2], [1.3, 1.7, 1.7, 1.3] ]]],
    color=['blue', 'red'])

show(p)


# ## Ellipses

# In[13]:


from math import pi

from bokeh.plotting import figure, output_file, show

output_file('ellipses.html')

p = figure(plot_width=400, plot_height=400)
p.ellipse(x=[1, 2, 3], y=[1, 2, 3], width=[0.2, 0.3, 0.1], height=0.3,
          angle=pi/3, color="#CAB2D6")

show(p)


# ## Images

# In[14]:


import numpy as np

from bokeh.plotting import figure, output_file, show

# create an array of RGBA data
N = 20
img = np.empty((N, N), dtype=np.uint32)
view = img.view(dtype=np.uint8).reshape((N, N, 4))
for i in range(N):
    for j in range(N):
        view[i, j, 0] = int(255 * i / N)
        view[i, j, 1] = 158
        view[i, j, 2] = int(255 * j / N)
        view[i, j, 3] = 255

output_file("image_rgba.html")

p = figure(plot_width=400, plot_height=400, x_range=(0, 10), y_range=(0, 10))

p.image_rgba(image=[img], x=[0], y=[0], dw=[10], dh=[10])

show(p)


# ## Colormapped Images

# In[15]:


import numpy as np

from bokeh.plotting import figure, output_file, show

output_file("image.html", title="image.py example")

x = np.linspace(0, 10, 250)
y = np.linspace(0, 10, 250)
xx, yy = np.meshgrid(x, y)
d = np.sin(xx)*np.cos(yy)

p = figure(plot_width=400, plot_height=400)
p.x_range.range_padding = p.y_range.range_padding = 0

p.image(image=[d], x=0, y=0, dw=10, dh=10, palette="Spectral11", level="image")
p.grid.grid_line_width = 0.5

show(p)


# ## Segments and Rays

# In[16]:


from bokeh.plotting import figure, show

p = figure(plot_width=400, plot_height=400)
p.segment(x0=[1, 2, 3], y0=[1, 2, 3], x1=[1.2, 2.4, 3.1],
          y1=[1.2, 2.5, 3.7], color="#F4A582", line_width=3)

show(p)


# In[17]:


from bokeh.plotting import figure, show

p = figure(plot_width=400, plot_height=400)
p.ray(x=[1, 2, 3], y=[1, 2, 3], length=45, angle=[30, 45, 60],
      angle_units="deg", color="#FB8072", line_width=2)

show(p)


# ## Wedges and Arcs

# In[18]:


from bokeh.plotting import figure, show

p = figure(plot_width=400, plot_height=400)
p.arc(x=[1, 2, 3], y=[1, 2, 3], radius=0.1, start_angle=0.4, end_angle=4.8, color="navy")

show(p)


# In[19]:


from bokeh.plotting import figure, show

p = figure(plot_width=400, plot_height=400)
p.wedge(x=[1, 2, 3], y=[1, 2, 3], radius=0.2, start_angle=0.4, end_angle=4.8,
        color="firebrick", alpha=0.6, direction="clock")

show(p)


# In[20]:


from bokeh.plotting import figure, show

p = figure(plot_width=400, plot_height=400)
p.annular_wedge(x=[1, 2, 3], y=[1, 2, 3], inner_radius=0.1, outer_radius=0.25,
                start_angle=0.4, end_angle=4.8, color="green", alpha=0.6)

show(p)


# In[21]:


from bokeh.plotting import figure, show

p = figure(plot_width=400, plot_height=400)
p.annulus(x=[1, 2, 3], y=[1, 2, 3], inner_radius=0.1, outer_radius=0.25,
          color="orange", alpha=0.6)

show(p)


# ## Specialized Curves
# ### Combining Multiple Glyphs

# In[22]:


from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 7, 3]

output_file("multiple.html")

p = figure(plot_width=400, plot_height=400)

# add both a line and circles on the same plot
p.line(x, y, line_width=2)
p.circle(x, y, fill_color="white", size=8)

show(p)


# ## Setting Ranges

# In[24]:


from bokeh.models import Range1d
from bokeh.plotting import figure, output_file, show

output_file("title.html")

# create a new plot with a range set with a tuple
p = figure(plot_width=400, plot_height=400, x_range=(0, 20))

# set a range using a Range1d
p.y_range = Range1d(0, 15)

p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

show(p)


# ## Specifying Axis Types
# ### Categorical Axes

# In[25]:


from bokeh.plotting import figure, output_file, show

factors = ["a", "b", "c", "d", "e", "f", "g", "h"]
x = [50, 40, 65, 10, 25, 37, 80, 60]

output_file("categorical.html")

p = figure(y_range=factors)

p.circle(x, factors, size=15, fill_color="orange", line_color="green", line_width=3)

show(p)


# ### Twin Axes

# In[1]:


from numpy import arange, linspace, pi, sin

from bokeh.models import LinearAxis, Range1d
from bokeh.plotting import figure, output_file, show

x = arange(-2*pi, 2*pi, 0.1)
y = sin(x)
y2 = linspace(0, 100, len(y))

output_file("twin_axis.html")

p = figure(x_range=(-6.5, 6.5), y_range=(-1.1, 1.1))

p.circle(x, y, color="red")

p.extra_y_ranges = {"foo": Range1d(start=0, end=100)}
p.circle(x, y2, color="blue", y_range_name="foo")
p.add_layout(LinearAxis(y_range_name="foo"), 'left')

show(p)


# In[ ]:




