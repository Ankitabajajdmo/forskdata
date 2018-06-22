# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:46:38 2018

@author: hp
"""

import pandas as pd
import numpy as np
df= pd.read_csv("Automobile.csv")
df["price"]=df["price"].fillna(df["price"].mean())

ary=np.array(df.price)
print("min : ",ary.min())
print("max : ",ary.max())
print("Average : ",ary.mean())
print("standard deviation : ",ary.std())