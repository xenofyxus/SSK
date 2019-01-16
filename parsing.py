import os
import string
from nltk.corpus import reuters
from nltk.tokenize import word_tokenize

#trainingPath = 'C:/MLprojekt/SSK/reuters/reuters/silver'  # path for training set
#testPath = 'C:/MLprojekt/SSK/reuters/reuters/test'  # path for test set
stopwords = open('C:/MLprojekt/SSK/reuters/reuters/stopwords',
                 'r')  # path for our stopwords document
# path for our new folder with parsed training data
#newTrainingPath = 'C:/MLprojekt/SSK/reuters/reuters/updatedTraining'
# path for our new folder with parsed test data
#newTestPath = 'C:/MLprojekt/SSK/reuters/reuters/updatedTest'

category = 'sugar'

value = 1
hashtable = {'key': 'value'}
for word in stopwords:
    word = word.replace('\n', '')
    hashtable[word] = value
    value = value + 1

def parseDoc(file, fileName, newPath):

    table = str.maketrans("", "", string.punctuation)
    for words in file:
        for word in words:
            word = word.translate(table)
            word = word.lower()
            if(not word in hashtable and word != ' '):
                newfile = open(newPath+'/'+fileName, 'a')
                newfile.write(" " + word)
                newfile.close()

    """for word in words:
        print(word)
        word = word.translate(table)
        word = word.lower()
        if(not word in hashtable):
            newfile = open(newPath+'/'+fileName, 'a')
            newfile.write(" " + word)
            newfile.close()"""

docs = reuters.fileids(categories=[category])
count = 0
docAmount = len(docs)

trainingPath = 'C:/MLprojekt/SSK/reuters/reuters/'+category+'Training'
testPath = 'C:/MLprojekt/SSK/reuters/reuters/'+category+'Test'
if (not os.path.exists(trainingPath)):
    os.makedirs(trainingPath)
if (not os.path.exists(testPath)):
    os.makedirs(testPath)
        
for doc in docs:
    count += 1
    if (doc.find('test') != -1):
        name = doc.replace('test/', '')
        document = reuters.paras(fileids=[doc])
        parseDoc(document[0], name, testPath)
    else:
        name = doc.replace('training/', '')
        document = reuters.paras(fileids=[doc])
        parseDoc(document[0], name, trainingPath)
    
    print(docAmount - count, ' documents left')


# Parses a file, removing all stopwords and saves it with the same name in the new folder
"""
def parse(file, filename, newPath):
    lines = file.read()
    words = lines.split()
    table = str.maketrans("", "", string.punctuation)

    for word in words:
        word = word.translate(table)
        word = word.lower()
        if(not word in hashtable):
            newfile = open(newPath+'/'+filename, 'a')
            newfile.write(" " + word)
            newfile.close()


counter = 0
# for file in os.listdir(trainingPath):
#    counter = counter + 1
#    f = open(trainingPath+'/'+file, 'r')
#    parse(f, file, newTrainingPath)
#    f.close()
#    print('Done with document ', file, ' | ', 7769 - counter, ' documents left')

counter = 0
# for file in os.listdir(testPath):
#counter = counter + 1
#f = open(testPath+'/'+file, 'r')
#parse(f, file, newTestPath)
# f.close()
#print('Done with document ', file, ' | ', 3019-counter, ' documents left')

#3019 & 7769
"""