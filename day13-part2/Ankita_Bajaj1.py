# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 18:00:51 2018

@author: hp
"""


import pandas as pd

dataset=pd.read_csv("Cars.csv")
features = dataset.iloc[:,1:].values
labels=dataset.iloc[:,0].values

from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,label_test = train_test_split(features,labels,test_size = 0.5,random_state=0)

features_train = pd.DataFrame(features_train)
features_test = pd.DataFrame(features_test)
labels_train= pd.DataFrame(labels_train)
label_test=pd.DataFrame(label_test)

features_train.to_csv('features_train.csv', index=False, header=False)
features_test.to_csv('features_test.csv', index=False, header=False)
labels_train.to_csv("labels_train.csv",index=False, header=False)
label_test.to_csv("label_test.csv",index=False, header=False)



'''
def convert_to_csv(listname):    
    listname = pd.DataFrame(listname)
    name =str([x for x in globals() if globals()[x] is listname][0])
    print(name)
    listname.to_csv(name+".csv", index=False, header=False)

convert_to_csv(features_train)
convert_to_csv(features_test)
convert_to_csv(labels_train)
convert_to_csv(label_test)

'''
