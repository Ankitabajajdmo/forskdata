import pandas as pd
df = pd.read_fwf('Auto_mpg.txt',header=None)
df.columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" ]
df.isnull().sum()

#car name  with highest mpg is 
df.query('mpg == mpg.max()')["car name"].values[0]

'''
carname=df["car name"][df["mpg"]==df[["mpg"]].max()[0]]
print("car name  with highest mpg is : ",carname.values[0])
#spike_cols = [col for col in df if '?' in df[col]]
'''

for i in df:
    if df[i].dtype==object:
        df[i][df[i]=='?'] = df[i].mode()[0]

df.iloc[:,-1].nunique()
features=df.iloc[:,1:-1]
labels=df.iloc[:,0].values.reshape(-1,1)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features=scaler.fit_transform(features)

from sklearn.cross_validation import train_test_split
features_train, features_test, label_train, label_test = train_test_split(features,labels,test_size=0.2,random_state=0)

view=pd.DataFrame(features)
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(features_train,label_train)
pred=regressor.predict(features_test)

import numpy as np
inputdata1=scaler.transform(np.array([6,215,100,2360,22.2,80,3]).reshape(1,-1))

label_predict= regressor.predict(inputdata1)
scored=regressor.score(features_test,label_test)


#******************************************************
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=12,random_state=0)
regressor.fit(features_train,label_train)
pred2=regressor.predict(features_test)

scored=regressor.score(features_test,label_test)

