__author__ = 'arkilic'

import matplotlib.pylab as plt
from benchmark.userapi import *

# create_header(header_range=1000000) #create 1 mil headers

plt.figure(0)
xa, ya, avg = query_header(header_range=10)
plt1, = generate_query_plot(xa, ya, data_points=10)
show()
#
plt.figure(1)
xb, yb, avg2 = query_header2(header_range=100, data=True, num_headers=10)
print avg2
plt2, = generate_query_plot2(xb, yb, data_points=100)
#show()
