import pandas as pd

dataset=pd.read_csv("Automobile.csv")
print(dataset.dtypes)

newdataset = dataset.select_dtypes(include=object)
print(newdataset.dtypes)

for i in newdataset:    
    mode=newdataset[i].mode()[0] 
    newdataset[i]=newdataset[i].fillna(mode)

features = newdataset.iloc[:,:].values


from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()

features[:,4]=le.fit_transform(features[:,4])
view=pd.DataFrame(features)






features[:,5]=le.fit_transform(features[:,5])
view=pd.DataFrame(features)

for i in [0,1,2,3,6,7,8,9]:
    features[:,i]=le.fit_transform(features[:,i])
    

ohe=OneHotEncoder(categorical_features=[5])
features=ohe.fit_transform(features).toarray()

