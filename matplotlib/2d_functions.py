''' DRAW MULTIPLE GRAPHICS IN ONE DRAWING. 
https://www.topcoder.com/thrive/articles/draw-different-two-dimensional-graphs-with-matplotlib-in-python'''

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 50)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.title('sin(x) & cos(x)')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.plot(x, y_sin, color = "red", linewidth = 1.5, linestyle = "-.", label = "y_sin")
plt.plot(x, y_cos, color = "green", linewidth = 1.5, linestyle = "-", label = "y_cos")
plt.plot(x, 1.5 * y_cos, marker = '+', linestyle = '-', label = '1.5 y_cos')

plt.legend(loc= 'upper left')

plt.show()
