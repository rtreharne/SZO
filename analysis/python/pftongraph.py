"""
Plot graph from data "pfton.txt"
"""
from pylab import *
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.mlab import griddata

data = 'pfton.txt'
x = loadtxt(data, unpack=True, usecols=[0])/2
y = loadtxt(data, unpack=True, usecols=[1])/2
z = loadtxt(data, unpack=True, usecols=[2])


fig = plt.figure()
ax = fig.gca(projection='3d')

xi = np.linspace(min(x), max(x))
yi = np.linspace(min(y), max(y))

X, Y = np.meshgrid(xi, yi)
Z = griddata(x, y, z, X, Y)

ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.3, linewidth = 0.2)
cset = ax.contourf(X, Y, Z, zdir='z', offset=0.0, cmap=cm.coolwarm)
#cset = ax.contourf(X, Y, Z, zdir='x', offset=-9, cmap=cm.coolwarm)
#cset = ax.contourf(X, Y, Z, zdir='y', offset=9, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-5,5)
ax.set_ylabel('Y')
ax.set_ylim(-5,5)
ax.set_zlabel('Z')
#ax.set_zlim(0,1.2)

plt.show()
