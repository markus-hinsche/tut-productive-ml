"""Train from scratch"""

from sklearn import svm
from sklearn import datasets
from joblib import dump, load

# Train model
clf = svm.SVC()
X, y= datasets.load_iris(return_X_y=True)
clf.fit(X, y)

# Save model
filename = 'iris.p'
dump(clf, filename)
clf2 = load(filename)
clf2.predict(X[0:1])
