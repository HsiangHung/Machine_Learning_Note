

def get_distance(x1, x2):
    return [(x1[d]-x2[d])**2 for d in range(len(x1))]

class KMeans(object):
    def __init__(self, data):
        self.data = data

    def train(self, k=2):

        centroids = self.initialize_centroids(k)

        update, iteration = True, 0
        while update and iteration <= 500:
            
            # print (iteration, centroids)

            labels = self.assign_labels(centroids)
            new_centroids = self.get_new_centroids(labels)

            if self.ifStop(centroids, new_centroids):
                update = False
            # else:
            #     centroids = self.update_centroids(centroids, new_centroids)

            centroids[:] = new_centroids[:]

            # print (centroids)
            # print ('----------------')

            iteration += 1

        print (iteration, centroids)

    def update_centroids(self, centroids, new_centroids):
        for c in range(len(centroids)):
            for f in range(len(centroids[0])):
                df = new_centroids[c][f]-centroids[c][f]
                centroids[c][f] += 0.01*df
        return centroids

    def ifStop(self, centroids, new_centroids):
        stop = True
        for c in range(len(centroids)):
            for f in range(len(centroids[0])):
                if abs(centroids[c][f]-new_centroids[c][f]) > 0.001: return False
        return stop


    def get_new_centroids(self, labels):

        num_features = len(self.data[0])
        label_coord, num_data_class = {}, {}

        for i in range(len(self.data)):
            c = labels[i]
            if c not in label_coord: label_coord[c] = [0]*num_features

            for f in range(num_features):
                label_coord[c][f] += self.data[i][f]

            num_data_class[c] = num_data_class.get(c, 0) + 1

        new_centroids = []
        for c in sorted(label_coord.keys()):
            coord = []
            for f in range(num_features):
                coord.append(float(label_coord[c][f])/num_data_class[c])
            new_centroids.append(coord)

        return new_centroids


    def assign_labels(self, centroids):
        labels = []
        for i in range(len(self.data)):

            min_dist, tag = get_distance(self.data[i], centroids[0]), 0
            for k in range(1, len(centroids)):
                dist = get_distance(self.data[i], centroids[k])
                if dist < min_dist:
                    min_dist, tag = dist, k
            labels.append(tag)

        return labels

    def initialize_centroids(self, k):
        import random
        centroids = []
        while len(centroids) < k:
            i = random.randint(0, len(self.data)-1)
            if self.data[i] not in centroids:
                centroids.append(self.data[i])
        return centroids




data = [[1, 1], [0, 3], [6, 0], [7, 4], [0.5, -1], [6.5, 2], [3, 10], [3.5, 11]]
# data = [[1, 1], [0, 3], [6, 0], [7, 4], [0.5, -1], [6.5, 2]]
obj = KMeans(data)
obj.train(k=3)

print ([(1+0+0.5)/3, (1+3-1)/3], [(6+7+6.5)/3, (0+4+2)/3], [6.5/2, 21/2])