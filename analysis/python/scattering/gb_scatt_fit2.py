#! /usr/bin/env python

from numpy import *
from pylab import *
from math import *
from pylab import *
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import tkFileDialog
import numpy as np
import nvsmob
import nelmin
from matplotlib.font_manager import FontProperties
#matplotlib.rc('xtick', labelsize = 15)
#matplotlib.rc('ytick', labelsize = 15, )

class Page:
    fig = figure(figsize = (6,5))
    #subplots_adjust(bottom=0.35)
    global e, m0, e0, hbar, k, T, kT, m
    e = 1.602e-19
    e0 = 8.85e-12
    m0 = 9.11e-31
    hbar = 1.055e-34
    k = 1.38e-23
    T = 300
    kT = k*T
    m = 0.4*m0

    def __init__(self):
        self.x = arange(1e19, 1e21, 1e18)
        self.ax = subplot(111)

        self.xdata, self.ydata, self.greenx, self.greeny= nvsmob.mob()


        p = ([50, 1.8, 9.25, 10])

        p = self.fit(p)

        mu_total, mu1, mu2 = self.crunch(p)
        
        p[1] = 0.9*p[1]
        munew, mu3, mu4 = self.crunch(p)
        self.update(self.x, mu_total, mu1, mu2, munew)
        print p

    def crunch(self, p):
        self.index = 0
        mumax = 50
        x = self.x
        L = p[0]*1e-7
        Nt = p[1]*1e14
        A = p[2]/e
        B = p[3]
        Er = self.renorm(self.x)*e
        mu0 = e*L/sqrt(2*pi*m*kT)
        Eb = e**2*Nt**2/(8*8.4*e0*x)
        Ef = hbar**2*(3*pi**2*x*1e6)**(2.0/3)/(2*m)
        mu1 = mu0*exp(-Eb/kT)
        mu2 = (mumax - mu0)/(1+exp(-A*(Ef -Er- B*Eb)))
        mu_total = mu1+mu2
        return mu_total, mu1, mu2

    def update(self, x, mu_total, mu1, mu2, newmu):
        sigma = 1e-20

        for i in range (0,len(x)):
            x[i] = sigma*x[i]

        for i in range (0,len(self.xdata)):
            self.xdata[i] = sigma*self.xdata[i]
            self.greenx[i] = sigma*self.greenx[i]

        self.ax.clear()
        line3, = self.ax.plot(x, mu_total, linewidth = 3, alpha = 0.75)
        data1, = self.ax.plot(self.xdata, self.ydata, 'o', color = 'red', alpha = 0.75, markersize = 5)
        data2, = self.ax.plot(self.greenx, self.greeny, 'o', color = 'green', alpha = 0.75, markersize = 5)
        #self.ax.plot(self.greenx, self.greeny, 'o', color = 'green')
        line1, = self.ax.plot(x, mu1, '--', linewidth = 2, color = 'orange')
        line2, = self.ax.plot(x, mu2, '-', linewidth = 2, color = 'purple')
        line2.set_dashes([8, 4, 2, 4, 2, 4]) 
        #self.ax.set_xscale('log')
        self.ax.set_ylim(0, 50)
        self.ax.set_ylabel(r'$\mu_e$ (cm$^2$V$^{-1}$s$^{-1}$)', fontsize = 15)
        self.ax.set_xlim(0.5, 5)
        self.ax.set_xlabel(r'$n_e$ ($\times10^{20}$ cm$^{-3}$)', fontsize = 15)
        #self.ax.set_xscale('log')
 
        fontP = FontProperties()
        fontP.set_size('large')
        leg1 = self.ax.legend((data1,data2,line1, line2,line3), (r'data ($< 0.65\%$ wt. SiO$_{2}$)',r'data ($>0.65\%$ wt. SiO$_{2}$)',r'$\mu_{gb}=\mu_0\exp(-\frac{\phi}{k_BT})$', r'$\mu_t=\frac{\mu_{ii}-\mu_{gb}}{1+\exp[-\alpha(E_f-\beta\phi)]}$',r'$\mu_{eff}=\mu_{gb} + \mu_t$'), 'upper left', prop = fontP,fancybox=False)
        leg1.get_frame().set_alpha(0.0)
        
        l4, = self.ax.plot(x, newmu)

     

    def func(self, p):

        for i in range (0, len(p)):
            p[i] = sqrt((p[i])**2)
        sum = 0
        x = self.xdata
        y = self.ydata
        mumax = 50
        L = p[0]*1e-7
        Nt = p[1]*1e14
        A = p[2]/e
        B = p[3]
        mu0 = e*L/sqrt(2*pi*m*kT)
        Eb, Ef, mu1, mu2, mu_total = [],[],[],[],[]
        Er = self.renorm(x)*e
        for i in range (0, len(x)):
            Eb.append(e**2*Nt**2/(8*8.4*e0*x[i]))
            Ef.append(hbar**2*(3*pi**2*x[i]*1e6)**(2.0/3)/(2*m))
            mu1.append(mu0*exp(-Eb[i]/kT))
            mu2.append((mumax - mu0)/(1+exp(-A*(Ef[i] - Er[i] - B*Eb[i]))))
            mu_total.append(mu1[i] + mu2[i])
            self.mu_total = mu_total
            sum += sqrt((mu_total[i]-y[i])**2)
        sum = sum/len(x)
        return sum

    def fit(self, p):
        for i in range (0, 5):
            result, fx, conv_flag, nfe, res = nelmin.minimize(self.func, p)
            for j in range (0, len(p)):
                p[j] = sqrt((p[j])**2)
            p = result
            self.p = p
        return result

    def renorm(self, x):
        x = transpose(x)
        A = 17.96e24
        B = 4.23e24
        C = 0.0075e24
        
        E1 = (x/A)**(1.0/3)
        E2 = (x/B)**(1.0/4)
        E3 = (x/C)**(1.0/2)

        Er = E1+E2+E2

        return Er

    

       

graph = Page()
show()
