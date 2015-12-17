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
z = loadtxt(data1, unpack=True, usecols=[2])
n = []

fig = plt.figure(figsize=(10,9.6))
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111)

for i in range (0, len(x)):
    n.append([x[i], y[i], z[i]])

n_sort = sorted(n, key = lambda x: (x[0], x[1]))

n_list = list(n_sort)
savetxt('n_sorted.txt', n_list)

plt.show()
