def classify(features_train, labels_train):

    ### your code goes here--should return a trained decision tree classifer
    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier()
    clf.fit(features_train, labels_train)

    return clf
