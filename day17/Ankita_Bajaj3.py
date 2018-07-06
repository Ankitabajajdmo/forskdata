import pandas as pd
df = pd.read_csv("stats_females.csv")

df.isnull().sum()

features=df.iloc[:,1:].values
label_stu_height=df.iloc[:,0].reshape(-1,1)

import numpy as np
import statsmodels.formula.api as sm
features = np.append(arr = np.ones((214,1)).astype(int),values = features,axis=1)

features_opt = features[:,[0,1,2]]
r_ols= sm.OLS(endog=label_stu_height,exog=features_opt).fit()
r_ols.summary()

