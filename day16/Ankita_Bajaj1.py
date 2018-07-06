import pandas as pd
import numpy as np

df_foodtruck=pd.read_csv("Foodtruck.csv")
population=df_foodtruck.iloc[:,0].values.reshape(-1,1)#reshape to get 2d array format
profit=df_foodtruck.iloc[:,1].values.reshape(-1,1)

from sklearn.model_selection import train_test_split
population_train , population_test,profit_train,profit_test=train_test_split(population,profit,test_size =0.2,random_state = 0)


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(population_train,profit_train)

profit_predict = lr.predict(population_test)

jaipur_predict = lr.predict(3.073)[0][0]

score=lr.score(population_test,profit_test)


import matplotlib.pyplot as plt
#visualising train results
plt.scatter(population_train,profit_train,color="red")
plt.plot(population_train,lr.predict(population_train),color="blue")
plt.title("Population vs Profit ")
plt.xlabel("population")
plt.ylabel("profit")
plt.show()

#visualising test results
plt.scatter(population_test,profit_test,color="red")
plt.plot(population_train,lr.predict(population_train),color="blue")
plt.title("Population vs Profit ")
plt.xlabel("population")
plt.ylabel("profit")
plt.show()

