from pylab import *
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.mlab import griddata
from matplotlib.colors import LogNorm

data1 = 'mob.txt'

x = loadtxt(data1, unpack=True, usecols=[0])/2
y = loadtxt(data1, unpack=True, usecols=[1])/2
z = loadtxt(data1, unpack=True, usecols=[2])
mob = []

fig = plt.figure(figsize=(10,9.6))
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111)

for i in range (0, len(x)):
    mob.append([x[i], y[i], z[i]])

mob_sort = sorted(mob, key = lambda x: (x[0], x[1]))

mob_list = list(mob_sort)
savetxt('mob_sorted.txt', mob_list)

plt.show()
