# AI algorithms and libraries
# we can use the scikit-learn library to implement machine learning algorithms
from sklearn import datasets
# load the iris dataset
iris = datasets.load_iris()
# get the features and target
X = iris.data
y = iris.target
# we can use the KNN algorithm for classification
from sklearn.neighbors import KNeighborsClassifier
# create the KNN model
knn = KNeighborsClassifier(n_neighbors=3)
# train the model
knn.fit(X, y)
# make predictions
predictions = knn.predict(X)
print("Predictions: ")
print(predictions)