# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:41:27 2018

@author: hp
"""

import operator
x = {"A": 2, "B": 4, "C": 3, "D": 1, "E": 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))

print(sorted_x)
