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

x = loadtxt(data1, unpack=True, usecols=[0])/2
y = loadtxt(data1, unpack=True, usecols=[1])/2
z = loadtxt(data1, unpack=True, usecols=[2])/1e26


fig = plt.figure(figsize=(10,9.6))
fig.patch.set_alpha(0.0)
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111)
ax.patch.set_alpha(0.0)

xi = np.linspace(min(x), max(x), 100)
yi = np.linspace(min(y), max(y), 100)

X, Y = np.meshgrid(xi, yi)
Z = griddata(x, y, z, X, Y)

lvls = arange(0, 6, 0.5)
#ax.plot_surface(Y, X, Z, rstride=100, cstride=100, alpha=0.3, linewidth = 0.2)
#CS = ax.contour(Y,X, Z,  colors = 'red')
ax.contourf(X,Y, Z, cmap =cm.BuGn, levels = lvls)
#ax.clabel(CS)
#cset = ax.contourf(X, Y, Z, zdir='x', offset=-9, cmap=cm.coolwarm)
#cset = ax.contourf(X, Y, Z, zdir='y', offset=9, cmap=cm.coolwarm)

ax.set_xlabel('X')
#ax.set_xlim(-5,5)
ax.set_ylabel('Y')
#ax.set_ylim(-5,5)
#ax.set_zlabel('Z')



plt.show()
