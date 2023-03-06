''' OOP API is mor clear and readeable -as always
Same cases both implementations '''

import numpy as np
import matplotlib.pyplot as plt

### Drawing a Quadratic function: Second degree polynomial, graph is a parabola.

x = np.arange(-10, 11)
y_positive = x ** 2                     # positive_parabola
y_negative = -1 * y_positive            # negative parabola


## Global API (draw parabolas usin Matplotlib Global API)
# Matplotlib's default pyplot API has a global, MATLAB-style interface. Like procedural
# paradigm order or secuence define beahaivor.

plt.figure(figsize= (9, 5))
plt.plot(x, y_positive)
plt.plot(x, y_negative)
plt.title('My Nice Plot - Global API')
plt.show()                                  # display allabove plt. commands

## OOP API (draw parabolas usin Matplotlib OOP API)
#fig, axes = plt.subplots(figsize=(12, 6))

fig, axes = plt.subplots(figsize=(12, 6))   # two objects created
axes.plot(x, y_positive)
axes.plot(x, y_negative)
axes.set_title("My Nice Plot - OOP API")
plt.show()


# ### Drawing three plots in one graph: 1. Linear funct.: straight line, 2. Quadratic
# # funct.: parabola, 3. Cubic funct.: third degree polynomial. Using .subplot()

x = np.arange(-10, 11)
lf = 2.4 * x + 1
qf = 1.6 * x ** 2 + lf
cf = 0.9 * x ** 3 + qf

# # ## Global API

plt.figure(figsize=(12, 6))
plt.title('Linear, Quadratic, & Cubic functions')
plt.subplot(1, 3, 1)                                # rows, columns, panel selected
plt.plot(x, lf)                                     # plot the above panel
plt.subplot(1, 3, 2)                                # second fig in 1 row, 3 columns
plt.plot(x, qf)
plt.subplot(133)                                
plt.plot(x, cf)
plt.show()

## OOP API

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize= (11, 5))
ax1 = plt.subplot(131)
ax2 = plt.subplot(132)
ax3 = plt.subplot(1, 3, 3)
ax2.plot(x, qf)                 # e/obj w/ a defined plot no matter order of the code
ax3.plot(x, cf)
ax1.plot(x, lf)
plt.show()

### OOP plots in loops
functs_lst = [cf, qf, lf]
fig, axs = plt.subplots(1, len(functs_lst), figsize= (14, 6))
for i in range(len(functs_lst)):
    axs[i].plot(x, functs_lst[i])
plt.show()

# functs_lst = [lf, qf, cf, cf, qf, lf]
# fig, axs = plt.subplots(int(len(functs_lst)/2), len(functs_lst))
# for i in range(len(functs_lst)):
#     axs[i].plot(x, functs_lst[i])

# lst = [lf, -lf]
# fig, axs = plt.subplots(len(lst))
# fig.suptitle('Two elements lists')
# for i in range(len(lst)):
#     axs[i].plot(x, lst[i])
# # axs[0].plot(x, lf)
# # axs[1].plot(x, -lf)
# plt.show()


