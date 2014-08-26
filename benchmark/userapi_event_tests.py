__author__ = 'arkilic'

import matplotlib.pylab as plt
from benchmark.userapi import *
from matplotlib.pylab import text

plt.figure(0)
xa, ya, avg = record_event(10)
plt1, = generate_event_plot(xa, ya, 10)
text(5, 5,'matplotlib',
     horizontalalignment='center',
     verticalalignment='center')
show()
#
#
# plt.figure(1)
# xb, yb, avg2 = record_event(100)
# plt2, = generate_event_plot(xb, yb, 100)
# show()
# plt.figure(2)
# xc, yc, avg3 = record_event(1000)
# plt3, = generate_event_plot(xc, yc, 1000)
#
#
# plt.figure(3)
# xd, yd, avg4 = record_event(10000)
# plt4, = generate_event_plot(xd, yd, 10000)
#
#
#
