import pandas as pd
df=pd.read_csv("iq_size.csv")
df.isnull().sum()

features=df.iloc[:,1:].values
label_piq=df.iloc[:,0].values.reshape(-1,1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features=sc.fit_transform(features)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(features,label_piq)

score = lr.score(features,label_piq)

import numpy as np

x = np.array([90,70,150]).reshape(1,-1)
x=sc.transform(x)
pred = lr.predict(x)

