# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:23:51 2018

@author: hp
"""

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(150, 20, 1000)

plt.hist(incomes,100)
print(incomes.std())
print(incomes.var())