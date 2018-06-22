PREPROCESSING:
    using sklearm
    1.Imputer
    2.LabelEncoder
    3.OneHotEncoder
    
    using Pandas
    1.fillna
    2.cat-Cod
    3.cat-Dummies
    
    
#in ml, handling missing values is called IMPUTATION


from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values="NAN",strategy="most_frequent", axis=0,)
#imputer only works with numerical data

#for categorical data use fillna  to handle missing values
dataframe["column name"].fillna(mode, inplace=True)





