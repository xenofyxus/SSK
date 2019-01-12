from sklearn.svm import SVC
import numpy as np
import os
import matplotlib.pyplot as plt
from SSKModified import Ssk
from sklearn import svm, datasets


iris = datasets.load_iris()
# Select 2 features / variable for the 2D plot that we are going to create.
counter = 0
n, lam, limCoefficient = 3, 0.5, 0.05
trainingPath = 'C:/MLprojekt/SSK/reuters/reuters/silverTraining'
targets = []
training = []
ssk = Ssk(n, lam, limCoefficient)
count = 0

for file in os.listdir(trainingPath):
        if (10 > count):
                f = open(trainingPath+'/'+file, 'r')
                text = f.read()
                training.append(text)
                targets.append('silver')
                counter = counter + 1
                f.close
        else:
                break
        count += 1
count = 0
trainingPath = 'C:/MLprojekt/SSK/reuters/reuters/goldTraining'              
for file in os.listdir(trainingPath):
        if (10 > count):
                f = open(trainingPath+'/'+file, 'r')
                text = f.read()
                training.append(text)
                targets.append('gold')
                counter = counter + 1
                f.close
        else:
                break
        count += 1


print('length is ', len(training))
model = svm.SVC(kernel=ssk.kernel).fit(training, targets)

X, y = datasets.make_multilabel_classification()

X = X[:,:2]


def own_kernel(X, Y):
    """
    We create a custom kernel:

                 (2  0)
    k(X, Y) = X  (    ) Y.T
                 (0  1)
    """
    M = np.array([[2, 0], [0, 1.0]])
    return np.dot(np.dot(X, M), Y.T)

def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out
"""
model = svm.SVC(kernel=own_kernel).fit(X, y)
"""
fig, ax = plt.subplots()
X0, X1 = X[:, 0], X[:, 1]
xx, yy = make_meshgrid(X0, X1)

plot_contours(ax, model, xx, yy, alpha=0.8)
ax.scatter(X0, X1, c=y, s=20, edgecolors='k')
ax.set_ylabel('THIS IS AN INTERESTING FEATURE')
ax.set_xlabel('THIS IS ANOTHER')
ax.set_title('TITLE GAME ON POINT')     
ax.set_xticks(())
ax.set_yticks(())
ax.legend()
plt.show()
