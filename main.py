from sklearn import datasets
from sklearn.model_selection import train_test_split
from decision_tree import DecisionTree
import numpy as np

data = datasets.load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

clf = DecisionTree(max_depth=10)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy
print(X.shape)
#print(np.random.choice(211,5,replace=False))
acc = accuracy(y_test, predictions)
print(acc)