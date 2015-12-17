from numpy import *
from random import randint
from pylab import *
from math import *
import tkFileDialog



global e, e0, m0, hbar, me, C
e = 1.602e-19
e0 = 8.85e-12
m0 = 0.35*9.11e-31
hbar = 1.055e-34

C = 0.30/e

class Calc:
    def __init__(self):
        filename = 'output.txt'
        self.x = loadtxt(filename, unpack = True, usecols=[0])
        self.y = loadtxt(filename, unpack = True, usecols=[1])
        self.w = loadtxt(filename, unpack = True, usecols=[3])*2*pi*2.418e14 #Convert to rad/sec

    def crunch(self):
        w = self.w
        self.n = []
        self.m = []
        print max(w)
        
        for i in range (0,len(self.x)):
            p = 0
            n0 = w[i]**2*m0*e0/e**2
            A = w[i]
            mstar0 = m0*sqrt(1+(((2*C*hbar**2)/(2*m0))*(3*pi**2*n0)**(2.0/3)))
            B = sqrt((n0*e**2)/(mstar0*e0))
            while p<20:
                if B < A:
                    n1 = n0
                    mstar1 = mstar0
                    n0 += (n0/2**p)
                    mstar0 = m0*sqrt(1+(((2*C*hbar**2)/(2*m0))*(3*pi**2*n0)**(2.0/3)))
                    B = sqrt((n0*e**2)/(mstar0*e0))

                else:
                    p += 1
                    n0 = n1
                    mstar0 = mstar1
                    n0 += (n0/2**p)
                    mstar0 = m0*sqrt(1+(((2*C*hbar**2)/(2*m0))*(3*pi**2*n0)**(2.0/3)))
                    B = sqrt((n0*e**2)/(mstar0*e0))
            self.n.append(n0)
            self.m.append(mstar0/9.11e-31)
        return self.x, self.y, self.n, self.m

    def save(self, x, y, n, m):
        filename = 'pfton.txt'
        output = (x, y, n, m)
        output = transpose([output])
        savetxt(filename, output)
        print 'File "pfton.txt" has been saved'

        
A = Calc()
x, y, n, m = A.crunch()
A.save(x,y,n,m)
print max(m)




    
