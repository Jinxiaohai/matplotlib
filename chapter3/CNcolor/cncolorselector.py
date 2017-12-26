#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""document of the module"""


import os
import sys
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

th = np.linspace(0, 2*np.pi, 128)


def demo(sty):
    mpl.style.use(sty)
    fig, ax = plt.subplots(figsize=(3, 3))

    ax.set_title("style: {!r}".format(sty), color="C0")

    ax.plot(th, np.cos(th), "C1", label="C1")
    ax.plot(th, np.sin(th), "C2", label="C2")
    ax.legend()


demo("default")
plt.savefig("default.png")
demo("seaborn")
plt.savefig("seaborn.png")

plt.show()
