# 3D grpahs in Python

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# FIRST Ex.-- Change the Size of Graph using figsize=
fig = plt.figure(figsize=(10, 6))
# Generating a 3D sine wave
ax = plt.axes(projection='3d')
# Creating array points using numpy
x = np.arange(0, 20, 0.1)
y = np.sin(x)
z = y*np.sin(x)
c = x + y
# To create a scatter graph
ax.scatter(x, y, z, c=c)
# turn off/on axis
plt.axis('off')
# show the graph
plt.show()

# https://stackoverflow.com/users/380231/tacaswell

#


# #ax = Axes3D(fig) DONT WORK??
# fig = plt.figure()
# ax = Axes3D(fig)
# dim = 10
# # Define x,y plane.
# X, Y = np.meshgrid([-dim, dim], [-dim, dim])
# Z = np.zeros((2, 2))
# # Define inclined plane.
# angle = 0.5  # <-- This is the variable
# X2, Y2 = np.meshgrid([-dim, dim], [0, dim])
# Z2 = Y2 * angle
# X3, Y3 = np.meshgrid([-dim, dim], [-dim, 0])
# Z3 = Y3 * angle
# # Plot x,y plane.
# ax.plot_surface(X, Y, Z, color='gray', alpha=.5, linewidth=0, zorder=1)
# # Plot top half of inclined plane.
# ax.plot_surface(X2, Y2, Z2, color='blue', alpha=.5, linewidth=0, zorder=3)
# # Plot bottom half of inclined plane.
# ax.plot_surface(X2, Y3, Z3, color='blue', alpha=.5, linewidth=0, zorder=-1)
# ax.set_xlim(-10., 10.)
# ax.set_ylim(-10., 10.)
# ax.set_zlim(-10., 10.)
# plt.show()

# # projection 3d ??
# values = range(-10, 11)
# def plotPlane(plot, normal, d, values, colorName):
#     # x, y, z
#     x, y = np.meshgrid(values, values)
#     z = (-normal[0] * x - normal[1] * y - d) * 1. / normal[2]
#     # draw plot
#     plot.plot_surface(x, y, z, color=colorName)
# image = plt.figure().gca(projection='3d')
# plotPlane(image, [3, 2, -4], 1, values, "red")
# plotPlane(image, [5, -1, 2], 4, values, "gray")
# plt.show()

# ## Other simple case
# #https://stackoverflow.com/questions/53115276/matplotlib-how-to-draw-a-vertical-plane-in-3d-figure
# xs = np.linspace(0, 10, 100)
# zs = np.linspace(0, 10, 100)
# X, Z = np.meshgrid(xs, zs)
# Y = 5 - X
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X, Y, Z)
# plt.show()

# ## -DONT WORK... Axes3D--
# fig = plt.figure()
# ax = Axes3D(fig)
# for i in range(20):
#     theta = 2*np.pi*np.random.uniform(-1,1)    
#     psi = 2*np.pi*np.random.uniform(-1,1)
#     normal = np.array([np.sin(theta)*np.cos(psi),np.sin(theta)*np.sin(psi),
#                        np.cos(theta)])
#     xx, yy = np.meshgrid(np.arange(-1,1), np.arange(-1,1))
#     z = (-normal[0] * xx - normal[1] * yy)/normal[2]
#     ax.plot_surface(xx, yy, z, alpha=0.5)
# plt.show()


## Other - several cases: (projection=3d invalid????)
#https://stackoverflow.com/questions/3461869/plot-a-plane-based-on-a-normal-vector-and-a-point-in-matlab-or-matplotlib/12503243#12503243
# point  = np.array([1, 2, 3])
# normal = np.array([1, 1, 2])
# # a plane is a*x+b*y+c*z+d=0
# # [a,b,c] is the normal. Thus, we have to calculate
# # d and we're set
# d = -point.dot(normal)
# # create x,y
# xx, yy = np.meshgrid(range(10), range(10))
# # calculate corresponding z
# z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]
# # plot the surface
# plt3d = plt.figure().gca(projection='3d')
# plt3d.plot_surface(xx, yy, z)
# plt.show()

# ## Other case - simple plane
# yy, zz = np.meshgrid(range(2), range(2))
# xx = yy*0
# ax = plt.subplot(projection='3d')
# ax.plot_surface(xx, yy, zz)
# plt.show()

# # Other try:
# xis, yis = np.meshgrid(range(-3,4), range(-3, 4))
# z = 4 * yis + 3.5 * xis
# ax = plt.subplot(projection='3d')
# ax.plot_surface(xis, yis, z)
# plt.show()


