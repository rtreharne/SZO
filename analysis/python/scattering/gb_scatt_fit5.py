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
        self.x = arange(1e19, 5e20, 1e18)
        self.ax = subplot(111)

        self.xdata, self.ydata, self.greenx, self.greeny= nvsmob.mob()


        p = ([40, 17, 40, 44])

        p = self.fit(p)

        mu1, mu2 = self.crunch(p)
        self.update(self.x, mu1, mu2)
        print p

    def crunch(self, p):
        self.index = 0
        x = self.x
        L = p[0]*1e-7
        Nt = p[1]*1e13
        A = p[2]
        B = p[3]/100
        mumax = 30.0


        Ef = hbar**2*(3*pi**2*x*1e6)**(2.0/3)/(2*m)
        Eb = e**2*Nt**2/(8*8.4*e0*x)
        mu0 = e*L/sqrt(2*pi*m*kT)
        print 'mu0=', mu0
        mu1 = mu0*exp(-Eb/kT)
        mu2 = mu1*(1+exp(-(A/e)*(Eb-Ef+(B*e))))
        mu_tot = ((1/mu2)+(1/mumax))**(-1)
        return mu_tot, mu1

    def update(self, x, mu1, mu2):
        sigma = 1e-20

        for i in range (0,len(x)):
            x[i] = sigma*x[i]

        for i in range (0,len(self.xdata)):
            self.xdata[i] = sigma*self.xdata[i]
            self.greenx[i] = sigma*self.greenx[i]

        self.ax.clear()
        data1, = self.ax.plot(self.xdata, self.ydata, 'o', color = 'red', alpha = 0.7, markersize = 8)
        #data2, = self.ax.plot(self.greenx, self.greeny, '^', color = 'green', alpha = 0.7, markersize = 8)
        #self.ax.plot(self.greenx, self.greeny, 'o', color = 'green')
        line1, = self.ax.plot(x, mu1, '-', linewidth = 2, color = 'blue')
        line2, = self.ax.plot(x, mu2, '--', linewidth = 2, color = 'green')
        self.ax.set_ylim(0, 20)
        self.ax.set_ylabel(r'$\mu_e$ (cm$^2$V$^{-1}$s$^{-1}$)', fontsize = 15)
        self.ax.set_xlim(0.5, 5)
        self.ax.set_xlabel(r'$n_e$ ($\times10^{20}$ cm$^{-3}$)', fontsize = 15)
        #self.ax.set_xscale('log')
 
        fontP = FontProperties()
        fontP.set_size('large')
        leg1 = self.ax.legend((data1, line2, line1), ('data ($\leq 0.65 \%$ wt. SiO$_{2}$)',r'Seto', r'Extended model'), 'upper left', prop = fontP,fancybox=False)
        leg1.get_frame().set_alpha(0.0)

    def func(self, p):
        sum = 0
        x = self.xdata
        y = self.ydata
        L = p[0]*1e-7
        Nt = p[1]*1e13
        A = p[2]
        B = p[3]/100
        mumax = 30.0
        mu0 = e*L/sqrt(2*pi*m*kT)
        Eb, Ef, mu1, mu2, mu3 = [],[],[],[], []
        for i in range (0, len(x)):
            Eb.append(e**2*Nt**2/(8*8.4*e0*x[i]))
            Ef.append(hbar**2*(3*pi**2*x[i]*1e6)**(2.0/3)/(2*m))
            mu1.append(mu0*exp(-Eb[i]/kT))
            mu2.append(mu1[i]*(1+exp(-(A/e)*(Eb[i]-Ef[i]+(B*e)))))
            mu3.append(((1/mu2[i])+(1/mumax))**(-1))
            sum += (mu3[i]-y[i])**2
        sum = sum/len(x)
        return sum

    def fit(self, p):
        for i in range (0, 20):
            result, fx, conv_flag, nfe, res = nelmin.minimize(self.func, p)
            p = result
        return result

       

graph = Page()
show()
