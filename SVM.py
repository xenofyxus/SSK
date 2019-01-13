from sklearn.svm import SVC
import numpy as np
import os
import math
import time
import matplotlib.pyplot as plt
from SSKModified import Ssk
from sklearn import svm, datasets

start = time.time()
counter = 0
n, lam, limCoefficient = 3, 0.5, 0.01
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

length = len(training)
gramMatrix = np.zeros((length, length))
count = 0
for i in range(length):
        for j in range(i, length):
                gramMatrix[i][j] = ssk.kernel(training[i], training[j])
                gramMatrix[j][i] = gramMatrix[i][j]
                count += 1
                print(count, ' documents done out of ', length * length, ' documents')

normalized_gramMatrix = np.zeros((length, length))

for i in range(length):
        for j in range(i, length):
                normalized_gramMatrix[i][j] = gramMatrix[i][j] / (math.sqrt(gramMatrix[i][i]*gramMatrix[j][j]))

for array in normalized_gramMatrix:
        print(array)
print("----- %s seconds -----" % (time.time() - start))

"""
model = svm.SVC(kernel=ssk.kernel).fit(training, targets)

X, y = datasets.make_multilabel_classification()

X = X[:,:2]

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
#model = svm.SVC(kernel=own_kernel).fit(X, y)
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
"""