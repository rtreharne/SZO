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

data1 = 'SiO2_wt.txt'
data2 = 'n_sorted.txt'


x = loadtxt(data1, unpack=True, usecols=[2])
y = loadtxt(data2, unpack=True, usecols=[2])

print x

fig = plt.figure(figsize=(10,9.6))
ax = fig.add_subplot(111)

ax.plot(x,y, 'o')
plt.show()
