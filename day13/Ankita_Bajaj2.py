import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("Automobile.csv")
x=df["make"].value_counts().head(10)

labels =list(x.index)
sizes =x.values

explode=[0]*len(sizes) #creating list of length (sizes) and  all initialized to 0
explode[0] = 0.1  # only "explode" the 1st slice (i.e. 'toyota')

plt.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%', shadow=True, startangle=100)
 
plt.axis('equal')
plt.show()

