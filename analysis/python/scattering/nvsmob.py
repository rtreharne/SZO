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

data_hall = 'nvsmob_hall.txt'
hall_n = loadtxt(data_hall, unpack=True, usecols=[0])
hall_nerr = loadtxt(data_hall, unpack = True, usecols = [1])
hall_mob = loadtxt(data_hall, unpack = True, usecols = [2])
hall_moberr = loadtxt(data_hall, unpack = True, usecols = [3])

rho = zrs*zd*1e-7

mob = 1/(zn*1.602e-19*rho)

x = []
y = []
for i in range(0, len(zn)):
    x.append(zn[i])
    y.append(mob[i])
#ax2.plot(x,y, '-', color = 'red', alpha = 0.5)
#ax2.set_ylim([0,30])
#ax2.set_xscale('log')

c = []
d = []
for i in range (0, 16):
    a = []
    b = []
    minz = []
    for j in range (0, len(xrs)):
        if xrs[j] == xrs[i]:
            a.append((xrs[j]))
            b.append((yrs[j]))
            minz.append(zn[j])
            index = minz.index(max(minz))
    c.append(a[index])
    d.append(b[index])

coeff = polyfit(c, d, 1)
print coeff
#p = poly1d( coeff )
#x = linspace(-5, 5, 100)

#fig3 = plt.figure()
#ax3 = fig3.add_subplot(111)

redx, redy = [], []
greenx, greeny = [], []
for i in range (len(xrs)):
    if (xrs[i]+yrs[i])<(xrs[i]+coeff[0]*xrs[i]+(coeff[1])):
        redx.append(zn[i])
        redy.append(mob[i])
    else:
        greenx.append(zn[i])
        greeny.append(mob[i])

#ax3.plot(redx, redy, 'o', color = 'red', alpha = 1)
#ax3.plot(greenx, greeny, 'o', color = 'green', alpha = 0.8)
#ax3.set_xlabel('$n_{e}$ (cm$^{-3}$)', fontsize = 16)
#ax3.set_xscale('log')
#ax3.set_ylabel('$\mu_{e}$ (cm$^{2}$V$^{-1}$s$^{-1}$)', fontsize = 16)

#ax3.errorbar(hall_n, hall_mob, xerr=hall_nerr, #yerr=hall_moberr, fmt = 'bo')

def mob():
    file = open('newdata.txt', 'w')
    for i in range (0, len(redx)):
        file.write('{0} {1}\n'.format(redx[i], redy[i]))
    return(redx, redy, greenx, greeny)


#plt.show()


