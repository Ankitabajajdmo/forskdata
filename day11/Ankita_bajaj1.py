import pandas as pd
df= pd.read_csv("training_titanic.csv")

df.groupby(['Sex'],sort=False)["Survived"].value_counts(normalize = True)



















#**************************************
df["Survived"].value_counts()

df["Survived"][df['Sex'] == 'female'].value_counts(normalize = True)

df_m= df[df['Sex'] == 'male']
df_m["Survived"].value_counts(normalize = True)

#*****************************

# xx=df.loc[:,["Sex","Survived"]]



