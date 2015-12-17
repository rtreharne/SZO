"""
.. versionadded:: 1.1.0
   This demo depends on new features added to contourf3d.
"""
from pylab import *
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.mlab import griddata
from matplotlib.colors import LogNorm

data1 = 'pfton.txt'

x = loadtxt(data1, unpack=True, usecols=[0])
y = loadtxt(data1, unpack=True, usecols=[1])
z = loadtxt(data1, unpack=True, usecols=[2])

fig = plt.figure(figsize=(10,9.6))
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111)

xi = np.linspace(min(x), max(x))
yi = np.linspace(min(y), max(y))

X, Y = np.meshgrid(xi, yi)
Z = griddata(x, y, z, X, Y)

#ax.plot_surface(X, Y, Z, rstride=100, cstride=100, alpha=0.3, linewidth = 0.2)
levels = [0, 0.2, 0.5, 1, 2, 5, 10, 20]
CS = ax.contour(X, Y, Z, levels, colors = 'red')
#ax.contourf(X,Y,Z, cmap =cm.jet)
ax.clabel(CS)
#cset = ax.contourf(X, Y, Z, zdir='x', offset=-9, cmap=cm.coolwarm)
#cset = ax.contourf(X, Y, Z, zdir='y', offset=9, cmap=cm.coolwarm)

ax.set_xlabel('X')
#ax.set_xlim(-5,5)
ax.set_ylabel('Y')
#ax.set_ylim(-5,5)
#ax.set_zlabel('Z')



plt.show()
