import pandas as pd

loan_df=pd.read_csv("Loan.csv")

for i in loan_df:    
    mode=loan_df[i].mode()[0] 
    loan_df[i]=loan_df[i].fillna(mode)


features =loan_df.iloc[:,:-1].values
labels=loan_df.iloc[:,-1].values

'''
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,label_test = train_test_split(features,labels,test_size = 0.2,random_state=0)
'''
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()

for i in range(0,6):
    features[:,i]=le.fit_transform(features[:,i])

features[:,11]=le.fit_transform(features[:,11])

ohe=OneHotEncoder(categorical_features=[11])
features=ohe.fit_transform(features).toarray()

labels=le.fit_transform(labels)

from sklearn.model_selection import train_test_split
features_train1,features_test1,labels_train1,label_test1 = train_test_split(features,labels,test_size = 0.2,random_state=0)

'''
features_train1 = pd.DataFrame(features_train1)
features_test1 = pd.DataFrame(features_test1)
labels_train1= pd.DataFrame(labels_train1)
label_test1=pd.DataFrame(label_test1)
'''