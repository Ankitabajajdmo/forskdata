import pandas as pd

df=pd.read_csv("wine_data.csv",header=None,usecols=[0,1,2])
df.columns=['Class label', 'Alcohol', 'Malic acid']
features=df.values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features=sc.fit_transform(features)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
features=scaler.fit_transform(features)
