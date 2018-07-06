import pandas as pd
df=pd.read_csv("bluegills.csv")

df.isnull().sum()
feature=df.iloc[:,0].reshape(-1,1)
labels=df.iloc[:,1].reshape(-1,1)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(feature,labels)
lr.predict(5)
score1=lr.score(feature,labels)

import matplotlib.pyplot as plt
plt.scatter(feature,labels,color="red")
plt.plot(feature,lr.predict(feature),color="blue")
plt.title("fish length prediction")
plt.xlabel("age")
plt.ylabel("length")




from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree=5)
feature_poly = poly_object.fit_transform(feature)

lr2 = LinearRegression()
lr2.fit(feature_poly,labels)

plt.scatter(feature,labels,color="red")
plt.plot(feature,lr2.predict(feature_poly),color="blue")
plt.title("fish length prediction")
plt.xlabel("age")
plt.ylabel("length")

lr2.predict(poly_object.fit_transform(5))
score2=lr2.score(feature_poly,labels)


import numpy as np
features_grid=np.arange(min(feature),max(feature),0.1)
features_grid=features_grid.reshape(-1,1)
plt.scatter(feature,labels,color="red")
plt.plot(features_grid,lr2.predict(poly_object.fit_transform(features_grid)),color="blue")
plt.title("fish length prediction")
plt.xlabel("age")
plt.ylabel("length")

lr3 = LinearRegression()
lr3.fit(features_grid,labels[:50])
lr3.predict(poly_object.fit_transform(5))
score3=lr3.score(features_grid,labels[:50])
