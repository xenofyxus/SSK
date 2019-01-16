from sklearn import svm, datasets
import matplotlib.pyplot as plt
import numpy as np  
from sklearn.svm import SVC
import sklearn.preprocessing as preprocessing
import os
import math
import time
import string
from efficientSSK import Ssk

category = 'corn'
category2 = 'gold'
testCatsPath = 'C:/MLprojekt/SSK/reuters/reuters/testCats.txt'
trainingCatsPath = 'C:/MLprojekt/SSK/reuters/reuters/trainingCats.txt'
trainingPath = 'C:/MLprojekt/SSK/reuters/reuters/'+category+'Training'  # path for training set
testPath = 'C:/MLprojekt/SSK/reuters/reuters/'+category+'Test'  # path for test set
trainingPath2 = 'C:/MLprojekt/SSK/reuters/reuters/'+category2+'Training'  # path for training set
testPath2 = 'C:/MLprojekt/SSK/reuters/reuters/'+category2+'Test'  # path for test set
start = time.time()

n = 5
lam = 0.5
trainingSize = 10
testSize = 4
count = 0
ssk = Ssk(n, lam)

def getFiles(path, path2, amount, testSize):

    print('fetching ', amount, ' files')
    half, halfTest, count, testCount = amount/2, testSize/2, 0, 0
    files, fileNames, categories, testSet, testNames, testCategories = [], [], [], [], [], []

    for file in os.listdir(path):
        if (count == half):
            if (testCount == halfTest):
                break
            else:
                testCount += 1
                testNames.append(file)
                f = open(path+'/'+file, 'r')
                testSet.append(f.read())
                f.close()
                testCategories.append(category)
        else:
            count += 1
            fileNames.append(file)
            f = open(path+'/'+file, 'r')
            files.append(f.read())
            f.close()
            categories.append(category)
            #print(amount - count , ' documents left')
            
    for file in os.listdir(path2):
        if (count == amount):
            if (testCount == testSize):
                break
            else:
                testCount += 1
                testNames.append(file)
                f = open(path2+'/'+file, 'r')
                testSet.append(f.read())
                f.close()
                testCategories.append(category2)
        else:
            count += 1
            fileNames.append(file)
            f = open(path2+'/'+file, 'r')
            files.append(f.read())
            f.close()
            categories.append(category2)
            #print(amount - count , ' documents left')

    return files, fileNames, categories, testSet, testCategories

def getCategories(path, fileNames):
    text = open(path, 'r')
    file = text.read().split('\n')  #Used for fetching the categories 
    for i in range(len(fileNames)):       #corresponding to each of the training texts
        for f in file:
            temp = f.split(' ')
            if (temp[0] == 'training/'+fileNames[i]):
                text = f.replace('training/'+fileNames[i]+' ', '')
                fileNames[i] = text
                break
    
    return fileNames

def calculateGram(dataSet, dataSet2):

    gram = np.zeros((len(dataSet), len(dataSet2)))
    for i in range(len(dataSet)):
        for j in range(i, len(dataSet2)):
            gram[i][j] = ssk.kernel(dataSet[i], dataSet2[j])
            gram[j][i] = gram[i][j]   
    
    normalizedGram = np.zeros((len(dataSet), len(dataSet2)))
    for i in range(len(dataSet)):
        for j in range(len(dataSet)):
            normalizedGram[i][j] = gram[i][j]/math.sqrt(gram[i][i]*gram[j][j])

    return normalizedGram

trainingSet, trainingFileNames, trainingCats, testSet, testCategories = getFiles(trainingPath, trainingPath2, trainingSize, testSize)
trainingGram = calculateGram(trainingSet, trainingSet)
testGram = calculateGram(testSet, trainingSet)

for i in range(len(testGram)):
    for j in range(len(testGram)):
        print(testGram[i][j])
    print('-----------')

labels = np.array(trainingCats).reshape(-1)
encoder = preprocessing.LabelEncoder()
encoder.fit(labels)
labels = encoder.transform(labels)

model = svm.SVC(kernel='precomputed')
model.fit(trainingGram, labels)
predictions = model.predict(testGram)
print(predictions)

testLabels = np.array(testCategories)
encoder = preprocessing.LabelEncoder()
encoder.fit(testLabels)
testLabels = encoder.transform(testLabels)

countNumberOfRights = 0
for i in range(len(testLabels)):
	if(predictions[i] == testLabels[i]):
		countNumberOfRights += 1

print("right:", countNumberOfRights/len(testLabels))
print('---------- ', time.time() - start, ' -----------')