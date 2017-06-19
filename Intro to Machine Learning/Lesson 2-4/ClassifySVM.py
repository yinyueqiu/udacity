def classify(features_train, labels_train):
    ### import the sklearn module for SVC module
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier


    ### your code goes here!
    from sklearn.svm import SVC
    clf = SVC(C=1, gamma = 100)
    return clf.fit(features_train, labels_train)
