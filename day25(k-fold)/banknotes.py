import pandas as pd
df=pd.read_csv("banknotes.csv")

features=df.iloc[:,1:-1]
labels=df.iloc[:,-1].values.reshape(-1,1)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features=sc.fit_transform(features)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(random_state=0)
lr.fit(features,labels)
label_predicted=lr.predict(features)
score=lr.score(features,labels)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels,label_predicted)

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = lr, X = features, y =labels, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())

