import pandas as pd
df=pd.read_csv("Red_Wine.csv")

#handling missing values
for i in df:    
    mode=df[i].mode()[0] 
    df[i]=df[i].fillna(mode)
    
#features and labels
features =df.iloc[:,:-1].values
labels=df.iloc[:,-1].values

#label encoding
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()
features[:,0]=le.fit_transform(features[:,0])

#onehotencoding
ohe=OneHotEncoder(categorical_features=[0])
features=ohe.fit_transform(features).toarray()


#train test split
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,label_test = train_test_split(features,labels,test_size = 0.2,random_state=0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)
