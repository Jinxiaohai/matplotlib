#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import subprocess
import matplotlib.pyplot as plt
import numpy as np


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.xlabel("Smarts")
plt.ylabel("Probability")
plt.title("Histogram of IQ")
plt.text(60, 0.025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
