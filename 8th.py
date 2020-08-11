from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

i = datasets.load_iris()
print(type(i))
print(i.data)
print(i.feature_names)
print(i.target)
print(i.target_names)
x = i.data[:, 2]
y = i.target
x_train, x_test, y_train, y_test = np.array(train_test_split(x, y, test_size=0.2, random_state=4))

model = svm.SVC(kernel='linear')
model.fit(x_train, y_train)
print(accuracy_score(x_test, y_test))

"""
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# i = datasets.load_iris()
# print(type(i))
# print(i.data)
# print(i.feature_names)
# print(i.target)
# print(i.target_names)
# x = i.data[:, 2]
# y = i.target
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
# x_tr_m = x_train.reshape(-1, 1)
# x_ts_m = x_test.reshape(-1, 1)
# y_tr_m = y_train.reshape(-1, 1)
# y_ts_m = y_test.reshape(-1, 1)
# model = svm.SVC(kernel='linear')
# model.fit(x_tr_m, y_tr_m)
# y_pred_m = model.predict(x_ts_m)
# print(accuracy_score(y_ts_m, y_pred_m))


## KNN / K nearest neighbors

i = load_iris()
x = i.data
y = i.target
print(x.shape)
print(y.shape)

knn = KNeighborsClassifier(n_neighbors=1)
print(knn)
print(knn.fit(x, y))
a = np.array([[4, 5, 6, 2]])
print(knn.predict(a))
"""


