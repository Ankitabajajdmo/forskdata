import pandas as pd
df=pd.read_csv("breast_cancer.csv")

df.isnull().sum()
df.nunique()

df["G"]=df["G"].fillna(df.G.mode()[0])

df=df.iloc[:,1:]
features=df.iloc[:,:-1].values
labels=df.iloc[:,-1].values.reshape(-1,1)

from sklearn.model_selection import train_test_split
features_train , features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state = 0)

from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)

import numpy as np
x=np.array([6,2,5,3,9,4,7,2,2]).reshape(1,-1)
classifier.predict(x)

'''
Predict whether a women has Benign tumor or Malignant tumor, if her Clump thickness 
is around 6, uniformity of cell size is 2, Uniformity of Cell Shape is 5, Marginal Adhesion is 3,
Bland Chromatin is 9, Mitoses is 4, Bare Nuclei is 7, Normal Nuclei is 2 and Single Epithelial Cell Size is 2
'''
