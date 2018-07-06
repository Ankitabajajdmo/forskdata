import pandas as pd
df=pd.read_csv("mushrooms.csv")
df.isnull().sum()

df.nunique()

features=df.loc[:,["habitat","population","odor"]].values
label=df.iloc[:,0].values.reshape(-1,1)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

for i in [0,1,2]:
    features[:,i]=le.fit_transform(features[:,i])
    
label=le.fit_transform(label).reshape(-1,1)

from sklearn.model_selection import train_test_split
fetures_train,features_test,labels_train,labels_test=train_test_split(features,label,test_size=0.1,random_state = 0)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,p=2)
classifier.fit(fetures_train,labels_train)

pred=classifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,pred)

score=classifier.score(features_test,labels_test)

