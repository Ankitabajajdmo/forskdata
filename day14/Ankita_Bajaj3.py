import pandas as pd

loan_df=pd.read_csv("Loan.csv")
for i in loan_df:    
    mode=loan_df[i].mode()[0] 
    loan_df[i]=loan_df[i].fillna(mode)


features =loan_df.iloc[:,:-1]
labels=loan_df.iloc[:,-1]

for i in features.columns[1:6]:
    features[i] = features[i].astype('category')
    features[i] = features[i].cat.codes

features["Property_Area"] = features["Property_Area"].astype('category')
features["Property_Area"] = features["Property_Area"].cat.codes

encoded_features =pd.get_dummies(features, columns=["Property_Area"])

from sklearn.model_selection import train_test_split
features_train1,features_test1,labels_train1,label_test1 = train_test_split(features,labels,test_size = 0.2,random_state=0)