import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

class Kmeans_and_classification(object):
    def __init__(self, data, output='add', classifier=LogisticRegression()):
        self.split_training_test(data)
        self.output = output
        self.model = classifier
        
    def split_training_test(self, data):
        X, Y = pd.DataFrame(data.data), data.target
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, Y, test_size=0.3)
    
    def run_combined_model(self):
        self.Kmeans()
        self.classify()
    
    def Kmeans(self):
        n_clusters = len(np.unique(self.y_train))
        clf = KMeans(n_clusters = n_clusters)
        clf.fit(self.X_train)
    
        y_labels_train = clf.labels_
        y_labels_test = clf.predict(self.X_test)
    
        if self.output == 'replace':
            self.X_train = y_labels_train[:, np.newaxis]
            self.X_test = y_labels_test[:, np.newaxis]
        elif self.output == 'add':
            self.X_train['clust_label'] = y_labels_train
            self.X_test['clust_label'] = y_labels_test
        else:
            raise ValueError('output should be either add or replace')

    def classify(self):
        self.model.fit(self.X_train, self.y_train)
        y_test_pred = self.model.predict(self.X_test)
        print('Accuracy: {}'.format(accuracy_score(self.y_test, y_test_pred)))