#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import subprocess
import matplotlib.pyplot as plt
import numpy as np


ax = plt.subplot(1, 1, 1)

t = np.arange(0., 5., 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate("local max", xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor="black", shrink=0.05))

plt.ylim(-2, 2)
plt.show()
