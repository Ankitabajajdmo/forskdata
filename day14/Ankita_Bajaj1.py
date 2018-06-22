import pandas as pd

dataset=pd.read_csv("Automobile.csv")
print(dataset.dtypes)

newdataset = dataset.select_dtypes(include=object)
print(newdataset.dtypes)

#to check if any column has NaN in a Pandas DataFrame
null_columns=newdataset.columns[newdataset.isnull().any()]

#handle missing values
mode=newdataset["num_doors"].mode()[0] 
newdataset["num_doors"].fillna(mode, inplace=True)

#label encoding

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder=LabelEncoder()


#newdataset["body_style"]=labelencoder.fit_transform(newdataset["body_style"])

for i in newdataset.columns:
    newdataset[i]=labelencoder.fit_transform(newdataset[i])

#labelencoder.fit(["convertable","hardtop","hatchback","sedan","wagon"])
#newdataset["body_style"]=labelencoder.transform(newdataset["body_style"])

#newdataset["drive_wheels"]=labelencoder.fit_transform(newdataset["drive_wheels"])

onehotencoder=OneHotEncoder(categorical_features=[0])
newdataset=onehotencoder.fit_transform(newdataset).toarray()