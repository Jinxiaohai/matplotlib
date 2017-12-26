#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import subprocess
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title("click on points")

line, = ax.plot(np.random.rand(100), "o", picker=5)

def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_yline()
    ind = event.ind
    points = tuple(zip(xdata[ind], ydata[ind]))
    print("onpick points:", points)

fig.canvas.mpl_connect("pick_event", onpick)

plt.show()
