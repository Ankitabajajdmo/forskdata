import pandas as pd
df=pd.read_csv("crime_data.csv")
features=df.iloc[:,1:].values

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features=sc.fit_transform(features)

from sklearn.decomposition import PCA
pca=PCA(n_components=2)
features=pca.fit_transform(features)
variance=pca.explained_variance_ratio_


from sklearn.cluster import KMeans
wcss =[]
for i in range(1,11):
    kmeans =KMeans(n_clusters=i,init="k-means++",random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
    
import matplotlib.pyplot as plt
plt.plot(range(1,11),wcss)
plt.xlabel("no. of clusters")
plt.ylabel("wcss")
plt.show()

kmeans =KMeans(n_clusters=3,init="k-means++",random_state=0)
y_means=kmeans.fit_predict(features)





plt.scatter(features[y_means == 2,0],features[y_means ==2,1],s=100,c="green")
plt.scatter(features[y_means == 0,0],features[y_means == 0,1],s=100,c="red")
plt.scatter(features[y_means == 1,0],features[y_means ==1,1],s=100,c="blue")

'''
plt.scatter(features[y_means == 3,0],features[y_means ==3,1],s=100,c="black")
plt.scatter(features[y_means == 4,0],features[y_means ==4,1],s=100,c="Maroon")
plt.scatter(features[y_means == 5,0],features[y_means == 5,1],s=100,c="magenta")
plt.scatter(features[y_means == 6,0],features[y_means ==6,1],s=100,c="olive")
plt.scatter(features[y_means == 7,0],features[y_means ==7,1],s=100,c="purple")
'''
plt.title("cities group")
plt.xlabel("rape,Murder")
plt.ylabel("Assault")
plt.legend()
plt.show()

df["Crime_Groups"]=y_means

