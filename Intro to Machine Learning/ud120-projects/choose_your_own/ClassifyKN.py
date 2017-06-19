def classify(features_train, labels_train):

    ### your code goes here--should return a trained decision tree classifer
    from sklearn.neighbors import KNeighborsClassifier
    clf = KNeighborsClassifier(n_neighbors = 20)
    clf.fit(features_train, labels_train)

    return clf
