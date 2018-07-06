import pandas as pd 

deliveryfleet=pd.read_csv("deliveryfleet.csv")
deliveryfleet.isnull().sum()

deliveryfleet.nunique()

features=deliveryfleet.iloc[:,1:].values

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

kmeans =KMeans(n_clusters= 2,init = "k-means++" , random_state= 0)
y_means=kmeans.fit_predict(features)

plt.scatter(features[y_means == 0,0],features[y_means == 0,1],s=100,c="red",label="Rural drivers")
plt.scatter(features[y_means == 1,0],features[y_means ==1,1],s=100,c="blue",label="Urban drivers")
plt.title("clusters of deliveryfleet")
plt.xlabel("Distance")
plt.xlabel("speeding")
plt.legend()
plt.show()


kmeans =KMeans(n_clusters=4,init = "k-means++" , random_state= 0)
y_mean4s=kmeans.fit_predict(features)

plt.scatter(features[y_mean4s == 0,0],features[y_mean4s == 0,1],s=100,c="red",label="Rural drivers")
plt.scatter(features[y_mean4s == 1,0],features[y_mean4s ==1,1],s=100,c="blue",label="Urban drivers")
plt.scatter(features[y_mean4s == 2,0],features[y_mean4s ==2,1],s=100,c="green",label=" urban drivers speed")
plt.scatter(features[y_mean4s == 3,0],features[y_mean4s ==3,1],s=100,c="magenta",label="rural drivers speed")

plt.title("clusters of deliveryfleet")
plt.xlabel("Distance")
plt.ylabel("speeding")
plt.legend()
plt.show()
