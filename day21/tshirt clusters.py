import pandas as pd
tshirt_df=pd.read_csv("tshirts.csv")

tshirt_df.isnull().sum()
tshirt_df.nunique()

features=tshirt_df.iloc[:,1:].values

from sklearn.cluster import KMeans
wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init ="k-means++",random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
   
import matplotlib.pyplot as plt
plt.plot(range(1,11),wcss)
plt.title("The Elbow model")
plt.xlabel("no. of clusters")
plt.ylabel("WCSS")
plt.show()    


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features=sc.fit_transform(features)

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
kmeans =KMeans(n_clusters= 3,init = "k-means++" , random_state= 0)
y_means=kmeans.fit_predict(features)




plt.scatter(features[y_means == 0,0],features[y_means == 0,1],s=100,c="red",label="small")
plt.scatter(features[y_means == 2,0],features[y_means ==2,1],s=100,c="green",label="mediun")
plt.scatter(features[y_means == 1,0],features[y_means ==1,1],s=100,c="blue",label="large")

plt.title("T shirt factory")
plt.xlabel("Height")
plt.ylabel("weight")
plt.legend()
plt.show()