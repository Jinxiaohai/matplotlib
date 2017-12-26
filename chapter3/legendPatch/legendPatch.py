#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


red_patch = mpatches.Patch(color="red", label="The red data")
plt.legend(handles=[red_patch])

plt.show()
