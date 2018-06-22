# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:25:40 2018

@author: hp
"""
import numpy as np

x=np.random.randint(5,15,40)

from scipy.stats import mode

print(mode(x)[0][0])

#********************

counts = np.bincount(x)
print(np.argmax(counts))

#*********************

from collections import Counter
b = Counter(x)
print(b.most_common(1)[0][0])


