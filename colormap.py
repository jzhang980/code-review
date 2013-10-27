# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from matplotlib.colors import Normalize, LinearSegmentedColormap
a = arange(100).reshape(10,10)
a

# <codecell>

matplotlib.colors.LinearSegmentedColormap?

# <codecell>

cdict = {
    'red':   ((0.,    1, 1),
              (0.05,  1, 1),
              (0.11,  0, 0),
              (0.66,  1, 1),
              (0.89,  1, 1),
              (1,     0.5, 0.5)),
    'green': ((0.,    1, 1),
              (0.05,  1, 1),
              (0.11,  0, 0),
              (0.375, 1, 1),
              (0.64,  1, 1),
              (0.91,  0, 0),
              (1,     0, 0)),
    'blue':  ((0.,    1, 1),
              (0.05,  1, 1),
              (0.11,  1, 1),
              (0.34,  1, 1),
              (0.65,  0, 0),
              (1,     0, 0))
}

num_segments = 10
cmap_name = 'my_colormap'
my_cmap = LinearSegmentedColormap(cmap_name, cdict, num_segments)
pcolor(a, cmap=my_cmap)
colorbar()
show()

# <codecell>

r = 10
cmap_name = 'my_colormap'
my_cmap = matplotlib.colors.LinearSegmentedColormap(cmap_name,cdict,r)
b = a * (a % 5)
pcolor(b, cmap=my_cmap)
colorbar()
show()

# <codecell>

b

# <codecell>

cm.datad.keys()

# <codecell>

cm.datad['gist_ncar_r']

# <codecell>

r = 10
cmap_name = 'gist_ncar_r'
ncar = matplotlib.colors.LinearSegmentedColormap(cmap_name,cm.datad[cmap_name],r)
pcolor(a, cmap=ncar)
colorbar()
show()

