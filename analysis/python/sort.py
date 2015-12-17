"""
Interpolate SiO2_d_rot so that it has 289 data points instead of 81
"""
from pylab import *
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
#from matplotlib.mlab import griddata
from scipy.interpolate import griddata
data1 = 'output'
data2 = 'SiO2_d_rot'
x = loadtxt(data1, unpack=True, usecols=[0])/2
y = loadtxt(data1, unpack=True, usecols=[1])/2
x2 = loadtxt(data2, unpack=True, usecols=[0])
y2 = loadtxt(data2, unpack=True, usecols=[1])
z = loadtxt(data1, unpack=True, usecols=[2])
z2 = loadtxt(data2, unpack=True, usecols = [2])


fig = plt.figure()
ax = fig.gca(projection='3d')

points = []
for i in range (0, len(x2)):
    points.append([x2[i], y2[i]])

xi = np.linspace(min(x), max(x), 17)
yi = np.linspace(min(y), max(y), 17)

X, Y = np.meshgrid(xi, yi)
Z2 = griddata(points, z2, (X, Y), method = 'cubic')


SiO2 = []
ZnO = []
for i in range (0, len(Z2)):
    for j in range(0, len(Z2)):
        SiO2.append([xi[i], yi[j], Z2[i][j]])

for i in range (0, len(z)):
    ZnO.append([x[i], y[i], z[i]])

SiO2_sorted = sorted(SiO2, key = lambda x: x[0])
ZnO_sorted = sorted(ZnO, key = lambda x: (x[0], x[1]))

A = list(SiO2_sorted)
B = list(ZnO_sorted)

# write data to columns in text file
savetxt('SiO2_sorted.txt', A)
savetxt('ZnO_sorted.txt', B)

ax.plot_surface(X, Y, Z2, rstride=1, cstride=1, alpha=0.3, linewidth = 0.2)
#cset = ax.contourf(X, Y, Z2, zdir='z', offset=0.0, cmap=cm.coolwarm)
#cset = ax.contourf(X, Y, Z, zdir='x', offset=-9, cmap=cm.coolwarm)
#cset = ax.contourf(X, Y, Z, zdir='y', offset=9, cmap=cm.coolwarm)



ax.set_xlabel('X')
ax.set_xlim(-5,5)
ax.set_ylabel('Y')
ax.set_ylim(-5,5)
ax.set_zlabel('Z')
#ax.set_zlim(0,1.2)

plt.show()
