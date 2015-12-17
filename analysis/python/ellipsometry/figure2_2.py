from pylab import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

matplotlib.rc('xtick', labelsize = 14)
matplotlib.rc('ytick', labelsize = 14)


def open_files():
    data = '38c_fit_2.txt'
    data2 = '38c_nk_2.txt'
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
    fig = figure(figsize=(11, 9))
    ax = fig.add_subplot(211)
    ax.text(3.05,5, '(a)', fontsize=16)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 18)
    ax2 = ax.twinx()
    ax2.tick_params(axis = 'both', which = 'major', labelsize = 18)
    ax3 = fig.add_subplot(212)
    ax3.tick_params(axis = 'both', which = 'major', labelsize = 18)
    #ax4 = ax3.twinx()
    subplots_adjust(bottom=None)
    ev0 = (6.63e-34*3e8)/(x*1e-9*1.602e-19)
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    setp(ax2.get_xticklabels(), visible=False)
    ax.set_ylim(-1, 22)
    ax2.set_ylim(-125, 175)
    ax.set_xlabel('$E$ (eV)', fontsize = 18)
    ax.set_ylabel('$\Psi$', fontsize = 18, rotation = -0)
    ax2.set_ylabel('$\Delta$', fontsize = 18, rotation = 0)
    
    
    l1, = ax.plot(ev0, data[0], 'o', color = 'red') #65 Psi data
    l2, = ax2.plot(ev0, data[1], 'o', color = 'green') # 65 Delta data
    l3, = ax.plot(ev0, data[2], '--', color = 'black') #65 Psi fit
    l4, = ax2.plot(ev0, data[3], '--', color = 'black') # 65 Delta fit

    l5, = ax.plot(ev0, data[4], '^', color = 'red') # 70 Psi data
    l6, = ax2.plot(ev0, data[5], '^', color = 'green') # 70 Delta data
    l7, = ax.plot(ev0, data[6], '--', color = 'black') #70 Psi fit
    l8, = ax2.plot(ev0, data[7], '--', color = 'black') #70 Delta fit
    #ax.set_ylim(0, 20)
    ax.set_xlim(3, 4)
    fontP = FontProperties()
    fontP.set_size('large')
    leg1 = ax.legend((l1, l2, l5, l6, l7), ('$\Psi (65^{\circ})$', '$\Delta (70^{\circ})$', '$\Psi (65^{\circ})$', '$\Delta (70^{\circ})$', 'model'), prop = fontP, fancybox = False, loc = 'lower right')
    leg1.get_frame().set_alpha(0.0)


    eV1 = (6.63e-34*3e8)/(data2[0]*1e-9*1.602e-19)
    eV2 = (6.63e-34*3e8)/(data3[0]*1e-9*1.602e-19)
    alpha1 = ((4*pi*data2[1])/(data2[0]*1e-7))/10000
    alpha2 = ((4*pi*data3[1])/(data3[0]*1e-7))/10000
    l9, = ax3.plot(eV1, alpha1, '-o')
    l10, = ax3.plot(eV2, alpha2, '-^')
    print len(eV2), len(alpha2)
    ax3.set_xlim(3, 4)
    ax3.set_ylim(-0.25, 24)
    ax3.text(3.17,12, 'exponential Urbach tail', fontsize = 16)
    ax3.text(3.05,5,'(b)',fontsize=16)
    newx = linspace(3.67, 3.67, 10)
    newy = linspace(0, 14.4, 10)
    l11, = ax3.plot(newx, newy, '--', color = 'blue')
    t2 = ax3.text(3.68, 12, '$E_G = 3.67$ eV', fontsize = 16, color = 'blue')
    newx2 = linspace(3.38, 3.38, 10)
    newy2 = linspace(0, 8, 10)
    l12, = ax3.plot(newx2, newy2, '--', color = 'green')
    t3 = ax3.text(3.2, 8, '$E_G = 3.38$ eV', fontsize = 16, color = 'green')

    newx3 = linspace(3.5, 3.5, 10)
    newy3 = linspace(7.4, 11, 10)
    l13, = ax3.plot(newx3, newy3, '-', color = 'black')
    leg2 = ax3.legend((l9, l10), ('ellipsometery', 'spectrophotometry'), prop = fontP, fancybox = False, loc = 'upper left')
    leg2.get_frame().set_alpha(0.0)
    ax3.set_xlabel('$E$ (eV)', fontsize = 18)
    
    ax3.set_ylabel(r'$\alpha$ $(\times10^4$ cm$^{-1})$', fontsize = 18)
    #ax4.set_ylim(0, 1e14)
    #ax3.set_yscale('log')


if __name__ == "__main__":
    plot_graph()
    show()
