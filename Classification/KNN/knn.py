'''
sklearn: https://stackabuse.com/k-nearest-neighbors-algorithm-in-python-and-scikit-learn/
Python from scratch: https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

NOTE: we should standardize data if necessary
'''


import numpy as np
import heapq

class KnnClassifier(object):

    def __init__(self, k=5):
        self.X = None
        self.y = None
        self.neighbor = k

    def fit(self, X, y):
        self.X = X[:]
        self.y = y[:]

    def predict(self, Xtest):

        preds = []
        for data in Xtest:

            heap = []
            for i in range(len(self.X)):
                heapq.heappush(heap, (self.distance(data, self.X[i]), self.y[i]))
                # print (self.distance(data, self.X[i]))

            pred = {0: 0, 1:0}
            k = 0
            while k < self.neighbor:
                dist, y = heapq.heappop(heap)
                if dist != 0.0:
                    pred[y] += 1
                    k += 1
            
            preds.append(0 if pred[0] >= pred[1] else 1)

        return preds



    def distance(self, a, b):
        return np.sqrt(sum([(a[i]-b[i])**2 for i in range(len(a))]))
    

X = [[2.7810836,2.550537003],
	[1.465489372,2.362125076],
	[3.396561688,4.400293529],
	[7.627531214,2.759262235],
	[5.332441248,2.088626775],
	[6.922596716,1.77106367]]

y = [0,0,0,1,1,1]

knn = KnnClassifier(k=6)
knn.fit(X, y)

X_test = [[1.38807019,1.850220317],
	[3.06407232,3.005305973],
	[8.675418651,-0.242068655],
	[7.673756466,3.508563011]]

y_test = [0,0,1,1]

y_pred = knn.predict(X_test)
print (y_pred)