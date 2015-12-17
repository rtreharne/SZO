from pylab import *
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.mlab import griddata as grid
from scipy.interpolate import griddata as interp
from matplotlib.widgets import Slider
matplotlib.rc('xtick', labelsize = 20)
matplotlib.rc('ytick', labelsize = 20, )
class Rotate():
    def __init__(self, data):
        self.x = loadtxt(data, unpack = True, usecols = [0])
        self.y = loadtxt(data, unpack = True, usecols = [1])
        self.z = loadtxt(data, unpack = True, usecols = [2])

    def grid(self):
        x = self.x
        y = self.y
        z = self.z

        xi = np.linspace(min(x), max(x), 17)
        yi = np.linspace(min(y), max(y), 17)
     
        X, Y = np.meshgrid(xi, yi)
        Z = grid(x, y, z, X, Y)
        
        return X, Y, Z

    def rot(self, theta):

        theta = theta*pi/180
        x = self.x
        y = self.y
        z = self.z

        x_rot = x*cos(theta) + y*sin(theta)
        y_rot = -x*sin(theta) + y*cos(theta)

        xi = np.linspace(min(x), max(x), 17)
        yi = np.linspace(min(y), max(y), 17)

        
        X, Y = np.meshgrid(xi, yi)
        points = x_rot, y_rot
        Z = interp(points, z, (X, Y), method = 'cubic')

        return X, Y, Z
        
class Plot():
    def __init__(self):
        self.fig = figure(figsize=(6,12))
        self.fig.patch.set_alpha(1)
        self.ax1 = self.fig.add_subplot(311)
        self.ax2 = self.fig.add_subplot(312)
        self.ax3 = self.fig.add_subplot(313)
        subplots_adjust(hspace =  0.0, left = 0.17, bottom = 0.09, right = 0.95, top = 0.95)


    def xy(self, widget):
        theta = -25
        A = profile1.rot(theta)
        B = profile2.grid()
        C = A[0], A[1], (2.65*A[2]/(2.65*A[2]+5.61*B[2]))*100
        D = profile3.grid()
        E = profile4.grid()
        x, y1, y2 = C[2], D[2], E[2]
        y3 = 1/(D[2]*E[2]*1.602e-19*1e-6)
        self.ax1.plot(x, y1*1e-26, 'o', color = '#ee5038', alpha = 0.7, markersize = 15)
        self.ax1.set_xlim(0, 6)
        self.ax1.set_ylim(0, 5.5)
        self.ax1.set_yticks([0,1,2,3,4,5])
        self.ax1.xaxis.tick_top()
        self.ax1.set_ylabel('$n_{e}$ (x10$^{20}$ cm$^{-3}$)', fontsize = 20)
  

        self.ax2.plot(x, y2, 'o', color = '#01a79d', alpha = 0.7, markersize = 15)
        self.ax2.set_xlim(0, 6)
        self.ax2.set_ylim(0,18)
        self.ax2.set_yticks([0,5,10,15])
        setp(self.ax2.get_xticklabels(), visible=False)
        self.ax2.set_ylabel('$\mu$ (cm$^2$V$^{-1}$s$^{-1}$)', fontsize = 20)

        self.ax3.plot(x, y3, 'o', color = '#259eb1', alpha = 0.7, markersize = 15)
        self.ax3.set_xlim(0, 6)
        #setp(self.ax3.get_yticklabels(), rotation=45)
        self.ax3.set_ylim(1e-4, 0.5)
        self.ax3.set_yscale('log')
        #self.ax3.set_ylim(0,17)y
        self.ax3.set_xlabel('% wt. SiO$_{2}$ content', fontsize = 20)
        self.ax3.set_ylabel(r'$\rho$ ($\Omega$.cm)', fontsize=20)
        u = np.linspace(0, 2, 100)
        v = (u/100)*6.02e29*5.61*2*1e-26/60.08
        w = v/2

        self.ax1.plot(u, v, '-', linewidth=1.5, color = 'red')
        self.ax1.patch.set_alpha(1)
        self.ax2.patch.set_alpha(1)
        self.ax3.patch.set_alpha(1)
        




profile1 = Rotate('SiO2_sorted.txt')
profile2 = Rotate('ZnO_sorted.txt')
profile3 = Rotate('n_sorted.txt')
profile4 = Rotate('mob_sorted.txt')
plot1 = Plot()
plot1.xy(None)

show()


        
        
