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


data1 = 'ZnO_sorted.txt'
data2 = 'SiO2_sorted.txt'



x = loadtxt(data1, unpack=True, usecols=[0])
y = loadtxt(data1, unpack=True, usecols=[1])
z1 = loadtxt(data1, unpack=True, usecols=[2])
x2 = loadtxt(data2, unpack=True, usecols=[0])
y2 = loadtxt(data2, unpack=True, usecols=[1])
z2 = loadtxt(data2, unpack = True, usecols = [2])
print x2

z3 = []
A = 60.08
B = 81.408
for i in range (0, len(x)):
    z3.append(((A*z2[i])/(A*z2[i]+B*z1[i]))*100)

fig = plt.figure(figsize=(7,5))
fig.patch.set_alpha(0.0)
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111)
ax.set_aspect('equal')
ax.patch.set_alpha(0.0)
#ax.axis('off')

xi = np.linspace(min(x), max(x))
yi = np.linspace(min(y), max(y))

X, Y = np.meshgrid(xi, yi)
Z = griddata(x, y, z1, X, Y)
Z2 = griddata(x2, y2, z2, X, Y)
Z3 = griddata(x, y, z3, X, Y)
lvls = arange(0, 45,5)
ax.set_xticklabels([])
ax.set_yticklabels([])
#ax.plot_surface(X, Y, Z, rstride=100, cstride=100, alpha=0.3, linewidth = 0.2)
#CS = ax.contour(X, Y, Z2,  colors = '#ef442a', linestyles = 'dashed', linewidths = 2, levels = lvls2, fontsize = 30)
#CS2 = ax.contour(X, Y, Z2, colors = '#ef442a', levels = lvls3, linewidths = 4 )
plot1 = ax.contourf(X,Y,Z2, cmap =cm.jet, levels = lvls)
#ax.clabel(CS, fmt = '%2.2f', fontsize = 20)
#ax.clabel(CS2, fmt = '%2.2f', fontsize = 24)
#cset = ax.contourf(X, Y, Z, zdir='x', offset=-9, cmap=cm.coolwarm)
#cset = ax.contourf(X, Y, Z, zdir='y', offset=9, cmap=cm.coolwarm)
cbar = colorbar(plot1, ticks = lvls)
cbar.set_label("SiO$_2$ thickness (nm)", fontsize = 24)

ax.set_xlabel('', fontsize = 24)
ax.set_ylabel('', fontsize = 24)
#ax.set_zlabel('Z')
plt.show()
