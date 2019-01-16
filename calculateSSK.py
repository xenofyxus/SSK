from sklearn import svm
import numpy as np  
import sklearn.preprocessing as preprocessing
import os
import math
import time
from SSKModified import Ssk

category = 'corn' #Test andra kategorier
category2 = 'gold'  #testa andra kategorier
testCatsPath = 'C:/MLprojekt/SSK/reuters/reuters/testCats.txt'
trainingCatsPath = 'C:/MLprojekt/SSK/reuters/reuters/trainingCats.txt'
trainingPath = 'C:/MLprojekt/SSK/reuters/reuters/'+category+'Training'  # path for training set
testPath = 'C:/MLprojekt/SSK/reuters/reuters/'+category+'Test'  # path for test set
trainingPath2 = 'C:/MLprojekt/SSK/reuters/reuters/'+category2+'Training'  # path for training set
testPath2 = 'C:/MLprojekt/SSK/reuters/reuters/'+category2+'Test'  # path for test set
start = time.time()

n = 5
lam = 0.5
trainingSize = 10   #Dessa bör tweakas i olika test
testSize = 4        #Dessa bör tweakas i olika test
count = 0           
ssk = Ssk(n, lam, 0.01) #0.01 är vår egen variabel

def getFiles(path, path2, amount, testSize):

    print('fetching ', amount, ' files')
    count, testCount = 0, 0
    files, fileNames, categories = [' ' for i in range(amount)], [' ' for i in range(amount)], [' ' for i in range(amount)]
    testSet, testNames, testCategories = [' ' for i in range(testSize)], [' ' for i in range(testSize)], [' ' for i in range(testSize)]

    for file in os.listdir(path):
        if (count >= amount):
            if (testCount >= testSize):
                break
            else:
                testNames[testCount] = file
                f = open(path+'/'+file, 'r')
                testSet[testCount] = f.read()
                f.close()
                testCategories[testCount] = category
                testCount += 2
        else:
            
            fileNames[count] = file
            f = open(path+'/'+file, 'r')
            files[count] = f.read()
            f.close()
            categories[count] = category
            count += 2

    count, testCount = 1, 1
    for file in os.listdir(path2):
        if (count >= amount):
            if (testCount >= testSize):
                break
            else:
                testNames[testCount] = file
                f = open(path2+'/'+file, 'r')
                testSet[testCount] = f.read()
                f.close()
                testCategories[testCount] = category2
                testCount += 2
        else:

            fileNames[count] = file
            f = open(path2+'/'+file, 'r')
            files[count] = f.read()
            f.close()
            categories[count] = category2
            count += 2

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

    if(len(dataSet) == len(dataSet2)):
        print('equal length')
        for i in range(len(dataSet)):
            for j in range(i, len(dataSet2)):
                gram[i][j] = ssk.kernel(dataSet[i], dataSet2[j])
                gram[j][i] = gram[i][j]  
    else:
        print('not equal length')
        for i in range(len(dataSet)):
            for j in range(len(dataSet2)):
                gram[i][j] = ssk.kernel(dataSet[i], dataSet2[j]) 
    
    normalizedGram = np.zeros((len(dataSet), len(dataSet2)))
    for i in range(len(dataSet)):
        for j in range(len(dataSet)):
            normalizedGram[i][j] = gram[i][j]/math.sqrt(gram[i][i]*gram[j][j])

    return normalizedGram

trainingSet, trainingFileNames, trainingCats, testSet, testCategories = getFiles(trainingPath, trainingPath2, trainingSize, testSize)

for i in range(len(trainingCats)):
    print(trainingCats[i])

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

print('starting training model')
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