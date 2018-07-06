import pandas as pd
df=pd.read_csv("iq_size.csv")
df.isnull().sum()

features=df.iloc[:,1:].values
label_piq=df.iloc[:,0].values.reshape(-1,1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features=sc.fit_transform(features)

import numpy as np
import statsmodels.formula.api as sm
features = np.append(arr = np.ones((38,1)).astype(int),values = features,axis=1)

features_opt = features[:,[0,1,2,3]]
r_ols= sm.OLS(endog=label_piq,exog=features_opt).fit()

features_opt = features[:,[0,1,2]]
r_ols= sm.OLS(endog=label_piq,exog=features_opt).fit()


features_opt = features[:,[0,1]]
r_ols= sm.OLS(endog=label_piq,exog=features_opt).fit()

r_ols.summary()

features_opt = features_opt[:,1:].reshape(-1,1)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()

lr.fit(features_opt,label_piq)


score = lr.score(features_opt,label_piq)


x = np.array([90,70,150]).reshape(1,-1)
x=sc.transform(x)

pred = lr.predict(x[0][0])

