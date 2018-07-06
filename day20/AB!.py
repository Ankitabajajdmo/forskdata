import pandas as pd
df=pd.read_csv("affairs.csv")
df.isnull().sum()

#******************
df.columns
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#saleprice correlation matrix
k = 9 #number of variables for heatmap
corrmat =df.corr()
cols = corrmat.nlargest(k, 'affair')['affair'].index
cm = np.corrcoef(df[cols].values.T)
sns.set(font_scale=1.5)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
plt.show()
#***************

features=df.iloc[:,:-1].values
'''
features=pd.DataFrame(features)
features.drop([3], axis = 1, inplace = True)
'''
label=df.iloc[:,-1].values.reshape(-1,1)


from sklearn.preprocessing import OneHotEncoder
ohe1=OneHotEncoder(categorical_features=[7])
features1=ohe1.fit_transform(features).toarray()
features=features1[:,1:]

ohe2=OneHotEncoder(categorical_features=[11])
features1=ohe2.fit_transform(features).toarray()
features=features1[:,1:]


from sklearn.model_selection import train_test_split
features_train,features_test,label_train,label_test = train_test_split(features,label,test_size=0.10,random_state=0)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(random_state=0)
lr.fit(features_train,label_train)

label_pred=lr.predict(features_test)

from sklearn.metrics import confusion_matrix
cm1=confusion_matrix(label_test,label_pred)

score=lr.score(features_test,label_test)


import numpy as np
x=ohe1.transform(np.array([3,25,3,1,4,16,4,2]).reshape(1,-1)).toarray()
x = ohe2.transform(x[:,1:]).toarray()
x = x[:,1:]
lr.predict(x)[0]



import statsmodels.api as sm
features=np.append(arr=np.ones((6366,1)).astype(int),values=features,axis=1)

lab = df.iloc[:,-1].values
model = sm.OLS(lab,features)
results = model.fit()
print(results.summary())



'''
'rate_marriage'=3
'age'=25
 'yrs_married'=3
 'children'=1
 'religious'=4
 'educ'=16
 'occupation'=4
 'occupation_husb'=2
 'affair'
'''