# ## Other case -- PyVista
# import pyvista as pv
# plane1 = pv.Plane(center=(1.0, 0.0, 0.0), 
#                   direction=(1.0, 0.0, 0.0))
# plane2 = pv.Plane(center=(1.0, 2.0, 0.0), 
#                   direction=(0.0, 1.0, 0.0))
# plotter = pv.Plotter()
# plotter.add_mesh(plane1, color='blue')
# plotter.add_mesh(plane2, color='red')
# plotter.show_grid()
# plotter.show()

# ## Other nice 2D case.
# def f(x):
#     return 1.1*x - 1
# x = np.arange(-30,30)
# y = f(x)
# # Plot the line.
# plt.plot( x, y, 'r' )
# # Plot the two points.
# plt.plot( 7, f(7), 'bo' )
# plt.annotate( 'A', (7, f(7)-4), color='blue' )
# plt.plot( 17, f(17), 'ro')
# plt.annotate( 'B', (17, f(17)-4), color='red' )
# # Draw the axes.
# plt.axhline(0,color='black')
# plt.axvline(0,color='black')
# # Draw the grid lines.
# plt.minorticks_on()
# plt.grid( True, 'minor', markevery=2, linestyle='--' )
# plt.grid( True, 'major', markevery=10 )
# plt.show()


# ## Other case.. intesecction planes
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# dim = 10
# X, Y = np.meshgrid([-dim, dim], [-dim, dim])
# Z = np.zeros((2, 2))
# angle = .5
# X2, Y2 = np.meshgrid([-dim, dim], [0, dim])
# Z2 = Y2 * angle
# X3, Y3 = np.meshgrid([-dim, dim], [-dim, 0])
# Z3 = Y3 * angle
# r = 7
# M = 1000
# th = np.linspace(0, 2 * np.pi, M)
# x, y, z = r * np.cos(th),  r * np.sin(th), angle * r * np.sin(th)
# ax.plot_surface(X2, Y3, Z3, color='blue', alpha=.5, linewidth=0, zorder=-1)
# ax.plot(x[y < 0], y[y < 0], z[y < 0], lw=5, linestyle='--', color='green',
#         zorder=0)
# ax.plot_surface(X, Y, Z, color='red', alpha=.5, linewidth=0, zorder=1)
# ax.plot(r * np.sin(th), r * np.cos(th), np.zeros(M), lw=5, linestyle='--',
#         color='k', zorder=2)
# ax.plot_surface(X2, Y2, Z2, color='blue', alpha=.5, linewidth=0, zorder=3)
# ax.plot(x[y > 0], y[y > 0], z[y > 0], lw=5, linestyle='--', color='green',
#         zorder=4)
# plt.axis('off')
# plt.show()


## Other case... - Surface plot
# # defining surface and axes
# x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
# y = x.copy().T
# z = np.cos(x ** 2 + y ** 3)
# # xis = np.outer(np.linspace(-2, 2, 10), np.ones(10))
# # yis = xis.copy().T
# # z = 4 * yis + 3.5 * xis
# fig = plt.figure()
# # syntax for 3-D plotting
# ax = plt.axes(projection ='3d')
# # syntax for plotting
# ax.plot_surface(x, y, z, cmap ='viridis', edgecolor ='green')
# ax.set_title('Surface plot geeks for geeks')
# plt.show()


# ## Other case...
# # Change the Size of Graph using
# fig = plt.figure(figsize=(10, 7))
# # Generating a 3D sine wave
# ax = plt.axes(projection='3d')
# # Create axis
# axes = [5, 5, 5]
# # Create Data
# data = np.ones(axes)
# # Control Tranperency
# alpha = 0.9
# # Control colour
# colors = np.empty(axes + [4])
# colors[0] = [1, 0, 0, alpha] # red
# colors[1] = [0, 1, 0, alpha] # green
# colors[2] = [0, 0, 1, alpha] # blue
# colors[3] = [1, 1, 0, alpha] # yellow
# colors[4] = [1, 1, 1, alpha] # grey
# # turn off/on axis
# plt.axis('off')
# # Voxels is used to customizations of the sizes, positions and colors.
# ax.voxels(data, facecolors=colors, edgecolors='grey')
# plt.show()

# ## Other case...
# fig = plt.figure(figsize=(8, 6))
# ax = plt.axes(projection='3d')
# #ax = Axes3D(fig)
# x = [6,3,6,9,12,24]
# y = [3,5,78,12,23,56]
# ax.plot(x, y, zs=0, zdir='z', label='zs=0, zdir=z')
# plt.show()

# # ## Other
# fig = plt.figure(figsize=(9, 6))
# ax = plt.axes(projection='3d')
# x = [6,3,6,9,12,24]
# y = [3,5,78,12,23,56]
# # put 0s on the y-axis, and put the y axis on the z-axis
# ax.plot(xs=x, ys=[0]*len(x), zs=y, zdir='z', label='ys=0, zdir=z')
# plt.show()

# ## 2D-Grpah
# # plt.plot(x, y)
# # plt.show()

