from pylab import *
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.mlab import griddata
from matplotlib.colors import LogNorm
import matplotlib as m
from matplotlib.font_manager import FontProperties
matplotlib.rc('xtick', labelsize = 24)
matplotlib.rc('ytick', labelsize = 24, )


data1 = 'pfton.txt'
data2 = 'comp_prof.txt'



x = loadtxt(data1, unpack=True, usecols=[0])/2
y = loadtxt(data1, unpack=True, usecols=[1])/2
z = loadtxt(data1, unpack=True, usecols=[2])/1e26
x2 = loadtxt(data2, unpack=True, usecols=[0])
y2 = loadtxt(data2, unpack=True, usecols=[1])
z2 = loadtxt(data2, unpack = True, usecols = [2])
print x2

fig = plt.figure(figsize=(7,5))
fig.patch.set_alpha(0.0)
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111)
ax.set_aspect('equal')
ax.patch.set_alpha(0.0)

xi = np.linspace(min(x), max(x))
yi = np.linspace(min(y), max(y))

X, Y = np.meshgrid(xi, yi)
Z = griddata(x, y, z, X, Y)
Z2 = griddata(x2, y2, z2, X, Y)
lvls = arange(0, 5.5, 0.5)
lvls2 = (0.1, 0.2, 0.3, 0.4, 0.5, 1, 2, 4, 6)
lvls3 = (0.65, 20)
#ax.plot_surface(X, Y, Z, rstride=100, cstride=100, alpha=0.3, linewidth = 0.2)
#CS = ax.contour(X, Y, Z2,  colors = 'black', linestyles = 'dashed', linewidths = 2, levels = lvls2)
#CS2 = ax.contour(X, Y, Z2, colors = 'black', levels = lvls3, linewidths = 4 )
plot1 = ax.contourf(X,Y,Z, cmap =cm.jet, levels = lvls)
#ax.clabel(CS, fmt = '%2.2f', fontsize = 18)
#ax.clabel(CS2, fmt = '%2.2f', fontsize = 22)
#cset = ax.contourf(X, Y, Z, zdir='x', offset=-9, cmap=cm.coolwarm)
#cset = ax.contourf(X, Y, Z, zdir='y', offset=9, cmap=cm.coolwarm)
cbar = colorbar(plot1, ticks = lvls)
cbar.set_label(r"$n$ ($\times 10^{20}$cm$^{-3}$)", fontsize = 26)

ax.set_xticklabels([])
ax.set_yticklabels([])

ax.set_xlabel('', fontsize = 24)
ax.set_ylabel('', fontsize = 24)
#ax.set_zlabel('Z')
plt.show()
