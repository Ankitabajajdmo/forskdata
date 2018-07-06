import pandas as pd

df=pd.read_csv("PastHires.csv")

df.isnull().sum()
#sklearn.ensemble

#df["Level of Education"].nunique()

features=df.iloc[:,:-1].values
labels=df.iloc[:,-1].reshape(-1,1)

from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()

for i in [1,3,4,5]:
    features[:,i]=le.fit_transform(features[:,i])
labels=le.fit_transform(labels)
view=pd.DataFrame(features)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(features,labels)

import numpy as np
label_predict= regressor.predict(np.array([10,1,4,0,0,1]).reshape(1,-1))
label_predict2= regressor.predict(np.array([10,0,4,1,0,1]).reshape(1,-1))

scored=regressor.score(features,labels)

import matplotlib.pyplot as plt
features_grid = np.arange(min(features[0]),max(features[0]),0.01)
features_grid = features_grid.reshape(-1,1)
plt.scatter(features[:,0],labels,color="red")
plt.plot(features_grid[0],regressor.predict(features_grid),color = "blue")
plt.title("hired or not")
plt.xlabel("features")
plt.ylabel("hired")
plt.show()

