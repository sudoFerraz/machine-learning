import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
# creating the classifier
clf = GaussianNB()
# fitting the classifier
clf.fit(X, Y)
# testing a new point
print clf.predict([[-0.8, -1]])
