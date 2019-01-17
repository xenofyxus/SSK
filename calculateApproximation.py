from sklearn import svm, datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC
import sklearn.preprocessing as preprocessing
import os
import math
import time
import string
from approximationSSK import Ssk

category = 'gold'     #Dessa byter du för nya kategorier VIKTIGT
category2 = 'silver'      #Dessa byter du för nya kategorier VIKTIGT titta i reuters/reuters mappen för att se olika kategorier
testCatsPath = 'C:/MLprojekt/SSK/reuters/reuters/testCats.txt'
trainingCatsPath = 'C:/MLprojekt/SSK/reuters/reuters/trainingCats.txt'
trainingPath = 'C:/MLprojekt/SSK/reuters/reuters/'+category+'Training'  # path for training set
testPath = 'C:/MLprojekt/SSK/reuters/reuters/'+category+'Test'  # path for test set
trainingPath2 = 'C:/MLprojekt/SSK/reuters/reuters/'+category2+'Training'  # path for training set
testPath2 = 'C:/MLprojekt/SSK/reuters/reuters/'+category2+'Test'  # path for test set
start = time.time()

n = 6               #N måste stämma överrens med antal bokstäver i orden
lam = 0.5           #Testa gärna olika Markus men kom ihåg att bortkommentera commonWords du inte använder
#commonWords = open('C:/MLprojekt/SSK/CommonWords4.txt').read().split('\n') #100 ord, 4 bokstäver längd
#commonWords = open('C:/MLprojekt/SSK/CommonWords5.txt').read().split('\n') #100 ord, 5 bokstäver längd
commonWords = open('C:/MLprojekt/SSK/CommonWords6.txt').read().split('\n') #100 ord, 6 bokstäver längd
#commonWords = open('C:/MLprojekt/SSK/CommonWords54.txt').read().split('\n') #5 ord, 4 bokstäver längd
#commonWords = open('C:/MLprojekt/SSK/CommonWords55.txt').read().split('\n') #5 ord, 5 bokstäver längd
#commonWords = open('C:/MLprojekt/SSK/CommonWords56.txt').read().split('\n') #5 ord, 6 bokstäver längd

print(len(commonWords))
trainingSize = 20   #These are the ones you change
testSize = 20       #These are the ones you change
count = 0
ssk = Ssk(n, lam)

def getFiles(path, path2, amount, testSize):

    #print('fetching ', amount, ' files')
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

def preCalculateSSK(dataSet, words):

    #print('Initiating kernel calculations')
    sskCal = np.zeros((len(dataSet), len(words)))
    for i in range(len(dataSet)):
        for j in range(len(words)):
            sskCal[i][j] = ssk.kernel(dataSet[i], words[j])

    return sskCal

def calculateGram(dataSet, dataSet2):
    gram = np.zeros((len(dataSet), len(dataSet2)))
    for i in range(len(dataSet)):
        for j in range(len(dataSet2)):
            value = 0
            for k in range(len(dataSet[0])):
                value += dataSet[i][k] * dataSet2[j][k]
            gram[i][j] = value    
    
    #print('normalizing, length: ', len(dataSet), ' ', len(dataSet2))
    for i in range(len(dataSet)):
        for j in range(len(dataSet)):
            if(gram[i][i] == 0 or gram[j][j] == 0):
                gram[i][j] = 0
            else:
                gram[i][j] = gram[i][j]/math.sqrt(gram[i][i]*gram[j][j])

    return gram

trainingSet, trainingFileNames, trainingCats, testSet, testCategories = getFiles(trainingPath, trainingPath2, trainingSize, testSize)
preTraining = preCalculateSSK(trainingSet, commonWords)
preTest = preCalculateSSK(testSet, commonWords)
trainingGram = calculateGram(preTraining, preTraining)
testGram = calculateGram(preTest, preTraining)
"""
for i in range(len(testGram)):
    for j in range(len(testGram)):
        print(testGram[i][j])
    print('-----------')
"""
labels = np.array(trainingCats)
encoder = preprocessing.LabelEncoder()
encoder.fit(labels)
labels = encoder.transform(labels)

model = svm.SVC(kernel='precomputed')
model.fit(trainingGram, labels)
predictions = model.predict(testGram)

print("Using the SSK approximation kernel")
print("Checking ", category, "vs", category2)
print(testSize,"test documents")
print(trainingSize,"training documents")
print("The words are ", n , "long")
print("Using lambda", lam)
print("Using ",len(commonWords), "features")
print(predictions)

testLabels = np.array(testCategories)
encoder = preprocessing.LabelEncoder()
encoder.fit(trainingCats)
testLabels = encoder.transform(testLabels)
"""
for i in range(len(trainingGram)):
    for j in range(len(trainingGram[0])):
        print(testGram[i][j])
    print('-----------')
"""
countNumberOfRights = 0
for i in range(len(testLabels)):
	if(predictions[i] == testLabels[i]):
		countNumberOfRights += 1

print("Correct :", countNumberOfRights/len(testLabels))
print('---------- ', time.time() - start, ' -----------')