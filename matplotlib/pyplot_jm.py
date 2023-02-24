''' Pyplot tutorial: 
matplotlib.pyplot is a collection of functions that make matplotlib work like MATLAB
https://matplotlib.org/stable/tutorials/introductory/pyplot.html#pyplot-tutorial '''

import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

# plt.plot([1, 3, 7, 8, 9, 9.5, 9.6])
# plt.ylabel('a curve?')
# plt.show()

# plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
# plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.ylabel('[1, 4, 9, 16]')
# plt.xlabel('[1, 2, 3, 4]')
# plt.show()

# #plt.plot([1, 2, 3, 4], [1, 4, 9, 16])           # default 'b-' blue line 
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')     # comment previus you see only red circles
# plt.axis([0, 6, 0, 20])
# plt.title('plt.axis([0, 6, 0, 20]) - axis funct. in takes a list of [xmin, xmax, ymin, ymax].\n')
# plt.show()

### numpy arrays (...In fact, all sequences are converted to numpy arrays internally)
import numpy as np

# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
# print(t)
# t_jm =[round((x/10 * 2), 1) for x in range(25)] #-- something like that LATER !!
# print(t_jm)
# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.title("plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')")
# plt.show()
# t_jm_sqr = list(map(lambda x: round(x ** 2, 2), t_jm))
# t_jm_cub = list(map(lambda x: round(x ** 3, 2), t_jm))
# plt.title("plt.plot(t_jm, t_jm, 'r--', t_jm, t_jm_sqr, 'bs', t_jm, t_jm_cub, 'g^')")
# plt.plot(t_jm, t_jm, 'r--', t_jm, t_jm_sqr, 'bs', t_jm, t_jm_cub, 'g^')
# plt.show()

# ## Plotting with keyword strings (data keyword arg.)
# mydata = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# mydata['b'] = mydata['a'] + 10 * np.random.randn(50)
# mydata['d'] = np.abs(mydata['d']) * 100
# plt.scatter('a', 'b', c='c', s='d', data=mydata)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()

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