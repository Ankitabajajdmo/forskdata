import pandas as pd
import matplotlib.pyplot as plt

df_movies=pd.read_csv("Bahubali2_vs_Dangal.csv")

days=df_movies.iloc[:,0].values.reshape(-1,1)
movies=df_movies.iloc[:,[1,2]].values.reshape(-1,2)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(days,movies)

my_predict=lr.predict(days)
day10_predict=lr.predict(9)

score=lr.score(days,movies)

#visualising train results
plt.scatter(days,movies[:,0],color="red")
plt.scatter(days,movies[:,1],color="green")

plt.plot(days,lr.predict(days)[:,0],color="red")
plt.plot(days,lr.predict(days)[:,1],color="green")

plt.title("Bahubali2_vs_Dangal ")
plt.xlabel("day")
plt.ylabel("movies")
plt.show()