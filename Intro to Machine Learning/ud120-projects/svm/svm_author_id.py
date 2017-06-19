#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################
#These lines effectively slice the training dataset down to 1% of its original size, tossing out 99% of the training data.
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

# create the classifier
clf = svm.SVC(kernel='rbf', C=10000)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

# make predictions on the test data
t1 = time()
pred = clf.predict(features_test)
print "training time:", round(time()-t1, 3), "s"

# calculate the accuracy of the prediction
accuracy = accuracy_score(pred, labels_test)
print "accuracy: %f " % accuracy
print pred[10], pred[26], pred[50]
# find out how many 1s (Chris) are in the predicted results
chris_counter = 0
for i in pred:
    if i == 1:
        chris_counter = chris_counter + 1
print "number of Chris class: %d " % chris_counter
