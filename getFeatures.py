import os
import math
import time
import string
from nltk.corpus import reuters
from nltk.tokenize import word_tokenize


n = 5 #Length of each word
lam = 0.5
dict = {}
features = 100

def addDoc(doc, n):
    for i in range(len(doc) - n + 1):
        word = doc[i:i+n]
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

amount = 7769 #Number of the most common words to be kepts


testCats = 'C:/MLprojekt/SSK/reuters/reuters/testCats.txt'
trainingCats = open('C:/MLprojekt/SSK/reuters/reuters/trainingCats.txt')
trainingPath = 'C:/MLprojekt/SSK/reuters/FirstUpdatedTraining'  # path for training set
testPath = 'C:/MLprojekt/SSK/reuters/reuters/FirstUpdatedTest'  # path for test set
start = time.time()

training = []
test = []
count = 1
files = []
for file in os.listdir(trainingPath):
    files.append(file)
    f = open(trainingPath+'/'+file, 'r')
    training.append(addDoc(f.read(), n))
    f.close()
    print(amount - count , ' documents left')
    if (count == amount):
        break
    else:
        count += 1

newDict = sorted(dict, key=dict.get, reverse=True)[:features]

os.remove('C:/MLprojekt/SSK/CommonWords.txt') #Remove old file
new = open('C:/MLprojekt/SSK/CommonWords.txt', 'a') #Create new file
for word in newDict: #Write the most common words to file
    new.write(word)
    new.write('\n')
new.close()

print('Collection done!')


"""
file = trainingCats.read().split('\n')  #Used for fetching the categories 
for i in range(amount):                 #corresponding to each of the training texts
    for f in file:
        temp = f.split(' ')
        if (temp[0] == 'training/'+files[i]):
            text = f.replace('training/'+files[i]+' ', '')
            files[i] = text

os.remove('C:/MLprojekt/SSK/CommonWordsCategories.txt')
new = open('C:/MLprojekt/SSK/CommonWordsCategories.txt', 'a')
for file in files: #Write the categories of the most common words to file
    new.write(file)
    new.write('\n')
new.close
"""