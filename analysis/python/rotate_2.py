from pylab import *
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.mlab import griddata as grid
from scipy.interpolate import griddata as interp
from matplotlib.widgets import Slider

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
        self.fig = figure(figsize=(8,4))
        self.ax = self.fig.add_subplot(111)
        subplots_adjust(bottom=0.25)
        axtheta = axes([0.25,0.1,0.65,0.03])
        self.stheta = Slider(axtheta, 'theta', -180, 180, valinit = -12)
        self.stheta.on_changed(self.xy)

        self.fig2 = figure(figsize=(5,8))
        self.ax2 = self.fig2.add_subplot(211)


        

        

    def xy(self, widget):
        self.ax.clear()
        self.ax2.clear()
        theta = -18
        A = profile1.rot(theta)
        B = profile2.grid()
        C = A[0], A[1], (2.65*A[2]/(2.65*A[2]+5.61*B[2]))*100
        D = profile3.grid()
        x, y = C[2], D[2]
        self.ax.plot(x, y, 'o', color = 'red', alpha = 0.5)
        self.ax.set_xlim(0, 6)
        self.ax.set_ylim(0, 5e26)

        u = np.linspace(0, 2, 100)
        v = (u/100)*6.02e29*5.61*2/60.08
        w = v/2

        self.ax.plot(u, v, w, '-')
        self.ax.plot(u, w, '-')
        
        newa = []
        newb =[] 
        newc= []
        for i in range (len(A[0])):
            for j in range (len(A[0])):
                newa.append(A[0][i][j])
                newb.append(A[1][i][j])
                newc.append(C[2][i][j])
                
        export = (newa, newb, newc)
        savetxt('comp_prof.txt', transpose(export))
        

        levels = [0,0.1,0.2,0.4,1,2,4,6]
        CS = self.ax2.contour(A[0], A[1], C[2], levels, colors = 'black', linestyles = 'dashed')

        self.ax2.clabel(CS, fmt = '%2.1f', colors = 'black')

        levels = [0.58]
        CS2 = self.ax2.contour(A[0], A[1], C[2], levels, colors = 'black', linewidths = 2)
        self.ax2.clabel(CS2, fmt = '%2.2f', colors = 'black', fontsize =14, style = 'bold')
        print len(A[0]), len(D[2])
        
        x, y, z = [], [], []
        for i in range (0, len(A[0])):
            for j in range (0, len(A[0][0])):
                x.append(A[0][i][j])
                y.append(A[1][i][j])
                z.append(D[2][i][j]/1e6)

        #print len(x), len(y), len(z)


        xi = np.linspace(min(x), max(x),100)
        yi = np.linspace(min(y), max(y),100)
        X, Y = np.meshgrid(xi, yi)
        Z = griddata(x,y,z, X, Y)
        
        CF = self.ax2.contourf(X,Y,Z,50, cmap = cm.spectral, alpha = 0.6)
        self.ax2.set_xlabel('x (cm)', fontsize = 14)
        self.ax2.set_ylabel('y (cm)', fontsize = 14)
        cbar = self.fig2.colorbar(CF, spacing = 'proportional', orientation = 'vertical', ticks = [1e20, 1.5e20, 2e20, 2.5e20, 3e20, 3.5e20,4e20])
        cbar.set_label('$n_e$ (cm$^{-3}$)', fontsize = 14)
        l,b,w,h = cbar.ax.get_position().bounds
        cbar.ax.set_position([0.83,0.55,0.1,0.4])
        self.ax2.set_position([0.12, 0.55, 0.82,0.42])

        cbar2 = self.fig2.colorbar(CF, spacing = 'proportional', orientation = 'vertical', ticks = [1e20, 1.5e20, 2e20, 2.5e20, 3e20, 3.5e20,4e20])
        cbar2.ax.set_position([0.83,0.05,0.1,0.4])

        
        


profile1 = Rotate('SiO2_sorted.txt')
profile2 = Rotate('ZnO_sorted.txt')
profile3 = Rotate('n_sorted.txt')
plot1 = Plot()
plot1.xy(None)

show()


        
        
