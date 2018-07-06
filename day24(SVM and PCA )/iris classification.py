from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data

from sklearn.decomposition import PCA
pca=PCA(n_components=2)
features=pca.fit_transform(iris)
variance=pca.explained_variance_ratio_

from sklearn.cluster import KMeans
kmeans =KMeans(n_clusters=3,init="k-means++",random_state=0)
y_means=kmeans.fit_predict(features)

import matplotlib.pyplot as plt
plt.scatter(features[y_means == 2,0],features[y_means ==2,1],s=100,c="green")
plt.scatter(features[y_means == 0,0],features[y_means == 0,1],s=100,c="red")
plt.scatter(features[y_means == 1,0],features[y_means ==1,1],s=100,c="blue")
plt.title("species of Iris flower")
plt.xlabel("species")
plt.ylabel("")
plt.legend()
plt.show()
