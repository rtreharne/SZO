from pylab import *
import matplotlib.pyplot as plt


def open_files():
    data = '38c_fit_2.txt'
    data2 = '38c_nk.txt'
    data3 = 'Noutput.txt'
    x = loadtxt(data, unpack = True, usecols=[0])
    a = loadtxt(data, unpack = True, usecols=[1])
    b = loadtxt(data, unpack = True, usecols=[2])
    c = loadtxt(data, unpack = True, usecols=[3])
    d = loadtxt(data, unpack = True, usecols=[4])
    e = loadtxt(data, unpack = True, usecols=[5])
    f = loadtxt(data, unpack = True, usecols=[6])
    g = loadtxt(data, unpack = True, usecols=[7])
    h = loadtxt(data, unpack = True, usecols=[8])
    
    x2 = loadtxt(data2, unpack = True, usecols = [0])
    x3 = loadtxt(data3, unpack = True, usecols = [0])
    k1 = loadtxt(data2, unpack = True, usecols = [2])
    k2 = loadtxt(data3, unpack = True, usecols = [2])

    return x, (a, b, c, d, e, f, g, h), (x2, k1), (x3, -k2)

def plot_graph():
    x, data, data2, data3 = open_files()
    fig = figure(figsize=(9, 9))
    ax = fig.add_subplot(211)
    ax2 = ax.twinx()
    ax3 = fig.add_subplot(212)
    #ax4 = ax3.twinx()
    
    
    l1, = ax.plot(x, data[0], 'o', color = 'red') #65 Psi data
    l2, = ax2.plot(x, data[1], 'o', color = 'green') # 65 Delta data
    l3, = ax.plot(x, data[2], '--', color = 'red') #65 Psi fit
    l4, = ax2.plot(x, data[3], '--', color = 'green') # 65 Delta fit

    l5, = ax.plot(x, data[4], '^', color = 'red') # 70 Psi data
    l6, = ax2.plot(x, data[5], '^', color = 'green') # 70 Delta data
    l7, = ax.plot(x, data[6], '--', color = 'red') #70 Psi fit
    l8, = ax2.plot(x, data[7], '--', color = 'green') #70 Delta fit
    #ax.set_ylim(0, 20)
    ax.set_xlim(310, 413)

    eV1 = (6.63e-34*3e8)/(data2[0]*1e-9*1.602e-19)
    eV2 = (6.63e-34*3e8)/(data3[0]*1e-9*1.602e-19)
    alpha1 = ((4*pi*data2[1])/(data2[0]*1e-7))
    alpha2 = ((4*pi*data3[1])/(data3[0]*1e-7))
    l9, = ax3.plot(eV1, alpha1, 'o')
    l10, = ax3.plot(eV2, alpha2, '^')
    print len(eV2), len(alpha2)
    ax3.set_xlim(3, 4)
    #ax4.set_ylim(0, 1e14)
    #ax3.set_yscale('log')


if __name__ == "__main__":
    plot_graph()
    show()
