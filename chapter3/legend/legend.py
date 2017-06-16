#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import subprocess
import matplotlib.pyplot as plt
import numpy as np


line_up, = plt.plot([1, 2, 3], label="Line 2")
line_down, = plt.plot([3, 2, 1], label="Line 1")
plt.legend(handles=[line_up, line_down])
plt.show()
