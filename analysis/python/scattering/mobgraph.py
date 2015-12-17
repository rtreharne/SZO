"""
Plot graph from data "rs.txt"
"""
from pylab import *
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.mlab import griddata

datars = 'rs.txt'
xrs = loadtxt(datars, unpack=True, usecols=[0])/10
yrs = loadtxt(datars, unpack=True, usecols=[1])/10
zrs= loadtxt(datars, unpack=True, usecols=[2])*4.93

datad = 'd.txt'
zd = loadtxt(datad, unpack = True, usecols=[2])

datan = 'pfton.txt'
zn = loadtxt(datan, unpack=True, usecols=[2])/1e6

rho = zrs*zd*1e-7

mob = 1/(zn*1.602e-19*rho)

fig = plt.figure()
ax = fig.gca(projection='3d')

xi = np.linspace(min(xrs), max(xrs))
yi = np.linspace(min(yrs), max(yrs))

X, Y = np.meshgrid(xi, yi)
Z = griddata(xrs, yrs, mob, X, Y)

ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.3, linewidth = 0.2)
cset = ax.contourf(X, Y, Z, zdir='z', offset=0.0, cmap=cm.coolwarm)
#cset = ax.contourf(X, Y, Z, zdir='x', offset=-9, cmap=cm.coolwarm)
#cset = ax.contourf(X, Y, Z, zdir='y', offset=9, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-5,5)
ax.set_ylabel('Y')
ax.set_ylim(-5,5)
ax.set_zlabel('Z')
#ax.set_zlim(0,0.01)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

x = []
y = []
for i in range(0, len(zn)):
    x.append(zn[i])
    y.append(mob[i])
ax2.plot(x,y, '-', color = 'red', alpha = 0.5)
#ax2.set_ylim([0,30])
#ax2.set_xscale('log')

plt.show()
