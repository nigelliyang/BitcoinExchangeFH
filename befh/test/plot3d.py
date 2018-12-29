# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:17:13 2015

@author: Eddy_zheng
"""

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

btcinitial = 10
btc = 3868
eth = 135

fig = plt.figure()
ax = Axes3D(fig)
# btc price
X = np.arange(100, 100000, 1000)
# eth price
Y = np.arange(10, 5000, 100)
X, Y = np.meshgrid(X, Y)

btcend = btcinitial - 2 * btcinitial * btc * 1 * (1 / btc - 1 / X) + (Y - eth) * 0.000001 * btcinitial / (
            eth * 0.000001) - btcinitial / (eth / btc) * (Y / X - eth / btc)

Z = btcend * X - btc * btcinitial

# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()
