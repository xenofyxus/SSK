import os 
import string

trainingPath = 'C:/MLprojekt/SSK/reuters/reuters/training' #path for training set
testPath = 'C:/MLprojekt/SSK/reuters/reuters/test' #path for test set
stopwords = open('C:/MLprojekt/SSK/reuters/reuters/stopwords', 'r') #path for our stopwords document
newTrainingPath = 'C:/MLprojekt/SSK/reuters/reuters/updatedTraining' #path for our new folder with parsed training data
newTestPath = 'C:/MLprojekt/SSK/reuters/reuters/updatedTest' #path for our new folder with parsed test data

value = 1
hashtable = {'key': 'value'}

#Add words to a dictionary to easily search if a word is to be kept or not
for word in stopwords:
    word = word.replace('\n', '')
    hashtable[word] = value
    value = value + 1

#Parses a file, removing all stopwords and saves it with the same name in the new folder
def parse(file, filename, newPath):
    lines = file.read()
    words = lines.split()
    table = str.maketrans("","",string.punctuation)

    for word in words:
        word = word.translate(table)
        word = word.lower()
        if(not word in hashtable):
            newfile = open(newPath+'/'+filename, 'a')
            newfile.write(" " + word)
            newfile.close()

counter = 0
#for file in os.listdir(trainingPath):
#    counter = counter + 1 
#    f = open(trainingPath+'/'+file, 'r')
#    parse(f, file, newTrainingPath)
#    f.close()
#    print('Done with document ', file, ' | ', 7769 - counter, ' documents left')

counter = 0
for file in os.listdir(testPath):
    counter = counter + 1
    f = open(testPath+'/'+file, 'r')
    parse(f, file, newTestPath)
    f.close()
    print('Done with document ', file, ' | ', 3019-counter, ' documents left')

#3019 & 7769