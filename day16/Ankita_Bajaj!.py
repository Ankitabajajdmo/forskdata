import pandas as pd

df_foodtruck=pd.read_csv("Foodtruck.csv")
population=df_foodtruck.iloc[:,0].values
profit=df_foodtruck.iloc[:,1].values

from sklearn.model_selection import train_test_split
population_train , population_test,profit_train,profit_test=train_test_split(population,profit,test_size =0.2,random_state = 0)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(population_train,profit_train)
