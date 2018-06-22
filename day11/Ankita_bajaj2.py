import pandas as pd
df= pd.read_csv("training_titanic.csv")

df["child"]=0

df['child'][df['Age'] < 18] = 1

df.groupby(['child'],sort=False)["Survived"].value_counts(normalize = True)[1][1]


#***************************************



import pandas as pd
df= pd.read_csv("training_titanic.csv")

df["child"]=0
df["Age"]=df["Age"].fillna(df['Age'].mean())
df['child'][df['Age'] < 18] = 1

df.groupby(['child'],sort=False)["Survived"].value_counts(normalize = True)[1][1]
