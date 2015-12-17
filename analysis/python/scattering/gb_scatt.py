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

class Page:
    fig = figure(figsize = (14, 7))
    subplots_adjust(bottom=0.35)
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

        self.xdata, self.ydata = nvsmob.mob()

        slider1 = axes([0.25, 0.25, 0.65, 0.04])
        self.sL = Slider(slider1, 'L (cm)', 0, 100, valinit = 30)

        slider2 = axes([0.25,0.2,0.65,0.030])
        self.sNt = Slider(slider2, '$N_{t}$ (cm$^{-2}$)', 0, 100, valinit = 20)

        slider3 = axes([0.25,0.15,0.65,0.030])
        self.sNc = Slider(slider3, '$N_{c}$', 0, 50, valinit = 1)
  
        slider4 = axes([0.25,0.1,0.65,0.030])
        self.sgamma = Slider(slider4, '$\gamma$', 0, 100, valinit = 10)

        slider5 = axes([0.25, 0.05, 0.65, 0.030])
        self.sA = Slider(slider5, 'A', 0, 1000, valinit = 10)


        openit = axes([0.05, 0.05, 0.1, 0.04])
        self.openbut = Button(openit, 'Open', hovercolor = '0.5')

        self.crunch(self)

        self.sL.on_changed(self.crunch)
        self.sNt.on_changed(self.crunch)
        self.sNc.on_changed(self.crunch)
        self.sgamma.on_changed(self.crunch)
        self.sA.on_changed(self.crunch)

    def crunch(self, widget):
        mumax = 50
        A = self.sA.val
        x = self.x
        L = self.sL.val*1e-7
        Nt = self.sNt.val*1e13
        Nc = self.sNc.val*1e20
        gamma = self.sgamma.val/e 
        mu0 = e*L/sqrt(2*pi*m*kT)
        Eb = e**2*Nt**2/(8*8.4*e0*x)
        Ef = hbar**2*(3*pi**2*x*1e6)**(2.0/3)/(2*m)
        mueff = mu0*exp(-Eb/kT)
        #mutunn = ii-ii/(1+exp(-(Nc/x)))
        mu3 = (mumax - mu0)/(1+exp(-gamma*(Ef - A*Eb)))
        mu4 = mueff+mu3
        #sum = mueff+mutunn
        self.update(x, mueff, mu3, mu4)


    def update(self, x, mueff, mu3, mu4):
        self.ax.clear()
        self.ax.plot(x, mueff)
        #self.ax.plot(x, mutunn)
        self.ax.plot(self.xdata, self.ydata, 'o', color = 'red')
        #self.ax.plot(x, sum)
        self.ax.plot(x, mu3)
        self.ax.plot(x, mu4)
        #self.ax.set_xscale('log')
        #self.ax.set_ylim(0, 18)
        #self.ax.set_xlim(5e19, 5e20)
        
    
       

graph = Page()
show()
