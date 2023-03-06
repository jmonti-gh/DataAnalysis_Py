''' Pyplot tutorial: 
matplotlib.pyplot is a collection of functions that make matplotlib work like MATLAB
https://matplotlib.org/stable/tutorials/introductory/pyplot.html#pyplot-tutorial
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html '''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Three integers (nrows, ncols, index). fig.add_subplot(235) is the same as
# fig.add_subplot(2, 3, 5). Can only be used if there are no more than 9 subplots.


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 3.0, 0.01)

ax1 = plt.subplot(212)
ax1.margins(0.05)           # Default margin is 0.05, value 0 means fit
ax1.plot(t1, f(t1))

ax2 = plt.subplot(221)
ax2.margins(2, 2)           # Values >0.0 zoom out
ax2.plot(t1, f(t1))
ax2.set_title('Zoomed out')

ax3 = plt.subplot(222)
ax3.margins(x=0, y=-0.25)   # Values in (-0.5, 0.0) zooms in to center
ax3.plot(t1, f(t1))
ax3.set_title('Zoomed in')

plt.show()


# plot a line, implicitly creating a subplot(111)
plt.plot([1, 2, 3])
# now create a subplot which represents the top plot of a grid
# with 2 rows and 1 column. Since this subplot will overlap the
# first, the plot (and its axes) previously created, will be removed
plt.subplot(211)
plt.show()

## Plotting with categorical variables
names = ['grp_a', 'grp_b', 'grp_c']
values = [1, 10, 100]
plt.figure(figsize=(9, 5))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
# plt.subplot(133)
# plt.plot(names, values, 'ro')
plt.suptitle('Categorical Plotting')
plt.show()

## Controlling line properties
#plt.plot(x, y, linewidth=2.0) ....

''' Working with multiple figures and axes - Working with text
Logarithmic and other nonlinear axes -  '''

# https://matplotlib.org/stable/users/explain/api_interfaces.html#api-interfaces
# https://matplotlib.org/stable/tutorials/introductory/quick_start.html