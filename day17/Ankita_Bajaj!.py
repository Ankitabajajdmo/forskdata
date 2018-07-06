import pandas as pd
df=pd.read_csv("iq_size.csv")
df.isnull().sum()

features=df.iloc[:,1:].values
label_piq=df.iloc[:,0].values.reshape(-1,1)

