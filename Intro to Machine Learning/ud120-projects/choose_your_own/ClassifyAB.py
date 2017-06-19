def classify(features_train, labels_train):

    ### your code goes here--should return a trained decision tree classifer
    from sklearn.ensemble import AdaBoostClassifier
    clf = AdaBoostClassifier(n_estimators=20, learning_rate=2.0)
    clf.fit(features_train, labels_train)

    return clf
